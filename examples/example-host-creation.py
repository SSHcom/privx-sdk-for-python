# An example how to use PrivX API for host creation.
# Requires Python 3.6+

# Import the PrivX python library.
import privx_api
import config

# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.CA_CERT,
						 config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")

# Search role ID for host account mapping.
role_id = ""
resp = api.get_roles()
if resp.ok():
	for role in resp.data().get("items"):
		if role.get("name") == "privx-admin":
			role_id = role.get("id")
if role_id == "":
	print("Failed to get role ID.")

# Create host.
data = {
	"common_name": "api-test",
	"addresses": [
		"test.api.host.net",
		"123.123.123.123"
	],
	"services": [
		{
			"service": "SSH",
			"address": "123.123.123.123",
			"port": 22,
			"source": "UI",
		},
	],
	"principals": [
		{
			"principal": "root",
			"passphrase": "secret",
			"source": "UI",
			"roles": [
				{
					"id": role_id,
				},
			],
		},
	],
}

resp = api.create_host(data)
if resp.ok():
	print("Host created.")
else:
	print("Host creation failed.")
	print(resp.data())

