import http.client
import json


class PrivXAPIResponse:
    """
    Response object for PrivX API library.

    Args:
        response_status: The response object to handle.
        expected_status: The expected response status.
        data: data from the response.read() method.
    """

    def __init__(
        self, response_status: http.HTTPStatus, expected_status: int, data: bytes
    ):
        if expected_status == response_status:
            self._ok = True
            self._data = self._get_json(data)
        else:
            self._ok = False
            response_struct = {
                "status": response_status,
                "details": self._get_json(data),
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

    def _get_json(self, json_data: bytes) -> dict:
        try:
            data = json.loads(json_data)
        except ValueError:
            data = {}
        return data
