import io
from http import HTTPStatus
from typing import Union

import pytest

from privx_api.exceptions import InternalAPIException
from privx_api.response import PrivXAPIResponse, PrivXStreamResponse


class DummyHTTPResponse:
    def __init__(
        self, payload: bytes, *, status: Union[int, HTTPStatus] = HTTPStatus.OK
    ) -> None:
        self._payload = io.BytesIO(payload)
        self.status = status

    def read(self, chunk_size: int = -1) -> bytes:
        return self._payload.read(chunk_size)

    def close(self) -> None:
        self._payload.close()


class DummyAPI:
    def __init__(self):
        self.last_response_headers = {}

    def response(
        self, status=HTTPStatus.OK, expected=HTTPStatus.OK, body=b"", headers=None
    ):
        self.last_response_headers = headers or {}
        return PrivXAPIResponse(
            status, expected, body, headers=headers or self.last_response_headers
        )

    def stream_response(self, payload=b"", headers=None):
        self.last_response_headers = headers or {}
        dummy_http_resp = DummyHTTPResponse(payload)
        return PrivXStreamResponse(
            dummy_http_resp, HTTPStatus.OK, headers=self.last_response_headers
        )


def test_api_response_content_and_text():
    api = DummyAPI()
    resp = api.response(
        body=b"secret", headers={"Content-Type": "text/plain; charset=utf-8"}
    )

    assert resp.ok is True
    assert resp.content == b"secret"


def test_api_response_json_detection():
    api = DummyAPI()
    resp = api.response(
        body=b'{"key": "value"}', headers={"Content-Type": "application/json"}
    )

    assert resp.data == {"key": "value"}


def test_api_response_data_on_non_expected_status_keeps_error_details():
    api = DummyAPI()
    resp = api.response(
        status=HTTPStatus.BAD_REQUEST,
        expected=HTTPStatus.OK,
        body=b'{"message":"bad request"}',
        headers={"Content-Type": "application/json"},
    )

    assert resp.ok is False
    assert resp.data == {
        "status": HTTPStatus.BAD_REQUEST,
        "details": {"message": "bad request"},
    }


def test_api_response_data_on_non_expected_status_uses_empty_details_for_invalid_json():
    api = DummyAPI()
    resp = api.response(
        status=HTTPStatus.BAD_REQUEST,
        expected=HTTPStatus.OK,
        body=b"not-json",
        headers={"Content-Type": "application/json"},
    )

    assert resp.ok is False
    assert resp.data == {"status": HTTPStatus.BAD_REQUEST, "details": {}}


def test_stream_response_iter_content():
    api = DummyAPI()
    resp = api.stream_response(payload=b"abcdef")
    chunks = list(resp.iter_content(2))
    assert chunks == [b"ab", b"cd", b"ef"]


def test_stream_response_data_property_raises():
    api = DummyAPI()
    resp = api.stream_response(payload=b"abcdef")

    with pytest.raises(InternalAPIException):
        _ = resp.data


def test_stream_response_keeps_non_standard_status_code():
    response = DummyHTTPResponse(b"payload", status=599)
    stream_response = PrivXStreamResponse(response, HTTPStatus.OK, headers={})

    assert stream_response.status == 599
    assert stream_response.ok is False


def test_normalize_headers_lowercases_keys():
    normalized = PrivXAPIResponse._normalize_headers(
        {"Content-Type": "application/json", "X-Request-Id": "req-1"}
    )

    assert normalized == {
        "content-type": "application/json",
        "x-request-id": "req-1",
    }


@pytest.mark.parametrize(
    "payload, expected",
    [
        (b'{"a": 1}', {"a": 1}),
        (b"", {}),
        (b"invalid", {}),
    ],
)
def test_get_json_staticmethod(payload, expected):
    assert PrivXAPIResponse._get_json(payload) == expected


@pytest.mark.parametrize(
    "payload, expected",
    [
        (None, b""),
        (b"raw", b"raw"),
        ("text", b"text"),
    ],
)
def test_to_bytes_staticmethod(payload, expected):
    assert PrivXAPIResponse._to_bytes(payload) == expected
