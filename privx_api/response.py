import http.client
import json


class PrivXAPIResponse:
    """
    Response object for PrivX API library.

    Args:
        response: The response object to handle.
        expstatus: The expected response status.
    """

    def __init__(self, response: http.client.HTTPResponse, expstatus: int):
        if expstatus == response.status:
            self._ok = True
            self._data = {}

            content = response.read().strip()
            if len(content):
                self._data = json.loads(content)
        else:
            self._ok = False
            data = {
                "status": response.status,
                "details": {},
            }
            self._data = data

            content = response.read().strip()
            if len(content.strip()):
                data["details"] = json.loads(content)

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
