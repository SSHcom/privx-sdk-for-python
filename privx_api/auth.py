from http import HTTPStatus

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


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

    def get_auth_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.AUTH.STATUS, auth_required=False)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
