# PrivX URLs.

from typing import Union

from privx_api.exceptions import InternalAPIException


class AuthEnum:
    AUTHORIZE = "AUTH.AUTHORIZE"
    TOKEN = "AUTH.TOKEN"
    STATUS = "AUTH.STATUS"
    IDP_CLIENT = "AUTH.IDP_CLIENT"
    IDP_CLIENTS = "AUTH.IDP_CLIENTS"
    REGENERATE_IDP_CLIENT = "AUTH.REGENERATE_IDP_CLIENT"
    USER_SESSIONS = "AUTH.USER_SESSIONS"
    SOURCE_SESSIONS = "AUTH.SOURCE_SESSIONS"
    SEARCH_SESSIONS = "AUTH.SEARCH_SESSIONS"
    TERMINATE_SESSION = "AUTH.TERMINATE_SESSION"
    TERMINATE_USER_SESSIONS = "AUTH.TERMINATE_USER_SESSIONS"
    LOGOUT = "AUTH.LOGOUT"
    MGW_USER_DEVICES = "AUTH.MOBILE_GW_USER_DEVICES"
    MGW_USER_DEVICES_UNPAIR = "AUTH.MOBILE_GW_USER_DEVICES_UNPAIR"

    urls = {
        AUTHORIZE: "/auth/api/v1/oauth/authorize",
        TOKEN: "/auth/api/v1/oauth/token",
        STATUS: "/auth/api/v1/status",
        IDP_CLIENT: "/auth/api/v1/idp/clients/{idp_id}",
        IDP_CLIENTS: "/auth/api/v1/idp/clients",
        REGENERATE_IDP_CLIENT: "/auth/api/v1/idp/clients/{idp_id}/regenerate",
        USER_SESSIONS: "/auth/api/v1/sessionstorage/users/{user_id}/sessions",
        SOURCE_SESSIONS: "/auth/api/v1/sessionstorage/sources/{source_id}/sessions",
        SEARCH_SESSIONS: "/auth/api/v1/sessionstorage/sessions/search",
        TERMINATE_SESSION: "/auth/api/v1/sessionstorage/sessions/{session_id}"
        "/terminate",
        TERMINATE_USER_SESSIONS: "/auth/api/v1/sessionstorage/users/{user_id}"
        "/sessions/terminate",
        LOGOUT: "/auth/api/v1/logout",
        MGW_USER_DEVICES: "/auth/api/v1/users/{user_id}/devices",
        MGW_USER_DEVICES_UNPAIR: "/auth/api/v1/users/{user_id}/devices/{device_id}",
    }


class HostStoreEnum:
    DEPLOY = "HOST_STORE.DEPLOY"
    DEPLOYABLE = "HOST_STORE.DEPLOYABLE"
    DISABLE = "HOST_STORE.DISABLE"
    HOST = "HOST_STORE.HOST"
    HOSTS = "HOST_STORE.HOSTS"
    REALM = "HOST_STORE.REALM"
    RESOLVE = "HOST_STORE.RESOLVE"
    SEARCH = "HOST_STORE.SEARCH"
    SETTINGS = "HOST_STORE.SETTINGS"
    STATUS = "HOST_STORE.STATUS"
    TAGS = "HOST_STORE.TAGS"

    urls = {
        DEPLOY: "/host-store/api/v1/hosts/deploy",
        DEPLOYABLE: "/host-store/api/v1/hosts/{host_id}/deployable",
        DISABLE: "/host-store/api/v1/hosts/{host_id}/disabled",
        HOST: "/host-store/api/v1/hosts/{host_id}",
        HOSTS: "/host-store/api/v1/hosts",
        REALM: "/host-store/api/v1/realm/resolve",
        RESOLVE: "/host-store/api/v1/hosts/resolve",
        SEARCH: "/host-store/api/v1/hosts/search",
        SETTINGS: "/host-store/api/v1/settings/default_service_options",
        STATUS: "/host-store/api/v1/status",
        TAGS: "/host-store/api/v1/hosts/tags",
    }


