# Import the PrivX python library.
import json
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
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate(config.API_CLIENT_ID, config.API_CLIENT_SECRET)

# SECRET PARAMETERS
# Secret name
SECRET_NAME = "name1"

# Give read access to the secret for these role(s)
SECRET_READ_ROLES = ["name-of-role"]

# Give write access to the secret for these role(s)
SECRET_WRITE_ROLES = ["name-of-role"]

# The secret data in JSON format
SECRET_DATA = {"username": "alice", "password": "example_password"}

# Give the secret's owner user id
SECRET_OWNER = "a06a619e-1979-46ef-ab77-8000c2ff1f3c"


def main():
    try:
        _check_secret_already_exists(SECRET_NAME)
        read_role_data = _get_role_data(SECRET_READ_ROLES)
        write_role_data = _get_role_data(SECRET_WRITE_ROLES)
    except Exception as e:
        print(e)
        print("Exiting without modifying anything...")
        sys.exit(1)

    # Create-secret request data
    data = {
        "read_roles": read_role_data,
        "write_roles": write_role_data,
        "data": SECRET_DATA,
    }

    response = api.create_user_secret(SECRET_OWNER, SECRET_NAME, data)

    if response.ok:
        print(json.dumps(data))
        print("Secret created succesfully!")
    else:
        print(response.data)
        print("Secret creation failed!")


def _get_role_data(role_names: list[str]) -> list[dict]:
    """
    Helper function for obtaining role data by role names.

    :param role_names: List of role names.
    :return: List describing the roles in {id, name} format.
    :raise: Exception if any role(s) cannot be found from PrivX.
    """
    response = api.resolve_roles(role_names)
    if response.ok:
        response_data = response.data["items"]
    else:
        print(response.data)
        raise Exception("Error obtaining role data")

    role_data = []

    for role in role_names:
        data = next((r for r in response_data if r["name"] == role), None)
        if data:
            role_data.append({"id": data["id"], "name": data["name"]})
        else:
            raise Exception("Error: role " + role + " does not exist.")

    return role_data


def _check_secret_already_exists(secret_name: str) -> None:
    """
    Helper function to check if secret with SECRET_NAME already exists

    :raise: Exception if secret with SECRET_NAME already exists.
    """
    response = api.get_secret(secret_name)
    if response.ok:
        print(response.data)
        raise Exception("Secret named " + secret_name + " already exists!")


if __name__ == "__main__":
    main()
