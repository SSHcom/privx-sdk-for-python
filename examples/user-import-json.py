# An example how to use PrivX API for user creation.
# Requires Python 3.6+

import json
import os
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


# Specify the path to the user-data JSON file.
# By default, uses the user-import.json from the data directory.
# For more information about user-data syntax, see the
# PrivX-API specifications.
USER_DATA_FILE = os.path.join(sys.path[0], "data/user-import.json")

# Destination for logging user import.
LOGFILE = "user-import-json.log"


def main():
    with open(USER_DATA_FILE, "r") as f:
        user_data = json.load(f)

    with open(LOGFILE, "w") as log:
        print("Adding users from " + USER_DATA_FILE)

        fails = 0

        for user in user_data:
            response = api.create_user(user)

            if response.ok:
                log.write(user["username"] + " added succesfully.\n")
            else:
                log.write(user["username"] + " failed to be added: ")
                log.write(json.dumps(response.data) + "\n")
                fails += 1

    print("User import completed.")

    if fails > 0:
        print("{} out of {} users failed to be added!".format(fails, len(user_data)))

    print("Check {} for additional information.".format(os.path.abspath(LOGFILE)))


if __name__ == "__main__":
    main()
