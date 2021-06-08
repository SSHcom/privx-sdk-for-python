# An example how to use PrivX API for granting roles to users.
# Can be used as basis for automating temporary role grants via ServiceNow or
# similar services.
# Requires Python 3.6+

import datetime
import sys

import config

# this importation for demonstration purpose only
# for proper importation of privx_api module
# see https://github.com/SSHcom/privx-sdk-for-python#getting-started
try:
    # Running example with pip-installed SDK
    import privx_api
except ImportError:
    # Running example without installing SDK
    from utils import load_privx_api_lib_path

    load_privx_api_lib_path()
    import privx_api

# Initialize the API.
api = privx_api.PrivXAPI(
    config.HOSTNAME,
    config.HOSTPORT,
    config.CA_CERT,
    config.OAUTH_CLIENT_ID,
    config.OAUTH_CLIENT_SECRET,
)

# Authenticate.
api.authenticate(config.API_CLIENT_ID, config.API_CLIENT_SECRET)


# Target-user name
EMAIL = "alice@example.com"

# Name of the role to grant to the target user
ROLE = "Example Role"

# Specify the validity of the grant as one of the following:
# * PERMANENT: The grant never expires.
# * FLOATING: Validity starts running after user permissions are checked.
# * TIME_RESTRICTED: Specify timestamps for grant start and end.
GRANT_TYPE = "FLOATING"

# Validity of the grant in hours (for time-restricted grants only)
VALIDITY = 1


def get_user_ID(email: str) -> str:
    """
    Return the ID of the user with the given email.

    :param email: Email address of the user.
    :return: Matching user's ID. None if the user cannot be found.
    """
    response = api.search_users(search_payload={"keywords": EMAIL})

    if not response.ok:
        print(response.data)
        sys.exit(1)

    for item in response.data.get("items"):
        if item.get("email") == EMAIL:
            return item.get("id")
    else:
        return None


def get_user_roles(user_id: str) -> list:
    """
    Return the current roles of the target user.

    :param user_id: ID of the target user.
    :return: List of target-user's roles.
    """
    response = api.get_user_roles(user_id)

    if not response.ok:
        print(response.data)
        sys.exit(1)

    return response.data.get("items")


def get_role_ID(name: str) -> str:
    """
    Return the ID of the named role.

    :param name: Name of the role.
    :return: Matching role's ID. None if the role cannot be found.
    """
    response = api.get_roles()

    if not response.ok:
        print(response.data)
        sys.exit(1)

    for role in response.data.get("items"):
        if role.get("name") == ROLE:
            return role.get("id")
    else:
        return None


def get_new_role(role_id: str, grant_type: str, duration=1) -> object:
    """
    Return the role object for granting target-role membership.

    :param role_id: ID of the target role.
    :param grant_type: Grant type for specifying membership validity.
    :param duration: Validity period of the grant.
                     Only applicable to non-permanent grant types.

    :return: Role object for the specified grant.
    """
    start = datetime.datetime.utcnow()
    end = start + datetime.timedelta(hours=duration)

    roles = {
        "PERMANENT":
        {
            "id": role_id,
            "name": ROLE,
            "grant_type": "PERMANENT",
            "grant_start": None,
            "grant_end": None,
            "floating_length": None,
            "explicit": True
        },
        "FLOATING":
        {
            "id": role_id,
            "name": ROLE,
            "grant_type": "FLOATING",
            "grant_start": None,
            "grant_end": None,
            "floating_length": duration,
            "explicit": True
        },
        "TIME_RESTRICTED":
        {
            "id": role_id,
            "name": ROLE,
            "grant_type": "TIME_RESTRICTED",
            "grant_start": start.isoformat() + "Z",
            "grant_end": end.isoformat() + "Z",
            "floating_length": 0,
            "explicit": True
        }
    }

    if grant_type not in roles:
        print(f"Invalid grant type {grant_type}. Exiting...")
        sys.exit(1)

    return roles[grant_type]


def main():
    print(f"Searching for user {EMAIL}")
    userID = get_user_ID(EMAIL)
    if not userID:
        print(f"Cannot find user with email {EMAIL}. Exiting...")
        sys.exit(1)

    print(f"Fetching target role {ROLE}")
    roleID = get_role_ID(ROLE)
    if not roleID:
        print(f"Cannot find role with name {ROLE}. Exiting...")
        sys.exit(1)

    print("Fetching user's existing roles")
    userRolesQuery = api.get_user_roles(userID)
    if not userRolesQuery.ok:
        print(userRolesQuery.data)
        sys.exit(1)

    print("Determining new role setup for user.")
    userRoles = get_user_roles(userID)
    role = get_new_role(roleID, GRANT_TYPE, VALIDITY)
    userRoles.append(role)

    print("Updating roles for user")
    response = api.set_user_roles(userID, userRoles)

    if response.ok:
        print("User roles updated.")
    else:
        print(response.data)
        print("User-role update failed.")


if __name__ == "__main__":
    main()
