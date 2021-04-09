# PrivX URLs.

from typing import Union

from privx_api.exceptions import InternalAPIException


class AuthEnum:
    AUTHORIZE = "AUTH.AUTHORIZE"
    TOKEN = "AUTH.TOKEN"

    urls = {
        AUTHORIZE: "/auth/api/v1/oauth/authorize",
        TOKEN: "/auth/api/v1/oauth/token",
    }


class HostStoreEnum:
    HOSTS = "HOST_STORE.HOSTS"
    HOST = "HOST_STORE.HOST"
    SEARCH = "HOST_STORE.SEARCH"

    urls = {
        HOSTS: "/host-store/api/v1/hosts",
        HOST: "/host-store/api/v1/hosts/{host_id}",
        SEARCH: "/host-store/api/v1/hosts/search",
    }


class RoleStoreEnum:
    ROLES = "ROLE_STORE.ROLES"
    SOURCES = "ROLE_STORE.SOURCES"
    MEMBERS = "ROLE_STORE.MEMBERS"
    ROLE = "ROLE_STORE.ROLE"
    RESOLVE = "ROLE_STORE.RESOLVE"
    EVALUATE = "ROLE_STORE.EVALUATE"
    PRINCIPAL_KEYS = "ROLE_STORE.PRINCIPAL_KEYS"
    PRINCIPAL_KEY = "ROLE_STORE.PRINCIPAL_KEY"
    GENERATE_PRINCIPAL_KEY = "ROLE_STORE.GENERATE_PRINCIPAL_KEY"
    IMPORT_PRINCIPAL_KEY = "ROLE_STORE.IMPORT_PRINCIPAL_KEY"
    AWS_ROLES = "ROLE_STORE.AWS_ROLES"
    AWS_TOKEN = "ROLE_STORE.AWS_TOKEN"
    SEARCH_USERS = "ROLE_STORE.SEARCH_USERS"

    urls = {
        ROLES: "/role-store/api/v1/roles",
        SOURCES: "/role-store/api/v1/sources",
        MEMBERS: "/role-store/api/v1/roles/{role_id}/members",
        ROLE: "/role-store/api/v1/roles/{role_id}",
        RESOLVE: "/role-store/api/v1/roles/resolve",
        EVALUATE: "/role-store/api/v1/roles/evaluate",
        PRINCIPAL_KEYS: "/role-store/api/v1/roles/{role_id}/principalkeys",
        PRINCIPAL_KEY: ("/role-store/api/v1/roles/{role_id}/principalkeys/{key_id}"),
        GENERATE_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/generate",
        IMPORT_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/import",
        AWS_ROLES: "/role-store/api/v1/users/current/awsroles",
        AWS_TOKEN: "/role-store/api/v1/roles/{awsrole_id}/awstoken",
        SEARCH_USERS: "/role-store/api/v1/users/search",
    }


class UserStoreEnum:
    STATUS = "USER_STORE.STATUS"
    USERS = "USER_STORE.USERS"
    USER = "USER_STORE.USER"

    urls = {
        STATUS: "/local-user-store/api/v1/status",
        USERS: "/local-user-store/api/v1/users",
        USER: "/local-user-store/api/v1/users/{user_id}",
    }


class ConnectionManagerEnum:
    SEARCH = "CONNECTION_MANAGER.SEARCH"

    urls = {SEARCH: "/connection-manager/api/v1/connections/search"}


class VaultEnum:
    SECRET = "VAULT.SECRET"

    urls = {SECRET: "/vault/api/v1/secrets/{name}"}


class UrlEnum:
    AUTH = AuthEnum
    CONNECTION_MANAGER = ConnectionManagerEnum
    HOST_STORE = HostStoreEnum
    ROLE_STORE = RoleStoreEnum
    USER_STORE = UserStoreEnum
    VAULT = VaultEnum

    @classmethod
    def get(cls, url_name: str) -> Union[str, None]:
        """
        looking for required url name among inner enums
        Args:
            url_name: str e.g. 'TOKEN'
        Returns:
            str e.g.'/auth/api/v1/oauth/token'
            None if url name not found
        """

        list_urls = list(
            filter(
                lambda inner_enum: inner_enum.urls.get(url_name),
                (
                    val
                    for key, val in cls.__dict__.items()
                    if key == key.upper() and not key.startswith("__")
                ),
            )
        )
        if len(list_urls) != 1:
            raise InternalAPIException
        return list_urls[0].urls.get(url_name)
