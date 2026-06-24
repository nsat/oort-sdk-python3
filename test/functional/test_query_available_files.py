import time
from pathlib import Path


class TestQueryAvailableFiles:
    def test_empty_topic_returns_no_files(self, sdk, topic):
        response = sdk.query_available_files(topic)

        assert response.files == []

    def test_staged_file_appears_with_complete_fileinfo(
        self, sdk, topic, stage_inbound
    ):
        payload = b"inbound payload bytes"
        file_id = stage_inbound(topic, payload, name="first.bin")
        now = int(time.time())

        response = sdk.query_available_files(topic)

        assert len(response.files) == 1
        info = response.files[0]
        assert info.id == file_id
        assert info.size == len(payload)
        assert info.crc32
        assert not Path(info.path).exists()
        assert Path(info.path).name == "first.bin"
        assert abs(info.created - now) < 60
        assert abs(info.modified - now) < 60

    def test_topic_isolation(self, sdk, stage_inbound):
        topic_a = "topic_alpha"
        topic_b = "topic_bravo"
        a1 = stage_inbound(topic_a, b"alpha one", name="a1.bin")
        a2 = stage_inbound(topic_a, b"alpha two", name="a2.bin")
        b1 = stage_inbound(topic_b, b"bravo one", name="b1.bin")

        resp_a = sdk.query_available_files(topic_a)
        resp_b = sdk.query_available_files(topic_b)
        resp_unused = sdk.query_available_files("topic_unused")

        assert {f.id for f in resp_a.files} == {a1, a2}
        assert {f.id for f in resp_b.files} == {b1}
        assert resp_unused.files == []

    def test_does_not_raise_for_unused_topic(self, sdk, stage_inbound):
        # Callers are expected to poll query_available_files in a loop (see
        # SDK/samples/python/query.py). It must never raise for a well-formed
        # topic, even when other topics have files staged.
        stage_inbound("populated_topic", b"someone elses bytes")

        response = sdk.query_available_files("unrelated_topic")

        assert response.files == []

    def test_overflow_flag_when_many_files(self, sdk, topic, stage_inbound):
        # max_query defaults to 50 (see Agent.h). Staging 51 files forces
        # the cap and should surface as response.overflow is True.
        for i in range(51):
            stage_inbound(topic, f"payload {i}".encode(), name=f"f{i}.bin")

        response = sdk.query_available_files(topic)

        assert response.overflow is True
        assert len(response.files) == 50
