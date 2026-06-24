import uuid

import pytest
from pydantic import ValidationError

from oort_sdk_client.exceptions import ApiException
from oort_sdk_client.models.delivery_hints import DeliveryHints
from oort_sdk_client.models.send_file_request import SendFileRequest
from oort_sdk_client.models.send_options import SendOptions
from oort_sdk_client.models.ttl_params import TTLParams


def _send(sdk, topic, filepath, destination="ground"):
    return sdk.send_file(
        SendFileRequest(
            topic=topic, destination=destination, filepath=str(filepath)
        )
    )


class TestSendFile:
    def test_returns_uuid_and_consumes_source(self, sdk, topic, make_source):
        payload = b"hello oort " + uuid.uuid4().bytes
        src = make_source(payload)

        response = _send(sdk, topic, src)

        assert response.uuid
        uuid.UUID(response.uuid)
        assert not src.exists()

    def test_records_metadata_in_collector_meta(
        self, sdk, topic, make_source, collector_meta
    ):
        payload = b"metadata oracle " + uuid.uuid4().bytes
        src = make_source(payload)

        response = _send(sdk, topic, src)
        meta = collector_meta(response.uuid)

        assert meta["topic"] == topic
        assert meta["destination"] == "ground"
        assert meta["file_info"]["size"] == len(payload)
        assert meta["file_info"]["crc32"] != 0

    def test_round_trips_send_options(
        self, sdk, topic, make_source, collector_meta
    ):
        options = SendOptions(
            ttl_params=TTLParams(urgent=60, bulk=120, surplus=240),
            reliable=False,
            tags={"env": "test", "run": "smoke"},
            delivery_hints=DeliveryHints(
                dest_path="/var/data/out.bin", mode="640"
            ),
        )
        src = make_source(b"with options")

        response = sdk.send_file(
            SendFileRequest(
                topic=topic,
                destination="ground",
                filepath=str(src),
                options=options,
            )
        )
        meta = collector_meta(response.uuid)
        stored_options = meta["send_options"]

        assert stored_options["TTLParams"] == {
            "urgent": 60,
            "bulk": 120,
            "surplus": 240,
        }
        assert stored_options["reliable"] is False
        assert stored_options["tags"] == {"env": "test", "run": "smoke"}
        assert stored_options["delivery_hints"] == {
            "dest_path": "/var/data/out.bin",
            "mode": "640",
        }

    def test_uuids_are_unique_across_calls(self, sdk, topic, make_source):
        src1 = make_source(b"first", name="a.bin")
        src2 = make_source(b"second", name="b.bin")

        uuid1 = _send(sdk, topic, src1).uuid
        uuid2 = _send(sdk, topic, src2).uuid

        assert uuid1 != uuid2

    def test_surfaces_nonexistent_source_error(self, sdk, topic, tmp_path):
        missing = tmp_path / "definitely_not_here.bin"

        with pytest.raises(ApiException) as excinfo:
            sdk.send_file(
                SendFileRequest(
                    topic=topic, destination="ground", filepath=str(missing)
                )
            )

        assert excinfo.value.status == 400
        assert excinfo.value.body

    def test_rejects_relative_filepath(self, topic):
        with pytest.raises(ValidationError):
            SendFileRequest(
                topic=topic, destination="ground", filepath="payload.bin"
            )

    def test_rejects_invalid_topic(self, sdk, make_source):
        src = make_source(b"bytes")
        bad_topic = "has spaces"

        with pytest.raises(ApiException) as excinfo:
            _send(sdk, bad_topic, src)

        assert excinfo.value.status == 400
        assert "topic" in excinfo.value.body.lower()
