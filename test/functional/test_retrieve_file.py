import os
import uuid

import pytest
from pydantic import ValidationError

from oort_sdk_client.exceptions import ApiException
from oort_sdk_client.models.retrieve_file_request import RetrieveFileRequest


class TestRetrieveFile:
    def test_round_trip_bytes(self, sdk, topic, stage_inbound, tmp_path):
        payload = b"round-trip payload " + uuid.uuid4().bytes
        file_id = stage_inbound(topic, payload, name="roundtrip.bin")
        dest = tmp_path / "out.bin"

        response = sdk.retrieve_file(
            RetrieveFileRequest(id=file_id, save_path=str(dest))
        )

        assert dest.read_bytes() == payload
        assert response.id == file_id
        assert response.size == len(payload)

    def test_empty_file_round_trip(self, sdk, topic, stage_inbound, tmp_path):
        file_id = stage_inbound(topic, b"", name="empty.bin")
        dest = tmp_path / "out.bin"

        response = sdk.retrieve_file(
            RetrieveFileRequest(id=file_id, save_path=str(dest))
        )

        assert dest.read_bytes() == b""
        assert response.size == 0

    def test_round_trip_large_payload(
        self, sdk, topic, stage_inbound, tmp_path
    ):
        # 1mb of bytes exercises move_file's (see Agent.cpp) buffered copy and
        # CRC32 calculation over a size that a tiny payload wouldn't reach.
        payload = os.urandom(1024 * 1024)
        file_id = stage_inbound(topic, payload, name="large.bin")
        dest = tmp_path / "out.bin"

        sdk.retrieve_file(RetrieveFileRequest(id=file_id, save_path=str(dest)))

        assert dest.read_bytes() == payload

    def test_consumes_inbound_entry(self, sdk, topic, stage_inbound, tmp_path):
        file_id = stage_inbound(topic, b"consumed", name="once.bin")
        dest = tmp_path / "out.bin"

        sdk.retrieve_file(RetrieveFileRequest(id=file_id, save_path=str(dest)))

        assert sdk.query_available_files(topic).files == []

    def test_retrieves_many_files_in_a_loop(
        self, sdk, topic, stage_inbound, tmp_path
    ):
        payloads = {
            stage_inbound(topic, b"first bytes", name="a.bin"): b"first bytes",
            stage_inbound(
                topic, b"second bytes", name="b.bin"
            ): b"second bytes",
            stage_inbound(topic, b"third bytes", name="c.bin"): b"third bytes",
        }

        available = sdk.query_available_files(topic).files
        retrieved = {}
        for f in available:
            dest = tmp_path / f"{f.id}.bin"
            sdk.retrieve_file(
                RetrieveFileRequest(id=f.id, save_path=str(dest))
            )
            retrieved[f.id] = dest.read_bytes()

        assert retrieved == payloads
        assert sdk.query_available_files(topic).files == []

    def test_rejects_relative_save_path(self):
        with pytest.raises(ValidationError):
            RetrieveFileRequest(
                id="00000000-0000-0000-0000-000000000000", save_path="out.bin"
            )

    def test_unknown_id_raises(self, sdk, tmp_path):
        dest = tmp_path / "nowhere.bin"
        bogus_id = "00000000-0000-0000-0000-000000000000"

        with pytest.raises(ApiException) as excinfo:
            sdk.retrieve_file(
                RetrieveFileRequest(id=bogus_id, save_path=str(dest))
            )

        assert excinfo.value.status == 400
        assert "meta file unreadable" in excinfo.value.body.lower()

    def test_double_retrieve_of_same_id_fails_cleanly(
        self, sdk, topic, stage_inbound, tmp_path
    ):
        # After a successful retrieve the meta file is deleted, so a second
        # retrieve of the same id must surface the same "meta file unreadable"
        # error as an unknown id — locks in the behaviour under races where
        # two callers try to claim the same file.
        file_id = stage_inbound(topic, b"claim me once")
        dest = tmp_path / "out.bin"
        sdk.retrieve_file(RetrieveFileRequest(id=file_id, save_path=str(dest)))

        with pytest.raises(ApiException) as excinfo:
            sdk.retrieve_file(
                RetrieveFileRequest(id=file_id, save_path=str(dest))
            )

        assert excinfo.value.status == 400
        assert "meta file unreadable" in excinfo.value.body.lower()