class RoleStoreEnum:
    ALL_AUTHORIZED_KEYS = "ROLE_STORE.ALL_AUTHORIZED_KEYS"
    AWS_ROLE = "ROLE_STORE.AWS_ROLE"
    AWS_ROLES = "ROLE_STORE.AWS_ROLES"
    AWS_ROLE_PRIVX_ROLES = "ROLE_STORE.AWS_ROLE_PRIVX_ROLES"
    AWS_TOKEN = "ROLE_STORE.AWS_TOKEN"
    CURRENT_AWS_ROLES = "ROLE_STORE.CURRENT_AWS_ROLES"
    DISABLE_MFA = "ROLE_STORE.DISABLE_MFA"
    ENABLE_MFA = "ROLE_STORE.ENABLE_MFA"
    EVALUATE = "ROLE_STORE.EVALUATE"
    EXTERNAL_SEARCH = "ROLE_STORE.EXTERNAL_SEARCH"
    GENERATE_PRINCIPAL_KEY = "ROLE_STORE.GENERATE_PRINCIPAL_KEY"
    IDENDITY_PROVIDERS_ID = "ROLE_STORE.IDENDITY_PROVIDERS_ID"
    IMPORT_PRINCIPAL_KEY = "ROLE_STORE.IMPORT_PRINCIPAL_KEY"
    IDENDITY_PROVIDERS = "ROLE_STORE.LIST_IDENDITY_PROVIDERS"
    IDENDITY_PROVIDERS_SEARCH = "ROLE_STORE.IDENDITY_PROVIDERS_SEARCH"
    LOG_CONF_COLLECTOR = "ROLE_STORE.LOG_CONF_COLLECTOR"
    LOG_CONF_COLLECTORS = "ROLE_STORE.LOG_CONF_COLLECTORS"
    MEMBERS = "ROLE_STORE.MEMBERS"
    PRINCIPAL_KEY = "ROLE_STORE.PRINCIPAL_KEY"
    PRINCIPAL_KEYS = "ROLE_STORE.PRINCIPAL_KEYS"
    REFRESH_SOURCES = "ROLE_STORE.REFRESH_SOURCES"
    RESET_MFA = "ROLE_STORE.RESET_MFA"
    RESOLVE = "ROLE_STORE.RESOLVE"
    RESOLVE_AUTHORIZED_KEYS = "ROLE_STORE.RESOLVE_AUTHORIZED_KEYS"
    RESOLVE_USER = "ROLE_STORE.RESOLVE_USER"
    ROLE = "ROLE_STORE.ROLE"
    ROLES = "ROLE_STORE.ROLES"
    SEARCH_USERS = "ROLE_STORE.SEARCH_USERS"
    SEARCH_ROLES = "ROLE_STORE.SEARCH_ROLES"
    SOURCE = "ROLE_STORE.SOURCE"
    SOURCES = "ROLE_STORE.SOURCES"
    STATUS = "ROLE_STORE.STATUS"
    USERS = "ROLE_STORE.USERS"
    USER_AUTHORIZED_KEYS = "ROLE_STORE.USER_AUTHORIZED_KEYS"
    USER_AUTHORIZED_KEY_ID = "ROLE_STORE.USER_AUTHORIZED_KEY_ID"
    USER_ROLES = "ROLE_STORE.USER_ROLES"
    USER_SETTINGS = "ROLE_STORE.USER_SETTINGS"

    urls = {
        ALL_AUTHORIZED_KEYS: "/role-store/api/v1/authorizedkeys",
        AWS_ROLE: "/role-store/api/v1/awsroles/{awsrole_id}",
        AWS_ROLES: "/role-store/api/v1/awsroles",
        AWS_ROLE_PRIVX_ROLES: "/role-store/api/v1/awsroles/{awsrole_id}/roles",
        AWS_TOKEN: "/role-store/api/v1/roles/{awsrole_id}/awstoken",
        CURRENT_AWS_ROLES: "/role-store/api/v1/users/current/awsroles",
        DISABLE_MFA: "/role-store/api/v1/users/mfa/disable",
        ENABLE_MFA: "/role-store/api/v1/users/mfa/enable",
        EVALUATE: "/role-store/api/v1/roles/evaluate",
        EXTERNAL_SEARCH: "/role-store/api/v1/users/search/external",
        GENERATE_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys"
        "/generate",
        IDENDITY_PROVIDERS_ID: "/role-store/api/v1/identity-providers/{id}",
        IDENDITY_PROVIDERS_SEARCH: "/role-store/api/v1/identity-providers/search",
        IMPORT_PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/import",
        IDENDITY_PROVIDERS: "/role-store/api/v1/identity-providers",
        LOG_CONF_COLLECTOR: "/role-store/api/v1/logconf/collectors/{collector_id}",
        LOG_CONF_COLLECTORS: "/role-store/api/v1/logconf/collectors",
        MEMBERS: "/role-store/api/v1/roles/{role_id}/members",
        PRINCIPAL_KEY: "/role-store/api/v1/roles/{role_id}/principalkeys/{key_id}",
        PRINCIPAL_KEYS: "/role-store/api/v1/roles/{role_id}/principalkeys",
        REFRESH_SOURCES: "/role-store/api/v1/sources/refresh",
        RESET_MFA: "/role-store/api/v1/users/mfa/reset",
        RESOLVE: "/role-store/api/v1/roles/resolve",
        RESOLVE_AUTHORIZED_KEYS: "/role-store/api/v1/authorizedkeys/resolve",
        RESOLVE_USER: "/role-store/api/v1/users/{user_id}/resolve",
        ROLE: "/role-store/api/v1/roles/{role_id}",
        ROLES: "/role-store/api/v1/roles",
        SEARCH_USERS: "/role-store/api/v1/users/search",
        SEARCH_ROLES: "/role-store/api/v1/roles/search",
        SOURCE: "/role-store/api/v1/sources/{source_id}",
        SOURCES: "/role-store/api/v1/sources",
        STATUS: "/role-store/api/v1/status",
        USERS: "/role-store/api/v1/users/{user_id}",
        USER_AUTHORIZED_KEYS: "/role-store/api/v1/users/{user_id}/authorizedkeys",
        USER_AUTHORIZED_KEY_ID: "/role-store/api/v1/users/{user_id}/authorizedkeys"
        "/{key_id}",
        USER_ROLES: "/role-store/api/v1/users/{user_id}/roles",
        USER_SETTINGS: "/role-store/api/v1/users/{user_id}/settings",
    }


