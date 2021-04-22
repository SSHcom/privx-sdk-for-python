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
    STATUS = "HOST_STORE.STATUS"
    HOSTS = "HOST_STORE.HOSTS"
    HOST = "HOST_STORE.HOST"
    SEARCH = "HOST_STORE.SEARCH"
    RESOLVE = "HOST_STORE.RESOLVE"
    DEPLOY = "HOST_STORE.DEPLOY"
    DEPLOYABLE = "HOST_STORE.DEPLOYABLE"
    DISABLE = "HOST_STORE.DISABLE"
    TAGS = "HOST_STORE.TAGS"
    REALM = "HOST_STORE.REALM"
    SETTINGS = "HOST_STORE.SETTINGS"

    urls = {
        STATUS: "/host-store/api/v1/status",
        HOSTS: "/host-store/api/v1/hosts",
        HOST: "/host-store/api/v1/hosts/{host_id}",
        SEARCH: "/host-store/api/v1/hosts/search",
        RESOLVE: "/host-store/api/v1/hosts/resolve",
        DEPLOY: "/host-store/api/v1/hosts/deploy",
        DEPLOYABLE: "/host-store/api/v1/hosts/{host_id}/deployable",
        DISABLE: "/host-store/api/v1/hosts/{host_id}/disabled",
        TAGS: "/host-store/api/v1/hosts/tags",
        REALM: "/host-store/api/v1/realm/resolve",
        SETTINGS: "/host-store/api/v1/settings/default_service_options",
    }


