# Requires Python 3.6+
import csv
import sys

# Import the configs.
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

# Default search order how to report user names in the output file. 
# NOTE: Not all user records have "principal" field defined necessarily,
# hence the script will check samaccountname and DN fields as a backup
username_attributes_to_check = ['principal', 'samaccountname', 'distinguished_name']

def get_roles():
    resp = api.get_roles()
    if resp.ok:
        data_load = resp.data
        roles_data = {}
        for role_data in data_load["items"]:
            name = role_data["name"]
            roles_data[name] = role_data["id"]
        return roles_data
    else:
        error = "Get Roles operation failed:"
        process_error(error)


def get_role_mapping_data(role_id, role_name):
    resp = api.search_hosts(search_payload={"role": [role_id]})
    if not resp.ok:
        error = "Hosts search operation failed:"
        process_error(error)

    data_load = resp.data
    role_hosts = {}
    hosts_accounts = {}
    hosts_accounts_list = {}
    all_data = []
    if data_load["count"]:
        resp1 = api.get_role_members(role_id)
        if not resp1.ok:
            error = "Get role members operation failed:"
            process_error(error)

        data_load1 = resp1.data
    else:
        return None
    members = []

    # Get userID data according to username attribute configuration
    for member in data_load1["items"]:
        for attribute in username_attributes_to_check:
            if attribute in member:
                members.append(member[attribute])
                # Break: no need to continue checking other attributes to find user name
                break
        else:
            print(f"Did not find user attribute, please configure script to use correct fields for user name attributes")
            members.append(member["Username not defined in these attribute fields: {username_attributes_to_check}"])

    members = ",".join(members)
    for host_data in data_load["items"]:
        accounts = []
        for principal in host_data["principals"]:
            if principal["principal"]:
                accounts.append(principal["principal"])
            address = ",".join(host_data["addresses"])
            hosts_accounts[address] = ",".join(accounts)
    for host, account in sorted(hosts_accounts.items()):
        hosts_accounts_list.setdefault(account, []).append(host)
    for accounts, hosts in hosts_accounts_list.items():
        role_hosts["user_id"] = members
        role_hosts["role_name"] = role_name
        role_hosts["target_hosts"] = "\n".join(hosts)
        role_hosts["target_accounts"] = accounts
        all_data.append(dict(role_hosts))
    return all_data


def process_error(messages):
    print(messages)
    sys.exit(2)


def main():
    output_csvfile = "access_report.csv"
    roles_data = get_roles()
    all_role_data = []
    for role_name, role_id in roles_data.items():
        role_data = get_role_mapping_data(role_id, role_name)
        if role_data:
            for data in role_data:
                all_role_data.append(dict(data))
    all_role_keys = all_role_data[0].keys()
    print("Writing role mapping data to", output_csvfile, end=" ")
    with open(output_csvfile, "w") as f:
        w = csv.DictWriter(f, all_role_keys)
        w.writeheader()
        for data in all_role_data:
            w.writerow(data)
    print("\nDone")


if __name__ == "__main__":
    main()