class UserStoreEnum:
    API_CLIENT = "USER_STORE.API_CLIENT"
    API_CLIENTS = "USER_STORE.API_CLIENTS"
    EXTENDING_CLIENTS = "USER_STORE.EXTENDING_CLIENTS"
    STATUS = "USER_STORE.STATUS"
    TRUSTED_CLIENT = "USER_STORE.TRUSTED_CLIENT"
    TRUSTED_CLIENTS = "USER_STORE.TRUSTED_CLIENTS"
    USER = "USER_STORE.USER"
    USERS = "USER_STORE.USERS"
    USER_PASSWORD = "USER_STORE.USER_PASSWORD"
    USER_TAGS = "USER_STORE.USER_TAGS"

    urls = {
        API_CLIENT: "/local-user-store/api/v1/api-clients/{api_client_id}",
        API_CLIENTS: "/local-user-store/api/v1/api-clients",
        EXTENDING_CLIENTS: "/local-user-store/api/v1/extender-clients",
        STATUS: "/local-user-store/api/v1/status",
        TRUSTED_CLIENT: "/local-user-store/api/v1/trusted-clients/{trusted_client_id}",
        TRUSTED_CLIENTS: "/local-user-store/api/v1/trusted-clients",
        USER: "/local-user-store/api/v1/users/{user_id}",
        USERS: "/local-user-store/api/v1/users",
        USER_PASSWORD: "/local-user-store/api/v1/users/{user_id}/password",
        USER_TAGS: "/local-user-store/api/v1/users/tags",
    }