class RoleStoreEnum:
    STATUS = "ROLE_STORE.STATUS"
    ROLES = "ROLE_STORE.ROLES"
    SOURCES = "ROLE_STORE.SOURCES"
    SOURCE = "ROLE_STORE.SOURCE"
    REFRESH_SOURCES = "ROLE_STORE.REFRESH_SOURCES"
    MEMBERS = "ROLE_STORE.MEMBERS"
    ROLE = "ROLE_STORE.ROLE"
    RESOLVE = "ROLE_STORE.RESOLVE"
    EVALUATE = "ROLE_STORE.EVALUATE"
    PRINCIPAL_KEYS = "ROLE_STORE.PRINCIPAL_KEYS"
    PRINCIPAL_KEY = "ROLE_STORE.PRINCIPAL_KEY"
    GENERATE_PRINCIPAL_KEY = "ROLE_STORE.GENERATE_PRINCIPAL_KEY"
    IMPORT_PRINCIPAL_KEY = "ROLE_STORE.IMPORT_PRINCIPAL_KEY"
    CURRENT_AWS_ROLES = "ROLE_STORE.CURRENT_AWS_ROLES"
    AWS_ROLES = "ROLE_STORE.AWS_ROLES"
    AWS_ROLE = "ROLE_STORE.AWS_ROLE"
    AWS_ROLE_PRIVX_ROLES = "ROLE_STORE.AWS_ROLE_PRIVX_ROLES"
    AWS_TOKEN = "ROLE_STORE.AWS_TOKEN"
    SEARCH_USERS = "ROLE_STORE.SEARCH_USERS"
    EXTERNAL_SEARCH = "ROLE_STORE.EXTERNAL_SEARCH"
    USERS = "ROLE_STORE.USERS"
    USER_SETTINGS = "ROLE_STORE.USER_SETTINGS"
    USER_ROLES = "ROLE_STORE.USER_ROLES"
    ENABLE_MFA = "ROLE_STORE.ENABLE_MFA"
    DISABLE_MFA = "ROLE_STORE.DISABLE_MFA"
    RESET_MFA = "ROLE_STORE.RESET_MFA"
    RESOLVE_USER = "ROLE_STORE.RESOLVE_USER"
    USER_AUTHORIZED_KEYS = "ROLE_STORE.USER_AUTHORIZED_KEYS"
    USER_AUTHORIZED_KEY_ID = "ROLE_STORE.USER_AUTHORIZED_KEY_ID"
    ALL_AUTHORIZED_KEYS = "ROLE_STORE.ALL_AUTHORIZED_KEYS"
    RESOLVE_AUTHORIZED_KEYS = "ROLE_STORE.RESOLVE_AUTHORIZED_KEYS"
    LOG_CONF_COLLECTORS = "ROLE_STORE.LOG_CONF_COLLECTORS"
    LOG_CONF_COLLECTOR = "ROLE_STORE.LOG_CONF_COLLECTOR"

    urls = {
        STATUS: "/role-store/api/v1/status",
        ROLES: "/role-store/api/v1/roles",
        SOURCES: "/role-store/api/v1/sources",
        SOURCE: "/role-store/api/v1/sources/{source_id}",
        REFRESH_SOURCES: "/role-store/api/v1/sources/refresh",
        MEMBERS: "/role-store/api/v1/roles/{role_id}/members",
        ROLE: "/role-store/api/v1/roles/{role_id}",
        RESOLVE: "/role-store/api/v1/roles/resolve",
        EVALUATE: "/role-store/api/v1/roles/evaluate",
        PRINCIPAL_KEYS: "/role-store/api/v1/roles/{role_id}/principalkeys",
        PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/{key_id}",
        GENERATE_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/generate",
        IMPORT_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/import",
        CURRENT_AWS_ROLES: "/role-store/api/v1/users/current/awsroles",
        AWS_ROLES: "/role-store/api/v1/awsroles",
        AWS_ROLE: "/role-store/api/v1/awsroles/{awsrole_id}",
        AWS_ROLE_PRIVX_ROLES: "/role-store/api/v1/awsroles/{awsrole_id}/roles",
        AWS_TOKEN: "/role-store/api/v1/roles/{awsrole_id}/awstoken",
        SEARCH_USERS: "/role-store/api/v1/users/search",
        EXTERNAL_SEARCH: "/role-store/api/v1/users/search/external",
        USERS: "/role-store/api/v1/users/{user_id}",
        USER_SETTINGS: "/role-store/api/v1/users/{user_id}/settings",
        USER_ROLES: "/role-store/api/v1/users/{user_id}/roles",
        ENABLE_MFA: "/role-store/api/v1/users/mfa/enable",
        DISABLE_MFA: "/role-store/api/v1/users/mfa/disable",
        RESET_MFA: "/role-store/api/v1/users/mfa/reset",
        RESOLVE_USER: "/role-store/api/v1/users/{user_id}/resolve",
        USER_AUTHORIZED_KEYS: "/role-store/api/v1/users/{user_id}/authorizedkeys",
        USER_AUTHORIZED_KEY_ID: "/role-store/api/v1/users/{user_id}/authorizedkeys/{key_id}",
        ALL_AUTHORIZED_KEYS: "/role-store/api/v1/authorizedkeys",
        RESOLVE_AUTHORIZED_KEYS: "/role-store/api/v1/authorizedkeys/resolve",
        LOG_CONF_COLLECTORS: "/role-store/api/v1/logconf/collectors",
        LOG_CONF_COLLECTOR: "/role-store/api/v1/logconf/collectors/{collector_id}",
    }


class UserStoreEnum:
    STATUS = "USER_STORE.STATUS"
    USERS = "USER_STORE.USERS"
    USER = "USER_STORE.USER"
    PASSWORD = "USER_STORE.PASSWORD"
    TAGS = "USER_STORE.TAGS"
    TRUSTED_CLIENTS = "USER_STORE.TRUSTED_CLIENTS"
    TRUSTED_CLIENT = "USER_STORE.TRUSTED_CLIENT"
    EXTENDER_CLIENTS = "USER_STORE.EXTENDER_CLIENTS"
    API_CLIENTS = "USER_STORE.API_CLIENTS"
    API_CLIENT = "USER_STORE.API_CLIENT"

    urls = {
        STATUS: "/local-user-store/api/v1/status",
        USERS: "/local-user-store/api/v1/users",
        USER: "/local-user-store/api/v1/users/{user_id}",
        PASSWORD: "/local-user-store/api/v1/users/{user_id}/password",
        TAGS: "/local-user-store/api/v1/users/tags",
        TRUSTED_CLIENTS: "/local-user-store/api/v1/trusted-clients",
        TRUSTED_CLIENT: "/local-user-store/api/v1/trusted-clients/{trusted_client_id}",
        EXTENDER_CLIENTS: "/local-user-store/api/v1/extender-clients",
        API_CLIENTS: "/local-user-store/api/v1/api-clients",
        API_CLIENT: "/local-user-store/api/v1/api-clients/{api_client_id}",
    }


