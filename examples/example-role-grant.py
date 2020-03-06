# An example how to use PrivX API for role grant.
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

email = "joe.firewall@testdomain.com"
roleName = "NQXusers"

# Get user.
print("Searching user ",email)
resp = api.search_users(email)
if resp.ok():
    for item in resp.data().get("items"):
        if item.get("email") == email:
            userID = item.get("id")
            roles = item.get("roles")
else:
    print(resp.data())
    sys.exit(1)


if userID == "":
    print("did not find user ID")
    sys.exit(1)

print("Found user", userID)

roleID = ""

print("Fetching roles")
roles = api.get_roles()
if roles.ok():
    roles = roles.data()
    for role in roles.get("items"):
        if role.get("name") == roleName:
            print("Found role", roleName)
            roleID = role.get("id")
    if roleID == "":
        print("cannot find role with name", roleName)
        sys.exit(1)

else:
    print(resp.data())
    sys.exit(1)


userRoles = api.get_user_roles(userID).data().get("items")

print("Updating roles for user")
# Floating role validity period in hours, clock starts running after user permiossions are checked. 
#role = {
#    "id": roleID,
#    "name": "NQXusers",
#    "grant_type": "FLOATING",
#    "grant_start": None,
#    "grant_end": None,
#    "floating_length": 1,
#    "explicit": True
#}

# Time restricted role validity
now = datetime.datetime.utcnow()
role = {
    "id": roleID,
    "name": "NQXusers",
    "grant_type": "TIME_RESTRICTED",
    "grant_start": now.isoformat()+"Z", # Append Z for UTC timezone
    "grant_end": (now+datetime.timedelta(minutes=5)).isoformat()+"Z", # Append Z for UTC timezone
    "floating_length": 0,
    "explicit": True
}
print(role)
userRoles.append(role)
resp = api.update_user_roles(userID, userRoles)

if resp.ok():
    print("User roles updated.")
else:
    print("User role update failed.")
    print(resp.data())

