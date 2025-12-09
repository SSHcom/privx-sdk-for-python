from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse
from privx_api.utils import get_value


class HostStoreAPI(BasePrivXAPI):
    def get_host_store_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.HOST_STORE.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_hosts(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        filter_param: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search for hosts

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
            filter=filter_param,
        )

        response_status, data = self._http_post(
            UrlEnum.HOST_STORE.SEARCH,
            query_params=search_params,
            body=get_value(search_payload, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_hosts(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        filter_param: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get hosts.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
            filter=filter_param,
        )

        response_status, data = self._http_get(
            UrlEnum.HOST_STORE.HOSTS, query_params=search_params
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_host(self, host: dict) -> PrivXAPIResponse:
        """
        Create a host, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(UrlEnum.HOST_STORE.HOSTS, body=host)
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def resolve_host(self, host_resolve_params: dict) -> PrivXAPIResponse:
        """
        Resolve service+address to a single host in host store.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.HOST_STORE.RESOLVE,
            body=host_resolve_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_host(self, host_id: str) -> PrivXAPIResponse:
        """
        Get a single host in host store.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.HOST_STORE.HOST,
            path_params={"host_id": host_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_host(self, host_id: str, host: dict) -> PrivXAPIResponse:
        """
        Update a host, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.HOST_STORE.HOST, path_params={"host_id": host_id}, body=host
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_host(self, host_id: str) -> PrivXAPIResponse:
        """
        Delete host record, required field host_id.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.HOST_STORE.HOST, path_params={"host_id": host_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def set_host_deployable(
        self, host_id: str, deployable_params: dict
    ) -> PrivXAPIResponse:
        """
        Set a host to be deployable or undeployable.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.HOST_STORE.DEPLOYABLE,
            path_params={"host_id": host_id},
            body=deployable_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_host_tags(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        query: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get list of host's tags.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            query=query,
            sortdir=sort_dir,
        )
        response_status, data = self._http_get(
            UrlEnum.HOST_STORE.TAGS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def set_host_disabled_status(
        self, host_id: str, host_params: dict
    ) -> PrivXAPIResponse:
        """
        Enable/disable host.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.HOST_STORE.DISABLE,
            path_params={"host_id": host_id},
            body=host_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def resolve_host_realm(self, realm_params: dict) -> PrivXAPIResponse:
        """
        Resolve address to a single host in host store and return web
        connections for user ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.HOST_STORE.REALM,
            body=realm_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_default_service_options(self) -> PrivXAPIResponse:
        """
        Get the default service options.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.HOST_STORE.SETTINGS,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_command_restriction_whitelists(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        query: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get all whitelists.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            query=query,
            sortdir=sort_dir,
        )
        response_status, data = self._http_get(
            UrlEnum.HOST_STORE.WHITELISTS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_command_restriction_whitelist(self, whitelist: dict) -> PrivXAPIResponse:
        """
        Create a whitelist, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.HOST_STORE.WHITELISTS,
            body=whitelist,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_command_restriction_whitelist(self, whitelist_id: str) -> PrivXAPIResponse:
        """
        Get a whitelist by id.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.HOST_STORE.WHITELIST,
            path_params={"whitelist_id": whitelist_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_command_restriction_whitelist(
        self, whitelist_id: str
    ) -> PrivXAPIResponse:
        """
        Remove a whitelist by id.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.HOST_STORE.WHITELIST,
            path_params={"whitelist_id": whitelist_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_command_restriction_whitelist(
        self, whitelist_id: str, whitelist: dict
    ) -> PrivXAPIResponse:
        """
        Update a whitelist by id, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.HOST_STORE.WHITELIST,
            path_params={"whitelist_id": whitelist_id},
            body=whitelist,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_command_restriction_whitelists(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:
        """
        Search for whitelists, more granular search could be done
        via "keywords" body param
        search_payload = {
            "keywords": "common_whitelist,allow_all_cmds",
        }

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
        )

        response_status, data = self._http_post(
            UrlEnum.HOST_STORE.WHITELIST_SEARCH,
            query_params=search_params,
            body=get_value(search_payload, dict()),
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def eval_commands_against_whitelist(
        self, whitelist: dict, rshell_variant: str, cmds: [str]
    ) -> PrivXAPIResponse:
        """
        Evaluate commands against the whitelist,see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.HOST_STORE.WHITELIST_EVALUATE,
            body={
                "whitelist": whitelist,
                "rshell_variant": rshell_variant,
                "commands": cmds,
            },
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_session_host_certificates(
        self,
        host_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get session host certificates.

        Returns:
            PrivXAPIResponse
        """

        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortkey=sort_key,
            sortdir=sort_dir,
        )

        response_status, data = self._http_get(
            UrlEnum.HOST_STORE.SESSION_HOST_CERTS,
            path_params={"host_id": host_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_session_host_certificates(self, host_id: str) -> PrivXAPIResponse:
        """
        Delete host's session hosts certificates.

        Returns:
            PrivXAPIResponse
        """

        response_status, data = self._http_delete(
            UrlEnum.HOST_STORE.SESSION_HOST_CERTS,
            path_params={"host_id": host_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_session_host_certificate(
        self,
        host_id: str,
        certificate_id: str,
    ) -> PrivXAPIResponse:
        """
        Delete a session host's certificate.

        Returns:
            PrivXAPIResponse
        """

        response_status, data = self._http_delete(
            UrlEnum.HOST_STORE.SESSION_HOST_CERT,
            query_params={"host_id": host_id, "certificate_id": certificate_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
