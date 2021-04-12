import http.client
import json


class PrivXAPIResponse:
    """
    Response object for PrivX API library.

    Args:
        response: The response object to handle.
        expected_status: The expected response status.
        data: data from the response.read() method.
    """

    def __init__(
        self, response: http.client.HTTPResponse, expected_status: int, data: bytes
    ):
        if expected_status == response.status:
            self._ok = True
            self._data = json.loads(data) if data else {}
        else:
            self._ok = False
            response_struct = {
                "status": response.status,
                "details": json.loads(data) if data else {},
            }
            self._data = response_struct

    def ok(self) -> bool:
        """
        Returns:
            Boolean wheter the call was successful or not
        """
        return self._ok

    def data(self) -> dict:
        """
        Returns:
            The response data
        """
        return self._data