class ConnectionManagerEnum:
    ACCESS_ROLE = "CONNECTION_MANAGER.ACCESS_ROLE"
    CONNECTION = "CONNECTION_MANAGER.CONNECTION"
    CONNECTIONS = "CONNECTION_MANAGER.CONNECTIONS"
    CONNECTION_ACCESS_ROLE = "CONNECTION_MANAGER.CONNECTION_ACCESS_ROLE"
    CONNECTION_ACCESS_ROLES = "CONNECTION_MANAGER.CONNECTION_ACCESS_ROLES"
    SEARCH = "CONNECTION_MANAGER.SEARCH"
    STATUS = "CONNECTION_MANAGER.STATUS"
    TERMINATE_CONNECTION_ID = "CONNECTION_MANAGER.TERMINATE_CONNECTION_ID"
    TERMINATE_HOST_ID = "CONNECTION_MANAGER.TERMINATE_HOST_ID"
    TERMINATE_USER_ID = "CONNECTION_MANAGER.TERMINATE_USER_ID"
    TRAIL = "CONNECTION_MANAGER.TRAIL"
    TRAIL_LOG = "CONNECTION_MANAGER.TRAIL_LOG"
    TRAIL_LOG_SESSION_ID = "CONNECTION_MANAGER.TRAIL_LOG_SESSION_ID"
    TRAIL_SESSION_ID = "CONNECTION_MANAGER.TRAIL_SESSION_ID"
    UEBA_CONFIGURATIONS = "CONNECTION_MANAGER.UEBA_CONFIGURATIONS"
    UEBA_ANOMALY_SETTINGS = "CONNECTION_MANAGER.UEBA_ANOMALY_SETTINGS"
    START_ANALYSIS = "CONNECTION_MANAGER.START_ANALYSIS"
    STOP_ANALYSIS = "CONNECTION_MANAGER.STOP_ANALYSIS"
    UEBA_SETUP_SCRIPT = "CONNECTION_MANAGER.UEBA_SETUP_SCRIPT"
    DOWNLOAD_SCRIPT = "CONNECTION_MANAGER.DOWNLOAD_SCRIPT"
    UEBA_DATASETS = "CONNECTION_MANAGER.UEBA_DATASETS"
    UEBA_DATASET = "CONNECTION_MANAGER.UEBA_DATASET"
    UEBA_TRAIN_DATASET = "CONNECTION_MANAGER.UEBA_TRAIN_DATASET"
    UEBA_CONNECTION_COUNT = "CONNECTION_MANAGER.UEBA_CONNECTION_COUNT"
    UEBA_INTERNAL_STATUS = "CONNECTION_MANAGER.UEBA_INTERNAL_STATUS"
    UEBA_STATUS = "CONNECTION_MANAGER.UEBA_STATUS"
    CONNECTION_TAGS = "CONNECTION_MANAGER.CONNECTION_TAGS"
    UPDATE_CONNECTION_TAGS = "CONNECTION_MANAGER.UPDATE_CONNECTION_TAGS"

    urls = {
        ACCESS_ROLE: "/connection-manager/api/v1/connections/access_roles/{role_id}",
        CONNECTION: "/connection-manager/api/v1/connections/{connection_id}",
        CONNECTIONS: "/connection-manager/api/v1/connections",
        CONNECTION_ACCESS_ROLE: "/connection-manager/api/v1/connections/{connection_id}"
        "/access_roles/{role_id}",
        CONNECTION_ACCESS_ROLES: "/connection-manager/api/v1/connections"
        "/{connection_id}"
        "/access_roles",
        SEARCH: "/connection-manager/api/v1/connections/search",
        STATUS: "/connection-manager/api/v1/status",
        TERMINATE_CONNECTION_ID: "/connection-manager/api/v1/terminate/connection"
        "/{connection_id}",
        TERMINATE_HOST_ID: "/connection-manager/api/v1/terminate/host/{host_id}",
        TERMINATE_USER_ID: "/connection-manager/api/v1/terminate/user/{user_id}",
        TRAIL: "/connection-manager/api/v1/connections/{connection_id}"
        "/channel/{channel_id}/file/{file_id}/{session_id}",
        TRAIL_LOG: "/connection-manager/api/v1/connections/{connection_id}"
        "/channel/{channel_id}/log",
        TRAIL_LOG_SESSION_ID: "/connection-manager/api/v1/connections/{connection_id}"
        "/channel/{channel_id}/log/{session_id}",
        TRAIL_SESSION_ID: "/connection-manager/api/v1/connections/{connection_id}"
        "/channel/{channel_id}/file/{file_id}",
        UEBA_CONFIGURATIONS: "/connection-manager/api/v1/ueba/configure",
        UEBA_ANOMALY_SETTINGS: "/connection-manager/api/v1/ueba/anomaly-settings",
        START_ANALYSIS: "/connection-manager/api/v1/ueba/start-analyzing/{dataset_id}",
        STOP_ANALYSIS: "/connection-manager/api/v1/ueba/stop-analyzing",
        UEBA_SETUP_SCRIPT: "/connection-manager/api/v1/ueba/setup-script",
        DOWNLOAD_SCRIPT: "/connection-manager/api/v1/ueba/setup-script/{session_id}",
        UEBA_DATASETS: "/connection-manager/api/v1/ueba/datasets",
        UEBA_DATASET: "/connection-manager/api/v1/ueba/datasets/{dataset_id}",
        UEBA_TRAIN_DATASET: "/connection-manager/api/v1/ueba/train/{dataset_id}",
        UEBA_CONNECTION_COUNT: "/connection-manager/api/v1/ueba/query-connection-count",
        UEBA_STATUS: "/connection-manager/api/v1/ueba/status",
        UEBA_INTERNAL_STATUS: "/connection-manager/api/v1/ueba/status/internal",
        CONNECTION_TAGS: "/connection-manager/api/v1/connections/tags",
        UPDATE_CONNECTION_TAGS: "/connection-manager/api/v1/connections/"
        "{connection_id}/tags",
    }


