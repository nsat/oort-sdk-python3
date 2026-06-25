import os
import socket
import subprocess
import time
from pathlib import Path

import pytest
import requests

from oort_sdk_client import ApiClient, Configuration
from oort_sdk_client.api.sdk_api import SdkApi
from oort_sdk_client.models.send_file_request import SendFileRequest

STARTUP_TIMEOUT_S = 5.0


def _find_default_binary():
    bundled = Path(__file__).resolve().parent / "oort-server"
    if bundled.exists():
        return bundled
    p = Path(__file__).resolve().parent
    while p != p.parent:
        candidate = p / "agent" / "build" / "oort-server"
        if candidate.exists():
            return candidate
        p = p.parent
    return None


def _free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def _wait_ready(port, deadline):
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("localhost", port), timeout=0.5):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError(f"oort-agent did not become ready on port {port}")


@pytest.fixture(scope="session")
def agent_binary():
    env = os.environ.get("OORT_AGENT")
    path = Path(env) if env else _find_default_binary()
    if not path or not path.exists():
        raise AssertionError("oort-agent not found; set OORT_AGENT")
    return path


@pytest.fixture()
def agent_process(agent_binary, tmpdir):
    # Function-scoped: fresh agent + fresh workdir per test so metafile_cache
    # (5s TTL, hardcoded in Cache.h) cannot leak across tests.
    workdir = Path(str(tmpdir.mkdir("oort-workdir")))
    port = _free_port()
    log_path = workdir / "oort-agent.log"
    log_file = log_path.open("wb")
    proc = subprocess.Popen(
        [
            str(agent_binary),
            "-w",
            str(workdir),
            "-p",
            str(port),
            "-l",
            "debug",
        ],
        stdout=subprocess.DEVNULL,
        stderr=log_file,
    )
    try:
        _wait_ready(port, time.monotonic() + STARTUP_TIMEOUT_S)
        yield workdir, port
    except RuntimeError:
        print("\n--- oort-agent log ---")
        print(log_path.read_text(errors="replace"))
        raise
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
        log_file.close()


@pytest.fixture()
def agent_workdir(agent_process):
    return agent_process[0]


@pytest.fixture()
def sdk(agent_process):
    _, port = agent_process
    cfg = Configuration(host=f"http://localhost:{port}/sdk/v1")
    return SdkApi(ApiClient(cfg))


def _topic_counter():
    n = 0
    while True:
        yield f"topic_{n}"
        n += 1


_topics = _topic_counter()


@pytest.fixture()
def topic():
    return next(_topics)


@pytest.fixture()
def make_source(tmp_path):
    counter = {"n": 0}

    def _make(data, name="payload.bin"):
        counter["n"] += 1
        sub = tmp_path / f"src-{counter['n']}"
        sub.mkdir()
        path = sub / name
        path.write_bytes(data)
        return path.resolve()

    return _make


@pytest.fixture()
def collector_meta(agent_process):
    _, port = agent_process

    def _get(file_id):
        resp = requests.get(
            f"http://localhost:{port}/collector/v1/meta/{file_id}", timeout=2
        )
        resp.raise_for_status()
        return resp.json()

    return _get


@pytest.fixture()
def stage_inbound(sdk, agent_workdir, make_source):
    # send_file writes to transfers/; rename the pair into uploads/ to
    # simulate collector delivery. Format stays in sync with the real agent
    # because the files are produced by the real code path.
    transfers = agent_workdir / "transfers"
    uploads = agent_workdir / "uploads"

    def _stage(topic, data, name="inbound.bin"):
        src = make_source(data, name)
        response = sdk.send_file(
            SendFileRequest(
                topic=topic, destination="ground", filepath=str(src)
            )
        )
        file_id = response.uuid
        for ext in (".data.oort", ".meta.oort"):
            (transfers / f"{file_id}{ext}").rename(uploads / f"{file_id}{ext}")
        return file_id

    return _stage
