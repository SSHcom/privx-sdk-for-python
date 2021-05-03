# Import the PrivX python library.
import json
import sys

import privx_api
import config


# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.HOSTPORT, config.CA_CERT,
                         config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")


# SECRET PARAMETERS
# Secret name
SECRET_NAME = "Example Secret 01"

# Give read access to the secret for these role(s)
SECRET_READ_ROLES = ["privx-admin"]

# Give write access to the secret for these role(s)
SECRET_WRITE_ROLES = ["privx-admin"]

# The secret data in JSON format
SECRET_DATA = \
    {
        "username": "alice",
        "password": "example_password"
    }


def main():
    try:
        _check_secret_already_exists()
        role_ids = _get_role_data()
    except Exception as e:
        print(e)
        print("Exiting without modifying anything...")
        sys.exit(1)

    # Create-secret request data
    data = {
        "name": SECRET_NAME,
        "read_roles": [{"id": role_ids[role], "name": role}
                       for role in SECRET_READ_ROLES],
        "write_roles": [{"id": role_ids[role], "name": role}
                        for role in SECRET_WRITE_ROLES],
        "data": SECRET_DATA
    }

    response = api.create_secret(data)

    if response.ok():
        print(json.dumps(data))
        print("Secret created succesfully!")
    else:
        print(response.data())
        print("Secret creation failed!")


def _get_role_data() -> dict:
    """
    Helper function for obtaining role data for the read/write roles.

    :return: Dictionary describing the roles in 'name: ID' format.
    :raise: Exception if any role(s) cannot be found from PrivX.
    """
    response = api.resolve_role(SECRET_READ_ROLES + SECRET_READ_ROLES)
    roles = {x["name"]: x["id"] for x in response.data()["items"]}

    # Verify that all required roles exist
    for role in SECRET_READ_ROLES + SECRET_READ_ROLES:
        if role not in roles:
            raise Exception(f"Error: cannot find role {role} from the system.")

    return roles


def _check_secret_already_exists():
    """
    Helper function to check if secret with SECRET_NAME already exists

    :raise: Exception if secret with SECRET_NAME already exists.
    """
    response = api.get_secret(SECRET_NAME)
    if response.ok():
        print(response.data())
        raise Exception(f"Secret named {SECRET_NAME} already exists")


if __name__ == '__main__':
    main()