class DbProxyEnum:
    STATUS = "DB_PROXY.STATUS"
    CONF = "DB_PROXY.CONF"

    urls = {STATUS: "/db-proxy/api/v1/status", CONF: "/db-proxy/api/v1/conf"}


class VaultEnum:
    METADATA = "VAULT.METADATA"
    SCHEMAS = "VAULT.SCHEMAS"
    SEARCH = "VAULT.SEARCH"
    SECRET = "VAULT.SECRET"
    SECRETS = "VAULT.SECRETS"
    STATUS = "VAULT.STATUS"
    USER_SECRETS = "VAULT.USER_SECRETS"
    USER_SECRET = "VAULT.USER_SECRET"
    USER_SECRET_METADATA = "VAULT.USER_SECRET_METADATA"

    urls = {
        METADATA: "/vault/api/v1/metadata/secrets/{name}",
        SCHEMAS: "/vault/api/v1/schemas",
        SEARCH: "/vault/api/v1/search/secrets",
        SECRET: "/vault/api/v1/secrets/{name}",
        SECRETS: "/vault/api/v1/secrets",
        STATUS: "/vault/api/v1/status",
        USER_SECRETS: "/vault/api/v1/user/{user_id}/secrets",
        USER_SECRET: "/vault/api/v1/user/{user_id}/secrets/{name}",
        USER_SECRET_METADATA: "/vault/api/v1/user/{user_id}/metadata/secrets/{name}",
    }


class LicenseManagerEnum:
    STATUS = "LICENSE_MANAGER.STATUS"
    LICENSE = "LICENSE_MANAGER.LICENSE"
    REFRESH = "LICENSE_MANAGER.REFRESH"
    OPT_IN = "LICENSE_MANAGER.OPT_IN"
    DEACTIVATE = "LICENSE_MANAGER.DEACTIVATE"
    MGW_STATUS = "MOBILE_GW.STATUS"
    MGW_REGISTER = "MOBILE_GW.REGISTER"
    MGW_UNREGISTER = "MOBILE_GW.UNREGISTER"

    urls = {
        STATUS: "/license-manager/api/v1/status",
        LICENSE: "/license-manager/api/v1/license",
        REFRESH: "/license-manager/api/v1/license/refresh",
        OPT_IN: "/license-manager/api/v1/license/optin",
        DEACTIVATE: "/license-manager/api/v1/license/deactivate",
        MGW_STATUS: "/license-manager/api/v1/mobilegw/status",
        MGW_REGISTER: "/license-manager/api/v1/mobilegw/register",
        MGW_UNREGISTER: "/license-manager/api/v1/mobilegw/unregister",
    }


class MonitorServiceEnum:
    AUDIT_EVENTS = "MONITOR.AUDIT_EVENTS"
    AUDIT_EVENT_CODES = "MONITOR.AUDIT_EVENT_CODES"
    COMPONENT = "MONITOR.COMPONENT"
    COMPONENTS = "MONITOR.COMPONENTS"
    INSTANCE_STATUS = "MONITOR.INSTANCE_STATUS"
    SEARCH_AUDIT_EVENTS = "MONITOR.SEARCH_AUDIT_EVENTS"
    STATUS = "MONITOR.STATUS"
    TERMINATE_INSTANCES = "MONITOR.TERMINATE_INSTANCES"

    urls = {
        AUDIT_EVENTS: "/monitor-service/api/v1/auditevents",
        AUDIT_EVENT_CODES: "/monitor-service/api/v1/auditevents/codes",
        COMPONENT: "/monitor-service/api/v1/components/{hostname}",
        COMPONENTS: "/monitor-service/api/v1/components",
        INSTANCE_STATUS: "/monitor-service/api/v1/instance/status",
        SEARCH_AUDIT_EVENTS: "/monitor-service/api/v1/auditevents/search",
        STATUS: "/monitor-service/api/v1/status",
        TERMINATE_INSTANCES: "/monitor-service/api/v1/instance/exit",
    }


