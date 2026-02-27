import io
from http import HTTPStatus

import pytest

from privx_api.exceptions import InternalAPIException
from privx_api.response import PrivXAPIResponse, PrivXStreamResponse


class DummyHTTPResponse:
    def __init__(self, payload: bytes, *, status: HTTPStatus = HTTPStatus.OK) -> None:
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
    assert resp.text() == "secret"


def test_api_response_json_detection():
    api = DummyAPI()
    resp = api.response(
        body=b'{"key": "value"}', headers={"Content-Type": "application/json"}
    )

    assert resp.data == {"key": "value"}
    assert resp.json() == {"key": "value"}


def test_api_response_json_error_when_not_json():
    api = DummyAPI()
    resp = api.response(body=b"plain", headers={"Content-Type": "text/plain"})

    with pytest.raises(InternalAPIException):
        resp.json()


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


def test_api_response_iter_content_chunks():
    api = DummyAPI()
    resp = api.response(body=b"abcdefgh")
    chunks = list(resp.iter_content(3))
    assert chunks == [b"abc", b"def", b"gh"]


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


def test_response_text_defaults_to_utf8_when_content_type_has_no_charset():
    resp = PrivXAPIResponse(
        HTTPStatus.OK,
        HTTPStatus.OK,
        b'{"hello":"world"}',
        headers={"Content-Type": "application/json"},
    )

    assert resp.text() == '{"hello":"world"}'


def test_response_json_requires_explicit_or_provided_headers():
    resp = PrivXAPIResponse(HTTPStatus.OK, HTTPStatus.OK, b'{"v": 1}')

    with pytest.raises(InternalAPIException):
        resp.json()


def test_response_normalizes_string_payload_to_bytes():
    resp = PrivXAPIResponse(
        HTTPStatus.OK,
        HTTPStatus.OK,
        "plain-text",
        headers={"Content-Type": "text/plain; charset=utf-8"},
    )

    assert resp.content == b"plain-text"
    assert list(resp.iter_content(5)) == [b"plain", b"-text"]


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


@pytest.mark.parametrize(
    "content_type, expected",
    [
        (None, "utf-8"),
        ("application/json", "utf-8"),
        ("text/plain; charset=utf-16", "utf-16"),
        ("text/plain; Charset=latin-1", "latin-1"),
    ],
)
def test_get_charset_staticmethod(content_type, expected):
    assert PrivXAPIResponse._get_charset(content_type) == expected
