from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


class RoleStoreAPI(BasePrivXAPI):
    def get_role_store_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.
        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.STATUS,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_sources(self) -> PrivXAPIResponse:
        """
        Get sources.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.ROLE_STORE.SOURCES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_source(self, source_params: dict) -> PrivXAPIResponse:
        """
        Create a new source definition.
        Id, author, created & updated are automatically populated by the PrivX server.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.SOURCES,
            body=source_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_source(self, source_id: str) -> PrivXAPIResponse:
        """
        Get source object by ID.

        Returns:
            PrivxAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.SOURCE,
            path_params={"source_id": source_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_source(self, source_id: str) -> PrivXAPIResponse:
        """
        Delete source by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.ROLE_STORE.SOURCE,
            path_params={"source_id": source_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_source(self, source_id: str, source_params: dict) -> PrivXAPIResponse:
        """
        Update a source.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.ROLE_STORE.SOURCE,
            path_params={"source_id": source_id},
            body=source_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def refresh_source(self, source_ids: list) -> PrivXAPIResponse:
        """
        Fetch hosts from local host directory,
        or users from any user directory.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.REFRESH_SOURCES,
            body=source_ids,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_all_aws_roles(self, refresh: bool = False) -> PrivXAPIResponse:
        """
        Get all AWS roles from all sources.

        Returns:
             PrivXAPIResponse
        """
        search_params = self._get_search_params(
            refresh=refresh,
        )
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.AWS_ROLES,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_aws_role(self, aws_role_id: str) -> PrivXAPIResponse:
        """
        Get role object by ID.

        Returns:
             PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.AWS_ROLE,
            path_params={"awsrole_id": aws_role_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_aws_role(self, aws_role_id: str) -> PrivXAPIResponse:
        """
        Delete cached AWS role and its mappings on PrivX.
        Does not affect the AWS service, if the role still exists on AWS,
        it will re-appear on the next role scan..

         Returns:
              PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.ROLE_STORE.AWS_ROLE,
            path_params={"awsrole_id": aws_role_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_aws_role(self, aws_role_id: str, privx_roles: list) -> PrivXAPIResponse:
        """
        Update a AWS role granting PrivX roles.

         Returns:
              PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.ROLE_STORE.AWS_ROLE_PRIVX_ROLES,
            path_params={"awsrole_id": aws_role_id},
            body=privx_roles,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_privx_roles_granted_by_aws_role(self, aws_role_id: str) -> PrivXAPIResponse:
        """
        Get AWS role granting PrivX roles..

         Returns:
              PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.AWS_ROLE_PRIVX_ROLES,
            path_params={"awsrole_id": aws_role_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_roles(self) -> PrivXAPIResponse:
        """
        Get roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.ROLE_STORE.ROLES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_role(self, role: dict) -> PrivXAPIResponse:
        """
        Create a role, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(UrlEnum.ROLE_STORE.ROLES, body=role)
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def resolve_role(self, role_names: list) -> PrivXAPIResponse:
        """
        Resolve role names to role IDs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.RESOLVE, body=role_names
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def evaluate_role(self, role_params: dict) -> PrivXAPIResponse:
        """
        Evaluate a new role definition, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.EVALUATE, body=role_params
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_role(self, role_id: str) -> PrivXAPIResponse:
        """
        Get role object by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.ROLE, path_params={"role_id": role_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_role(self, role_id: str) -> PrivXAPIResponse:
        """
        Delete role by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.ROLE_STORE.ROLE, path_params={"role_id": role_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def update_role(self, role_id: str, role: dict) -> PrivXAPIResponse:
        """
        Update a role, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.ROLE_STORE.ROLE, path_params={"role_id": role_id}, body=role
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_role_members(
        self,
        role_id: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Get Role Members.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.MEMBERS,
            path_params={"role_id": role_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_aws_token(
        self, aws_role_id: str, ttl: int = 900, token_code: Optional[str] = None
    ) -> PrivXAPIResponse:
        """
        Fetch temporary AWS token for given AWS role name and TTL.
        User needs to have the requested AWS role mapped to the available PrivX role by
        PrivX admin.
        Allowed TTL values 900-3600 seconds for assume-role (configurable max 43200) and 900-129600
        for federation token.

        Get temporary AWS token for given AWS role.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(ttl=ttl, tokencode=token_code)
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.AWS_TOKEN,
            path_params={"awsrole_id": aws_role_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_principal_keys(self, role_id: str) -> PrivXAPIResponse:
        """
        Get role's principal key objects.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.PRINCIPAL_KEYS, path_params={"role_id": role_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def generate_principal_key(self, role_id: str) -> PrivXAPIResponse:
        """
        Generate new principal key for role.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.GENERATE_PRINCIPAL_KEY,
            path_params={"role_id": role_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def import_principal_key(self, role_id: str, primary_key: dict) -> PrivXAPIResponse:
        """
        Import new principal key for role.

        primary_key = {"primary_key" : "----row1----\nrow2\nrow3..."}

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.IMPORT_PRINCIPAL_KEY,
            path_params={"role_id": role_id},
            body=primary_key,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_principal_key(self, role_id: str, key_id: str) -> PrivXAPIResponse:
        """
        Get role's principal key object.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.PRINCIPAL_KEY,
            path_params={"role_id": role_id, "key_id": key_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_principal_key(self, role_id: str, key_id: str) -> PrivXAPIResponse:
        """
        Delete a role's principal key object.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.ROLE_STORE.PRINCIPAL_KEY,
            path_params={"role_id": role_id, "key_id": key_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user(self, user_id: str) -> PrivXAPIResponse:
        """
        Get specific user & roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.USERS, path_params={"user_id": user_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user_settings(self, user_id: str) -> PrivXAPIResponse:
        """
        Get specific user settings.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.USER_SETTINGS, path_params={"user_id": user_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def set_user_settings(self, user_id: str, settings: dict) -> PrivXAPIResponse:
        """
        Set specific user's settings.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.ROLE_STORE.USER_SETTINGS,
            path_params={"user_id": user_id},
            body=settings,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user_roles(self, user_id: str) -> PrivXAPIResponse:
        """
        Get specific user's roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.USER_ROLES, path_params={"user_id": user_id}
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def set_user_roles(self, user_id: str, roles: list) -> PrivXAPIResponse:
        """
        Set specific user's roles. These are granted in addition to mapped roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.ROLE_STORE.USER_ROLES, path_params={"user_id": user_id}, body=roles
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def enable_user_mfa(self, user_ids: list) -> PrivXAPIResponse:
        """
        Turn on multifactor authentication for an array of user IDs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.ENABLE_MFA, body=user_ids
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def disable_user_mfa(self, user_ids: list) -> PrivXAPIResponse:
        """
        Turn off multifactor authentication for an array of user IDs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.DISABLE_MFA, body=user_ids
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def reset_user_mfa(self, user_ids: list) -> PrivXAPIResponse:
        """
        Reset multifactor authentication for an array of user IDs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.RESET_MFA, body=user_ids
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def resolve_user(self, user_id: str) -> PrivXAPIResponse:
        """
        Resolve user's roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.RESOLVE_USER,
            path_params={"user_id": user_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_users(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
        search_payload: Optional[dict] = None,
    ) -> PrivXAPIResponse:

        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )

        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.SEARCH_USERS,
            query_params=search_params,
            body=search_payload,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_external_users(
        self,
        external_params: dict,
    ) -> PrivXAPIResponse:
        """
        Search users with user search parameters.
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.EXTERNAL_SEARCH,
            body=external_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user_authorized_keys(self, user_id: str) -> PrivXAPIResponse:
        """
        List user's authorized keys

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.USER_AUTHORIZED_KEYS,
            path_params={"user_id": user_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_user_authorize_key(
        self,
        user_id: str,
        key_params: dict,
    ) -> PrivXAPIResponse:
        """
        Register an authorized key for user.
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.USER_AUTHORIZED_KEYS,
            path_params={"user_id": user_id},
            body=key_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_user_authorized_key(self, user_id: str, key_id: str) -> PrivXAPIResponse:
        """
        Get user's authorized key.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.USER_AUTHORIZED_KEY_ID,
            path_params={"user_id": user_id, "key_id": key_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_user_authorized_key(
        self, user_id: str, key_id: str, key_params: dict
    ) -> PrivXAPIResponse:
        """
        Update an authorized key for user.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.ROLE_STORE.USER_AUTHORIZED_KEY_ID,
            path_params={"user_id": user_id, "key_id": key_id},
            body=key_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_user_authorized_key(self, user_id: str, key_id: str) -> PrivXAPIResponse:
        """
        Delete a user's authorized key.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.ROLE_STORE.USER_AUTHORIZED_KEY_ID,
            path_params={"user_id": user_id, "key_id": key_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_log_collectors(self) -> PrivXAPIResponse:
        """
        Get logconf collectors.

        Returns:
             PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.LOG_CONF_COLLECTORS,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def create_log_collector(self, collector: dict) -> PrivXAPIResponse:
        """
        Create logconf collector.

        Returns:
             PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.LOG_CONF_COLLECTORS,
            body=collector,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

    def get_log_collector(self, collector_id: str) -> PrivXAPIResponse:
        """
        Get logconf collector.

        Returns:
             PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.LOG_CONF_COLLECTOR,
            path_params={"collector_id": collector_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def update_log_collector(
        self, collector_id: str, collector_params: dict
    ) -> PrivXAPIResponse:
        """
        Update logconf collector.

        Returns:
             PrivXAPIResponse
        """
        response_status, data = self._http_put(
            UrlEnum.ROLE_STORE.LOG_CONF_COLLECTOR,
            path_params={"collector_id": collector_id},
            body=collector_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def delete_log_collector(self, collector_id: str) -> PrivXAPIResponse:
        """
        Delete logconf collector.

        Returns:
             PrivXAPIResponse
        """
        response_status, data = self._http_delete(
            UrlEnum.ROLE_STORE.LOG_CONF_COLLECTOR,
            path_params={"collector_id": collector_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_all_authorized_keys(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_key: Optional[str] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        List all authorized keys.

        Returns:
             PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sort_key, sortdir=sort_dir
        )
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.ALL_AUTHORIZED_KEYS,
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def resolve_authorized_keys(self, authorized_keys: dict) -> PrivXAPIResponse:
        """
        Resolve authorized keys.

        Returns:
             PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.RESOLVE_AUTHORIZED_KEYS,
            body=authorized_keys,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    #
    # List accessible AWS roles.
    #
    def list_aws_roles(self) -> PrivXAPIResponse:
        """
        Get AWS roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.ROLE_STORE.AWS_ROLES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
