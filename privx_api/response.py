import http.client
import json
from io import BytesIO
from typing import Any, Generator, NoReturn, Optional, Union

from privx_api.exceptions import InternalAPIException


class BaseResponse:
    """Common response metadata shared by buffered and streamed responses."""

    def __init__(
        self,
        status: http.HTTPStatus,
        ok: bool,
        headers: Optional[dict] = None,
    ) -> None:
        """Store normalized HTTP status, success flag, and response headers."""
        self._status = status
        self._ok = ok
        self._headers = self._normalize_headers(headers or {})

    @property
    def ok(self) -> bool:
        """True when response status matches the expected status."""
        return self._ok

    @property
    def status(self) -> http.HTTPStatus:
        """Actual HTTP status returned by the server."""
        return self._status

    @property
    def headers(self) -> dict:
        """HTTP response headers as a normalized lowercase-key mapping."""
        return dict(self._headers)

    @property
    def data(self) -> NoReturn:
        """Response payload accessor implemented by concrete response classes."""
        raise NotImplementedError

    @staticmethod
    def _normalize_headers(headers: dict) -> dict:
        """Normalize header keys to lowercase for case-insensitive lookup."""
        return {str(k).lower(): v for k, v in headers.items()}


class PrivXAPIResponse(BaseResponse):
    """Buffered response for standard API methods (`GET`/`POST`/`PUT`/`DELETE`).

    Use this class when the full body is read into memory and callers need
    convenience helpers such as `.data`, `.json()`, `.text()`, and `.content`.
    """

    def __init__(
        self,
        response_status: http.HTTPStatus,
        expected_status: int,
        data: Union[bytes, str, None],
        headers: Optional[dict] = None,
    ) -> None:
        """Build a buffered response and derive backward-compatible `.data`."""
        ok = response_status == expected_status
        super().__init__(response_status, ok, headers=headers)
        self._raw = self._to_bytes(data)
        self._text_cache = None
        if ok:
            self._data = self._get_json(self._raw)
        else:
            self._data = {
                "status": response_status,
                "details": self._get_json(self._raw),
            }

    def __str__(self) -> str:
        """Readable response representation for logs/debugging."""
        return f"PrivXResponse {self._status}"

    @property
    def data(self) -> dict:
        """SDK-normalized payload kept for backward compatibility.

        Success responses return parsed JSON content.
        Non-success responses return `{"status": ..., "details": ...}`.
        """
        return self._data

    @property
    def content(self) -> bytes:
        """Raw response body bytes."""
        return self._raw

    def text(self, encoding: Optional[str] = None) -> str:
        """Decode body bytes into text using explicit or inferred charset."""
        if self._text_cache is None:
            enc = encoding or self._get_charset(self._headers.get("content-type"))
            self._text_cache = self._raw.decode(enc, errors="replace")
        return self._text_cache

    def json(self) -> dict:
        """Return parsed JSON body and fail if content type is not JSON."""
        if "application/json" not in self._headers.get("content-type", ""):
            raise InternalAPIException("Response is not JSON")
        return self._get_json(self._raw)

    def iter_content(
        self, chunk_size: int = 1024 * 1024
    ) -> Generator[bytes, Any, None]:
        """Yield buffered body in chunks for API parity with stream responses."""
        buffer = BytesIO(self._raw)
        while True:
            chunk = buffer.read(chunk_size)
            if not chunk:
                break
            yield chunk

    @staticmethod
    def _get_json(json_data: bytes) -> dict:
        """Parse JSON body and return empty dict for invalid/empty JSON."""
        try:
            return json.loads(json_data)
        except ValueError:
            return {}

    @staticmethod
    def _to_bytes(data: Union[bytes, str, None]) -> bytes:
        """Normalize supported body input types to bytes."""
        if data is None:
            return b""
        if isinstance(data, bytes):
            return data
        return data.encode("utf-8")

    @staticmethod
    def _get_charset(content_type: Optional[str]) -> str:
        """Extract charset from a Content-Type header, defaulting to UTF-8."""
        if not content_type:
            return "utf-8"
        for part in str(content_type).split(";"):
            part = part.strip()
            if part.lower().startswith("charset="):
                charset = part.split("=", 1)[1].strip()
                if charset:
                    return charset
        return "utf-8"


class PrivXStreamResponse(BaseResponse):
    """Streaming response for endpoints that should be consumed incrementally.

    Use this class for large files/artifacts where reading the whole response
    into memory would be unnecessary or expensive.
    """

    def __init__(
        self,
        response: http.client.HTTPResponse,
        expected_status: int,
        headers: Optional[dict] = None,
    ) -> None:
        """Wrap an open `HTTPResponse` and expose a chunk iterator."""
        ok = response.status == expected_status
        super().__init__(response.status, ok, headers=headers)
        self._response = response

    def __str__(self) -> str:
        """Readable stream response representation for logs/debugging."""
        return f"PrivXStreamResponse {self._status}"

    @property
    def data(self) -> NoReturn:
        """Stream responses do not support full in-memory payload access."""
        raise InternalAPIException("Should not access all data in a stream response")

    def iter_content(
        self, chunk_size: int = 1024 * 1024
    ) -> Generator[bytes, Any, None]:
        """Yield response bytes by chunk and always close the socket at end."""
        try:
            while True:
                chunk = self._response.read(chunk_size)
                if not chunk:
                    break
                yield chunk
        finally:
            self._response.close()