class PrivXSettingsEnum:
    SCOPE = "SETTINGS.SCOPE"
    SCOPE_SCHEMA = "SETTINGS.SCOPE_SCHEMA"
    SCOPE_SECTION = "SETTINGS.SCOPE_SECTION"
    SCOPE_SECTION_SCHEMA = "SETTINGS.SCOPE_SECTION_SCHEMA"
    STATUS = "SETTINGS.STATUS"

    urls = {
        SCOPE: "/settings/api/v1/settings/{scope}",
        SCOPE_SCHEMA: "/settings/api/v1/schema/{scope}",
        SCOPE_SECTION: "/settings/api/v1/settings/{scope}/{section}",
        SCOPE_SECTION_SCHEMA: "/settings/api/v1/schema/{scope}/{section}",
        STATUS: "/settings/api/v1/status",
    }


class WokFlowEngineEnum:
    DECISION = "WORKFLOW_ENGINE.DECISION"
    REQUEST = "WORKFLOW_ENGINE.REQUEST"
    REQUESTS = "WORKFLOW_ENGINE.REQUESTS"
    SEARCH_REQUESTS = "WORKFLOW_ENGINE.SEARCH_REQUESTS"
    SETTINGS = "WORKFLOW_ENGINE.SETTINGS"
    STATUS = "WORKFLOW_ENGINE.STATUS"
    TEST_SETTINGS = "WORKFLOW_ENGINE.TEST_SETTINGS"
    WORKFLOW = "WORKFLOW_ENGINE.WORKFLOW"
    WORKFLOWS = "WORKFLOW_ENGINE.WORKFLOWS"
    ROLE_REVOKE = "WORKFLOW_ENGINE.REQUEST_ROLE_REVOKE"

    urls = {
        DECISION: "/workflow-engine/api/v1/requests/{request_id}/decision",
        REQUEST: "/workflow-engine/api/v1/requests/{request_id}",
        REQUESTS: "/workflow-engine/api/v1/requests",
        SEARCH_REQUESTS: "/workflow-engine/api/v1/requests/search",
        SETTINGS: "/workflow-engine/api/v1/settings",
        STATUS: "/workflow-engine/api/v1/status",
        TEST_SETTINGS: "/workflow-engine/api/v1/testsmtp",
        WORKFLOW: "/workflow-engine/api/v1/workflows/{workflow_id}",
        WORKFLOWS: "/workflow-engine/api/v1/workflows",
        ROLE_REVOKE: "/workflow-engine/api/v1/requests/{request_id}/role/revoke",
    }


class TrailIndexEnum:
    CONNECTION_INDEXING_STATUS = "TRAIL_INDEX.CONNECTION_INDEXING_STATUS"
    CONNECTIONS_INDEXING_STATUSES = "TRAIL_INDEX.CONNECTIONS_INDEXING_STATUSES"
    SEARCH = "TRAIL_INDEX.SEARCH"
    START_INDEXING = "TRAIL_INDEX.START_INDEXING"
    STATUS = "TRAIL_INDEX.STATUS"

    urls = {
        CONNECTION_INDEXING_STATUS: "/trail-index/api/v1/index/{connection_id}/status",
        CONNECTIONS_INDEXING_STATUSES: "/trail-index/api/v1/index/status",
        SEARCH: "/trail-index/api/v1/index/search",
        START_INDEXING: "/trail-index/api/v1/index/start",
        STATUS: "/trail-index/api/v1/status",
    }


