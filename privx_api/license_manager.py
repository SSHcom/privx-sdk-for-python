from http import HTTPStatus

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


class LicenseManagerAPI(BasePrivXAPI):
    def get_license_manager_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.LICENSE.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_license(self) -> PrivXAPIResponse:
        """
        Gets PrivX license.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.LICENSE.LICENSE)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def set_license(self, license_code: str) -> PrivXAPIResponse:
        """
        Post a new license to server.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.LICENSE.LICENSE,
            body=license_code,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def refresh_license(self) -> PrivXAPIResponse:
        """
        Refresh the license info.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.LICENSE.REFRESH,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def set_license_analytics(self, license_params: dict) -> PrivXAPIResponse:
        """
        Settings for SSH license statistics.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.LICENSE.OPT_IN,
            body=license_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def deactivate_license(self) -> PrivXAPIResponse:
        """
        Deactivate license.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.LICENSE.DEACTIVATE,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_mobilegw_registration_status(self) -> PrivXAPIResponse:
        """
        Get Mobile Gateway registration status

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.LICENSE.MGW_STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def register_privx_to_mobilegw(self) -> PrivXAPIResponse:
        """
        Register PrivX to the Mobile Gateway

        Returns:
            PrivXAPIResponse
        """
        response_status = self._http_post(UrlEnum.LICENSE.MGW_REGISTER)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, "")

    def unregister_privx_from_mobilegw(self) -> PrivXAPIResponse:
        """
        Unregister PrivX from the Mobile Gateway

        Returns:
            PrivXAPIResponse
        """
        response_status = self._http_post(UrlEnum.LICENSE.MGW_UNREGISTER)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, "")
