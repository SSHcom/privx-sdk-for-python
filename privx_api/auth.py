from privx_api.base import BasePrivXAPI


class AuthAPI(BasePrivXAPI):
    """
    PrivX Authentication API
    """

    def authenticate(self, username: str, password: str):
        """
        Login api client to the API.

        Raises:
            An InternalAPIException on failure
        """
        # TODO: should return PrivXAPIResponse
        self._authenticate(username, password)
