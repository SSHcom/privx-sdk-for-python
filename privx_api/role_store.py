from http import HTTPStatus

from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse
from privx_api.base import BasePrivXAPI


class RoleStoreAPI(BasePrivXAPI):
    """
    Role store API.
    """

    def create_role(self, role: dict) -> PrivXAPIResponse:
        """
        Create a role, see required fields from API docs.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(UrlEnum.ROLE_STORE.ROLES, body=role)
        return PrivXAPIResponse(response_status, HTTPStatus.CREATED, data)

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

    def get_roles(self) -> PrivXAPIResponse:
        """
        Get roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.ROLE_STORE.ROLES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_role_by_id(self, role_id: str) -> PrivXAPIResponse:
        """
        Get role object by ID.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.ROLE, path_params={"role_id": role_id}
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

    def get_role_members(
        self,
        role_id: str,
        offset: int = None,
        limit: int = None,
        sortkey: str = None,
        sortdir: str = None,
    ) -> PrivXAPIResponse:
        """
        Get Role Members.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sortkey, sortdir=sortdir
        )
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.MEMBERS,
            path_params={"role_id": role_id},
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

    def search_users(
        self,
        offset: int = None,
        limit: int = None,
        sortkey: str = None,
        sortdir: str = None,
        **kw
    ) -> PrivXAPIResponse:

        search_params = self._get_search_params(
            offset=offset, limit=limit, sortkey=sortkey, sortdir=sortdir
        )

        response_status, data = self._http_post(
            UrlEnum.ROLE_STORE.SEARCH_USERS, query_params=search_params, body=kw
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

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

    #
    # List accessible AWS roles.
    #

    def list_awsroles(self) -> PrivXAPIResponse:
        """
        Get AWS roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.ROLE_STORE.AWS_ROLES)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    # Fetch temporary AWS token for given AWS role name and TTL.
    # User needs to have the requested AWS role mapped to the available PrivX role by PrivX admin.
    # Allowed TTL values 900-3600 seconds for assume-role (configurable max 43200) and 900-129600
    # for federation token.

    def get_awstoken(
        self, awsrole_id: str, ttl: int = 900, tokencode: str = None
    ) -> PrivXAPIResponse:
        """
        Get temporary AWS token for given AWS role.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(ttl=ttl, tokencode=tokencode)
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.AWS_TOKEN,
            path_params={"awsrole_id": awsrole_id},
            query_params=search_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_user_by_id(self, user_id: str) -> PrivXAPIResponse:
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
        Get specific user's roles.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.ROLE_STORE.RESOLVE_USER,
            path_params={"user_id": user_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_users_by_external_params(
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