class AuthorizerEnum:
    ACCESS_GROUP = "AUTHORIZER.ACCESS_GROUP"
    ACCESS_GROUPS = "AUTHORIZER.ACCESS_GROUPS"
    CREATE_ACCESS_GROUP_CA_KEY = "AUTHORIZER.CREATE_ACCESS_GROUP_CA_KEY"
    DELETE_ACCESS_GROUP_CA_KEY = "AUTHORIZER.DELETE_ACCESS_GROUP_CA_KEY"
    AUTHORIZER_CERT = "AUTHORIZER.AUTHORIZER_CERT"
    AUTHORIZER_CERT_ID = "AUTHORIZER.AUTHORIZER_CERT_ID"
    CARRIER_CONFIG_SESSION_ID = "AUTHORIZER.CARRIER_CONFIG_SESSION_ID"
    CERT_AUTH_TEMPLATES = "AUTHORIZER.CERT_AUTH_TEMPLATES"
    CERT_REVOCATION_LIST = "AUTHORIZER.CERT_REVOCATION_LIST"
    COMPONENT_CERT = "AUTHORIZER.COMPONENT_CERT"
    COMPONENT_CERTS = "AUTHORIZER.COMPONENT_CERTS"
    COMPONENT_CERT_REVOCATION_LIST = "AUTHORIZER.COMPONENT_CERT_REVOCATION_LIST"
    CREATE_GROUP_PRINCIPAL_KEY = "AUTHORIZER.CREATE_GROUP_PRINCIPAL_KEY"
    DEPLOYMENT_SCRIPT_SESSION_ID = "AUTHORIZER.DEPLOYMENT_SCRIPT_SESSION_ID"
    DOWNLOAD_CARRIER_CONFIG = "AUTHORIZER.DOWNLOAD_CARRIER_CONFIG"
    DOWNLOAD_COMMAND_SCRIPT = "AUTHORIZER.DOWNLOAD_COMMAND_SCRIPT"
    DOWNLOAD_DEPLOYMENT_SCRIPT = "AUTHORIZER.DOWNLOAD_DEPLOYMENT_SCRIPT"
    DOWNLOAD_WEB_PROXY_CONFIG = "AUTHORIZER.DOWNLOAD_WEB_PROXY_CONFIG"
    EXTENDER_CONFIG = "AUTHORIZER.EXTENDER_CONFIG"
    EXTENDER_CONFIG_SESSION_ID = "AUTHORIZER.EXTENDER_CONFIG_SESSION_ID"
    EXTENDER_TRUST_ANCHOR = "AUTHORIZER.EXTENDER_TRUST_ANCHOR"
    GET_CERT_BY_ID = "AUTHORIZER.GET_CERT_BY_ID"
    GET_CERTIFICATES_LIST = "AUTHORIZER.GET_CERTIFICATES_LIST"
    GROUP_PRINCIPAL_KEY = "AUTHORIZER.GROUP_PRINCIPAL_KEY"
    IMPORT_GROUP_PRINCIPAL_KEY = "AUTHORIZER.IMPORT_GROUP_PRINCIPAL_KEY"
    PRINCIPALS = "AUTHORIZER.PRINCIPALS"
    SEARCH_ACCESS_GROUPS = "AUTHORIZER.SEARCH_ACCESS_GROUPS"
    SEARCH_CERTS = "AUTHORIZER.SEARCH_CERTS"
    SIGN_GROUP_PRINCIPAL_KEY = "AUTHORIZER.SIGN_GROUP_PRINCIPAL_KEY"
    SSL_TRUST_ANCHOR = "AUTHORIZER.SSL_TRUST_ANCHOR"
    STATUS = "AUTHORIZER.STATUS"
    TARGET_HOST = "AUTHORIZER.TARGET_HOST"
    WEB_PROXY_CONFIG_SESSION_ID = "AUTHORIZER.WEB_PROXY_CONFIG_SESSION_ID"

    urls = {
        ACCESS_GROUP: "/authorizer/api/v1/accessgroups/{id}",
        ACCESS_GROUPS: "/authorizer/api/v1/accessgroups",
        CREATE_ACCESS_GROUP_CA_KEY: "/authorizer/api/v1/accessgroups/{id}/cas",
        DELETE_ACCESS_GROUP_CA_KEY: "/authorizer/api/v1/accessgroups/{id}/cas/{ca_id}",
        AUTHORIZER_CERT: "/authorizer/api/v1/cas",
        AUTHORIZER_CERT_ID: "/authorizer/api/v1/cas/{id}",
        CARRIER_CONFIG_SESSION_ID: "/authorizer/api/v1/carrier/conf"
        "/{trusted_client_id}",
        CERT_AUTH_TEMPLATES: "/authorizer/api/v1/cert/templates",
        CERT_REVOCATION_LIST: "/authorizer/api/v1/cas/{id}/crl",
        COMPONENT_CERT: "/authorizer/api/v1/{ca_type}/cas/{id}",
        COMPONENT_CERTS: "/authorizer/api/v1/{ca_type}/cas",
        COMPONENT_CERT_REVOCATION_LIST: "/authorizer/api/v1/{ca_type}/cas/{id}/crl",
        CREATE_GROUP_PRINCIPAL_KEY: "/authorizer/api/v1/principals/{group_id}/create",
        DEPLOYMENT_SCRIPT_SESSION_ID: "/authorizer/api/v1/deploy/{trusted_client_id}",
        DOWNLOAD_CARRIER_CONFIG: "/authorizer/api/v1/carrier/conf/{trusted_client_id}"
        "/{session_id}",
        DOWNLOAD_COMMAND_SCRIPT: "/authorizer/api/v1/deploy/principals_command.sh",
        DOWNLOAD_DEPLOYMENT_SCRIPT: "/authorizer/api/v1/deploy/{trusted_client_id}/{"
        "session_id}",
        DOWNLOAD_WEB_PROXY_CONFIG: "/authorizer/api/v1/icap/conf/{trusted_client_id}"
        "/{session_id}",
        EXTENDER_CONFIG: "/authorizer/api/v1/extender/conf/{trusted_client_id}"
        "/{session_id}",
        EXTENDER_CONFIG_SESSION_ID: "/authorizer/api/v1/extender/conf"
        "/{trusted_client_id}",
        EXTENDER_TRUST_ANCHOR: "/authorizer/api/v1/extender-trust-anchor",
        GET_CERT_BY_ID: "/authorizer/api/v1/cert/{id}",
        GET_CERTIFICATES_LIST: "/authorizer/api/v1/cert",
        GROUP_PRINCIPAL_KEY: "/authorizer/api/v1/principals/{group_id}",
        IMPORT_GROUP_PRINCIPAL_KEY: "/authorizer/api/v1/principals/{group_id}/import",
        PRINCIPALS: "/authorizer/api/v1/principals",
        SEARCH_ACCESS_GROUPS: "/authorizer/api/v1/accessgroups/search",
        SEARCH_CERTS: "/authorizer/api/v1/cert/search",
        SIGN_GROUP_PRINCIPAL_KEY: "/authorizer/api/v1/principals/{group_id}/sign",
        SSL_TRUST_ANCHOR: "/authorizer/api/v1/ssl-trust-anchor",
        STATUS: "/authorizer/api/v1/status",
        TARGET_HOST: "/authorizer/api/v1/ca/authorize",
        WEB_PROXY_CONFIG_SESSION_ID: "/authorizer/api/v1/icap/conf/{trusted_client_id}",
    }


