import http.client
import json
from typing import NoReturn

from privx_api.exceptions import InternalAPIException


class BaseResponse:
    def __init__(self) -> None:
        self._ok = None
        self._data = None

    @property
    def ok(self) -> bool:
        """
        Returns:
            Boolean wheter the call was successful or not
        """
        return self._ok

    @property
    def data(self) -> NoReturn:
        raise NotImplementedError

    def _get_json(self, json_data: bytes) -> dict:
        try:
            data = json.loads(json_data)
        except ValueError:
            data = {}
        return data


class PrivXAPIResponse(BaseResponse):
    """
    Response object for PrivX API library.

    Args:
        response_status: The response object to handle.
        expected_status: The expected response status.
        data: data from the response.read() method.
    """

    def __init__(
        self, response_status: http.HTTPStatus, expected_status: int, data: bytes
    ) -> None:
        super().__init__()
        self.status = response_status
        if expected_status == self.status:
            self._ok = True
            self._data = self._get_json(data)
        else:
            self._ok = False
            response_struct = {
                "status": self.status,
                "details": self._get_json(data),
            }
            self._data = response_struct

    def __str__(self) -> str:
        return "PrivXResponse {}".format(self.status)

    @property
    def data(self) -> dict:
        """
        Returns:
            The response data
        """
        return self._data


class PrivXStreamResponse(BaseResponse):
    """
    Example:
    with open("test.txt", "w") as file:
        for char in StreamResponseObject.iter_content(chunk_size):
            file.write(char.decode("utf-8"))
    """

    def __init__(
        self,
        response: http.client.HTTPResponse,
        expected_status: int,
    ) -> None:
        super().__init__()
        self._response = response
        self._status = response.status
        self._ok = self._status == expected_status

    def __str__(self) -> str:
        return "PrivXStreamResponse {}".format(self._status)

    @property
    def data(self) -> NoReturn:
        raise InternalAPIException("Should not access all data in a stream response")

    def iter_content(self, chunk_size: int = 1024 * 1024) -> bytes:
        """
        Generator for reading and returning response by chunk
        """

        try:
            while True:
                chunk = self._response.read(chunk_size)
                if not chunk:
                    break
                yield chunk
        finally:
            self._response.close()