class ConnectionManagerEnum:
    SEARCH = "CONNECTION_MANAGER.SEARCH"

    urls = {SEARCH: "/connection-manager/api/v1/connections/search"}


class VaultEnum:
    STATUS = "VAULT.STATUS"
    SECRETS = "VAULT.SECRETS"
    SECRET = "VAULT.SECRET"
    METADATA = "VAULT.METADATA"
    SEARCH = "VAULT.SEARCH"
    SCHEMAS = "VAULT.SCHEMAS"

    urls = {
        STATUS: "/vault/api/v1/status",
        SECRETS: "/vault/api/v1/secrets",
        SECRET: "/vault/api/v1/secrets/{name}",
        METADATA: "/vault/api/v1/metadata/secrets/{name}",
        SEARCH: "/vault/api/v1/search/secrets",
        SCHEMAS: "/vault/api/v1/schemas",
    }


class LicenseManagerEnum:
    STATUS = "LICENSE_MANAGER.STATUS"
    LICENSE = "LICENSE_MANAGER.LICENSE"
    REFRESH = "LICENSE_MANAGER.REFRESH"
    OPT_IN = "LICENSE_MANAGER.OPT_IN"
    DEACTIVATE = "LICENSE_MANAGER.DEACTIVATE"

    urls = {
        STATUS: "/license-manager/api/v1/status",
        LICENSE: "/license-manager/api/v1/license",
        REFRESH: "/license-manager/api/v1/license/refresh",
        OPT_IN: "/license-manager/api/v1/license/optin",
        DEACTIVATE: "/license-manager/api/v1/license/deactivate",
    }


class MonitorServiceEnum:
    STATUS = "MONITOR.STATUS"
    COMPONENTS = "MONITOR.COMPONENTS"
    COMPONENT = "MONITOR.COMPONENT"
    SEARCH_AUDIT_EVENTS = "MONITOR.SEARCH_AUDIT_EVENTS"
    AUDIT_EVENTS = "MONITOR.AUDIT_EVENTS"
    AUDIT_EVENT_CODES = "MONITOR.AUDIT_EVENT_CODES"
    INSTANCE_STATUS = "MONITOR.INSTANCE_STATUS"
    TERMINATE_INSTANCES = "MONITOR.TERMINATE_INSTANCES"

    urls = {
        STATUS: "/monitor-service/api/v1/status",
        COMPONENTS: "/monitor-service/api/v1/components",
        COMPONENT: "/monitor-service/api/v1/components/{hostname}",
        SEARCH_AUDIT_EVENTS: "/monitor-service/api/v1/auditevents/search",
        AUDIT_EVENTS: "/monitor-service/api/v1/auditevents",
        AUDIT_EVENT_CODES: "/monitor-service/api/v1/auditevents/codes",
        INSTANCE_STATUS: "/monitor-service/api/v1/instance/status",
        TERMINATE_INSTANCES: "/monitor-service/api/v1/instance/exit",
    }


class PrivXSettingsEnum:
    STATUS = "SETTINGS.STATUS"
    SCOPE = "SETTINGS.SCOPE"
    SCOPE_SECTION = "SETTINGS.SCOPE_SECTION"
    SCOPE_SCHEMA = "SETTINGS.SCOPE_SCHEMA"
    SCOPE_SECTION_SCHEMA = "SETTINGS.SCOPE_SECTION_SCHEMA"

    urls = {
        STATUS: "/settings/api/v1/status",
        SCOPE: "/settings/api/v1/settings/{scope}",
        SCOPE_SECTION: "/settings/api/v1/settings/{scope}/{section}",
        SCOPE_SCHEMA: "/settings/api/v1/schema/{scope}",
        SCOPE_SECTION_SCHEMA: "/settings/api/v1/schema/{scope}/{section}",
    }


class UrlEnum:
    AUTH = AuthEnum
    CONNECTION_MANAGER = ConnectionManagerEnum
    HOST_STORE = HostStoreEnum
    MONITOR = MonitorServiceEnum
    ROLE_STORE = RoleStoreEnum
    SETTINGS = PrivXSettingsEnum
    USER_STORE = UserStoreEnum
    VAULT = VaultEnum
    LICENSE = LicenseManagerEnum

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
