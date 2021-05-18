from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse, PrivXStreamResponse
from privx_api.utils import get_value


class AuthorizerAPI(BasePrivXAPI):
    def get_authorizer_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.AUTHORIZER.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_authorizer_cert(
        self, access_group_id: Optional[str] = None
    ) -> PrivXAPIResponse:
        """
        Gets authorizer's root certificate.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.AUTHORIZER.AUTHORIZER_CERT,
            query_params={"access_group_id": access_group_id}
            if access_group_id
            else None,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def download_authorizer_cert(self, cert_id: str) -> PrivXStreamResponse:
        """
        Gets authorizer's root certificate.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.AUTHORIZER_CERT_ID, path_params={"id": cert_id}
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def download_certificate_revocation_list(self, cert_id: str) -> PrivXStreamResponse:
        """
        Gets authorizer CA's certificate revocation list.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.CERT_REVOCATION_LIST, path_params={"id": cert_id}
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def get_target_host_credentials(
        self,
        target_params: dict,
    ) -> PrivXAPIResponse:
        """
        Get target host credentials for the user.

        Returns:
            PrivXStreamResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.TARGET_HOST,
            body=target_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_authorizer_principals(self) -> PrivXAPIResponse:
        """
        Get defined principals from the authorizer.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.AUTHORIZER.PRINCIPALS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_group_principal_key(
        self,
        group_id: str,
        key_id: Optional[str] = None,
        filter_param: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Gets the principal key by its group ID.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            key_id=key_id,
            filter=filter_param,
        )
        response_status, data = self._http_get(
            UrlEnum.AUTHORIZER.GROUP_PRINCIPAL_KEY,
            path_params={"group_id": group_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_authorizer_principal_key(
        self, group_id: str, key_id: Optional[str] = None
    ) -> PrivXAPIResponse:
        """
        Deletes the principal key by its group ID.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(key_id=key_id)
        response_status, data = self._http_delete(
            UrlEnum.AUTHORIZER.GROUP_PRINCIPAL_KEY,
            path_params={"group_id": group_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_authorizer_principal_key(
        self,
        group_id: str,
    ) -> PrivXAPIResponse:
        """
        Create a principal key pair.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.CREATE_GROUP_PRINCIPAL_KEY,
            path_params={"group_id": group_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def import_authorizer_principal_key(
        self, group_id: str, principal_key_params: dict
    ) -> PrivXAPIResponse:
        """
        Import a principal key pair.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.IMPORT_GROUP_PRINCIPAL_KEY,
            path_params={"group_id": group_id},
            body=principal_key_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def sign_by_authorizer_principal_key(
        self,
        group_id: str,
        key_id: str,
        sign_params: dict,
    ) -> PrivXAPIResponse:
        """
        Get a signature.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(key_id=key_id)
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.SIGN_GROUP_PRINCIPAL_KEY,
            path_params={"group_id": group_id},
            query_params=search_params,
            body=sign_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_extender_certs(
        self, access_group_id: Optional[str] = None
    ) -> PrivXAPIResponse:
        """
        Gets authorizer's extender CA certificates.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(access_group_id=access_group_id)
        response_status, data = self._http_get(
            UrlEnum.AUTHORIZER.EXTENDER_CERTS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def download_extender_cert(self, cert_id: str) -> PrivXStreamResponse:
        """
        Gets authorizer's extender CA certificate.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.EXTENDER_CERT, path_params={"id": cert_id}
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def download_extender_cert_revocation_list(
        self, cert_id: str
    ) -> PrivXStreamResponse:
        """
        Gets authorizer CA's certificate revocation list.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.EXTENDER_CERT_REVOCATION_LIST,
            path_params={"id": cert_id},
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def enroll_end_entity_cert(
        self,
        enrollment_params: dict,
    ) -> PrivXAPIResponse:
        """
        Enroll an EE certificate from extender CA.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.ENROLL_END_ENTITY_CERT,
            body=enrollment_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def revoke_extender_cert(
        self,
        revocation_params: dict,
    ) -> PrivXAPIResponse:
        """
        Revoke a certificate.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.REVOKE_EXTENDER_CERT,
            body=revocation_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_extender_config_download_handle(
        self,
        trusted_client_id: str,
    ) -> PrivXAPIResponse:
        """
        Gets a extender-config.toml pre-configured for this PrivX installation.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.EXTENDER_CONFIG_SESSION_ID,
            path_params={"trusted_client_id": trusted_client_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def download_extender_config(
        self,
        trusted_client_id: str,
        session_id: str,
    ) -> PrivXStreamResponse:
        """
        Gets a extender-config.toml pre-configured for this PrivX installation.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.EXTENDER_CONFIG,
            path_params={
                "trusted_client_id": trusted_client_id,
                "session_id": session_id,
            },
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def create_deployment_script_download_handle(
        self, trusted_client_id: str
    ) -> PrivXAPIResponse:
        """
        Gets a deployment script pre-configured for this PrivX installation.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.DEPLOYMENT_SCRIPT_SESSION_ID,
            path_params={"trusted_client_id": trusted_client_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def download_deployment_script(
        self,
        trusted_client_id: str,
        session_id: str,
    ) -> PrivXStreamResponse:
        """
        Gets a deployment script pre-configured for this PrivX installation.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.DOWNLOAD_DEPLOYMENT_SCRIPT,
            path_params={
                "trusted_client_id": trusted_client_id,
                "session_id": session_id,
            },
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def download_principal_command_script(self) -> PrivXStreamResponse:
        """
        Gets the principals_command.sh script.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.DOWNLOAD_COMMAND_SCRIPT,
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def create_carrier_config_download_handle(
        self, trusted_client_id: str
    ) -> PrivXAPIResponse:
        """
        Gets a carrier-config.toml pre-configured for this PrivX installation.

        Returns:
            PrivXStreamResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.CARRIER_CONFIG_SESSION_ID,
            path_params={"trusted_client_id": trusted_client_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def download_carrier_config(
        self,
        trusted_client_id: str,
        session_id: str,
    ) -> PrivXStreamResponse:
        """
        Gets a carrier-config.toml pre-configured for this PrivX installation.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.DOWNLOAD_CARRIER_CONFIG,
            path_params={
                "trusted_client_id": trusted_client_id,
                "session_id": session_id,
            },
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def create_web_proxy_config_download_handle(
        self, trusted_client_id: str
    ) -> PrivXAPIResponse:
        """
        Gets a web-proxy-config.toml pre-configured for this PrivX installation.

        Returns:
            PrivXStreamResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.WEB_PROXY_CONFIG_SESSION_ID,
            path_params={"trusted_client_id": trusted_client_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def download_web_proxy_config(
        self,
        trusted_client_id: str,
        session_id: str,
    ) -> PrivXStreamResponse:
        """
        Gets a web-proxy-config.toml pre-configured for this PrivX installation.

        Returns:
            PrivXStreamResponse
        """
        response = self._http_stream(
            UrlEnum.AUTHORIZER.DOWNLOAD_CARRIER_CONFIG,
            path_params={
                "trusted_client_id": trusted_client_id,
                "session_id": session_id,
            },
        )
        return PrivXStreamResponse(response, HTTPStatus.OK)

    def get_cert_auth_templates(
        self, service: Optional[str] = None
    ) -> PrivXAPIResponse:
        """
        Returns the certificate authentication templates for the service.

        Returns:
            PrivXStreamResponse
        """
        search_params = self._get_search_params(service=service)
        response_status, data = self._http_get(
            UrlEnum.AUTHORIZER.CERT_AUTH_TEMPLATES,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_ssl_trust_anchor(self) -> PrivXAPIResponse:
        """
        Returns the SSL trust anchor (PrivX TLS CA certificate).

        Returns:
            PrivXStreamResponse
        """
        response_status, data = self._http_get(
            UrlEnum.AUTHORIZER.SSL_TRUST_ANCHOR,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_extender_trust_anchor(self) -> PrivXAPIResponse:
        """
        Returns the extender trust anchor (PrivX Extender CA certificate).

        Returns:
            PrivXStreamResponse
        """
        response_status, data = self._http_get(
            UrlEnum.AUTHORIZER.EXTENDER_TRUST_ANCHOR,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_access_groups(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get access groups.

        Returns:
            PrivXStreamResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
        )
        response_status, data = self._http_get(
            UrlEnum.AUTHORIZER.ACCESS_GROUPS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_access_group(self, access_group_params: dict) -> PrivXAPIResponse:
        """
        Create access group.

        Returns:
            PrivXStreamResponse
        """
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.ACCESS_GROUPS,
            body=access_group_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def search_access_groups(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        access_group_params: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Get access groups.

        Returns:
            PrivXStreamResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
        )
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.SEARCH_ACCESS_GROUPS,
            query_params=search_params,
            body=get_value(access_group_params, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_access_group(self, access_group_id: str) -> PrivXAPIResponse:
        """
        Get access group.

        Returns:
            PrivXStreamResponse
        """
        response_status, data = self._http_get(
            UrlEnum.AUTHORIZER.ACCESS_GROUP,
            path_params={"id": access_group_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_access_group(
        self, access_group_id: str, access_group_params: dict
    ) -> PrivXAPIResponse:
        """
        Update access group.

        Returns:
            PrivXStreamResponse
        """
        response_status, data = self._http_put(
            UrlEnum.AUTHORIZER.ACCESS_GROUP,
            path_params={"id": access_group_id},
            body=access_group_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_certificates(
        self,
        cert_params: dict,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Search certificates.

        Returns:
            PrivXStreamResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
        )
        response_status, data = self._http_post(
            UrlEnum.AUTHORIZER.SEARCH_CERTS,
            query_params=search_params,
            body=cert_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
