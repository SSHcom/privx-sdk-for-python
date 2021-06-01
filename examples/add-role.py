# An example how to use PrivX API for granting roles to users.
# Can be used as basis for automating temporary role grants via ServiceNow or
# similar services.
# Requires Python 3.6+

import sys

# Import the PrivX python library.
import privx_api
import config
import datetime

# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.HOSTPORT, config.CA_CERT,
                         config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")


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


def main():
    # Get user.
    print("Searching for user", EMAIL)
    resp = api.search_users(
            search_payload={"keywords": EMAIL})

    userID = ""

    if resp.ok():
        for item in resp.data().get("items"):
            if item.get("email") == EMAIL:
                userID = item.get("id")
                roles = item.get("roles")
    else:
        print(resp.data())
        sys.exit(1)

    if userID == "":
        print("Did not find user ID")
        sys.exit(1)

    print("Found user", userID)

    roleID = ""

    print("Fetching roles")
    roles = api.get_roles()
    if roles.ok():
        roles = roles.data()
        for role in roles.get("items"):
            if role.get("name") == ROLE:
                roleID = role.get("id")
                print("Found role", ROLE, "with ID", roleID)
        if roleID == "":
            print("Cannot find role:", ROLE)
            sys.exit(1)

    else:
        print(resp.data())
        sys.exit(1)

    print("Fetching user roles")
    userRolesQuery = api.get_user_roles(userID)
    if not userRolesQuery.ok():
        print(userRolesQuery.data())
        sys.exit(1)

    userRoles = userRolesQuery.data().get("items")

    if GRANT_TYPE not in ("PERMANENT", "FLOATING", "TIME_RESTRICTED"):
        print("Invalid GRANT_TYPE:", GRANT_TYPE)
        sys.exit(1)

    print("Updating roles for user")
    if GRANT_TYPE == "PERMANENT":
        role = {
            "id": roleID,
            "name": ROLE,
            "grant_type": "PERMANENT",
            "grant_start": None,
            "grant_end": None,
            "floating_length": None,
            "explicit": True
        }
    elif GRANT_TYPE == "FLOATING":
        role = {
            "id": roleID,
            "name": ROLE,
            "grant_type": "FLOATING",
            "grant_start": None,
            "grant_end": None,
            "floating_length": VALIDITY,
            "explicit": True
        }
    elif GRANT_TYPE == "TIME_RESTRICTED":
        start = datetime.datetime.utcnow()
        end = start + datetime.timedelta(hours=VALIDITY)
        role = {
            "id": roleID,
            "name": ROLE,
            "grant_type": "TIME_RESTRICTED",
            "grant_start": start.isoformat() + "Z",
            "grant_end": end.isoformat() + "Z",
            "floating_length": 0,
            "explicit": True
        }

    print(role)
    userRoles.append(role)
    resp = api.set_user_roles(userID, userRoles)

    if resp.ok():
        print("User roles updated.")
    else:
        print("User role update failed.")
        print(resp.data())


if __name__ == "__main__":
    main()