class NetworkAccessManager:
    STATUS = "NETWORK_MANAGER.STATUS"
    SESSION = "NETWORK_MANAGER.SESSION"
    NETWORK_TARGETS = "NETWORK_MANAGER.NETWORK_TARGETS"
    NETWORK_TARGET = "NETWORK_MANAGER.NETWORK_TARGET"
    DISABLE_NETWORK_TARGET = "NETWORK_MANAGER.DISABLE_NETWORK_TARGET"
    SEARCH_NETWORK_TARGETS = "NETWORK_MANAGER.SEARCH_NETWORK_TARGETS"

    urls = {
        STATUS: "/network-access-manager/api/v1/status",
        SESSION: "/network-access-manager/api/v1/ws/session",
        NETWORK_TARGETS: "/network-access-manager/api/v1/nwtargets",
        NETWORK_TARGET: "/network-access-manager/api/v1/nwtargets/{network_target_id}",
        DISABLE_NETWORK_TARGET: "/network-access-manager/api/v1/nwtargets/"
        "{network_target_id}/disabled",
        SEARCH_NETWORK_TARGETS: "/network-access-manager/api/v1/nwtargets/search",
    }


class UrlEnum:
    AUTH = AuthEnum
    AUTHORIZER = AuthorizerEnum
    CONNECTION_MANAGER = ConnectionManagerEnum
    DB_PROXY = DbProxyEnum
    HOST_STORE = HostStoreEnum
    LICENSE = LicenseManagerEnum
    MONITOR = MonitorServiceEnum
    NETWORK_ACCESS_MANAGER = NetworkAccessManager
    ROLE_STORE = RoleStoreEnum
    SETTINGS = PrivXSettingsEnum
    TRAIL_INDEX = TrailIndexEnum
    USER_STORE = UserStoreEnum
    VAULT = VaultEnum
    WORKFLOW_ENGINE = WokFlowEngineEnum

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


# Set of PrivX STATUS endpoints names, which could be used without authentication
NO_AUTH_STATUS_URLS = {
    v.__dict__.get("STATUS") for k, v in UrlEnum.__dict__.items() if not k.islower()
}
