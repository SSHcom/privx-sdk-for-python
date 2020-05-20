# Requires Python 3.6+
import sys
import csv

# Import the PrivX python library.
import privx_api


# Import the configs.
import config

# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.HOSTPORT, config.CA_CERT,
                         config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")


def get_roles():
    resp = api.get_roles()
    if resp.ok():
        data_load = resp.data()
        roles_data = {}
        for role_data in data_load['items']:
            name = role_data['name']
            roles_data[name] = role_data['id']
        return roles_data
    else:
        error = "Get Roles operation failed:"
        process_error(error)


def get_role_mapping_data(role_id, role_name):
    resp = api.search_hosts(role=[role_id])
    if resp.ok():
        data_load = resp.data()
    else:
        error = "Hosts search operation failed:"
        process_error(error)
    role_hosts = {}
    hosts_accounts = {}
    hosts_accounts_list = {}
    all_data = []
    if data_load['count']:
        resp1 = api.get_role_members(role_id)
        if resp1.ok():
            data_load1 = resp1.data()
        else:
            error = "Get role members operation failed:"
            process_error(error)
    else:
        return None
    members = []
    for member in data_load1['items']:
        members.append(member['principal'])
    members = ",".join(members)
    for host_data in data_load['items']:
        accounts = []
        for principal in host_data['principals']:
            if principal['principal']:
                accounts.append(principal['principal'])
            address = ",".join(host_data['addresses'])
            hosts_accounts[address] = ",".join(accounts)
    for host, account in sorted(hosts_accounts.items()):
        hosts_accounts_list.setdefault(account, []).append(host)
    for accounts, hosts in hosts_accounts_list.items():
        role_hosts["user_id"] = members
        role_hosts["role_name"] = role_name
        role_hosts['target_hosts'] = "\n".join(hosts)
        role_hosts['target_accounts'] = accounts
        all_data.append(dict(role_hosts))
    return all_data


def process_error(messages):
    print(messages)
    sys.exit(2)


def main():
    header_printed = False
    output_csvfile = "access_report.csv"
    roles_data = get_roles()
    all_role_data = []
    for role_name, role_id in roles_data.items():
        role_data = get_role_mapping_data(role_id, role_name)
        if role_data:
            for data in role_data:
                all_role_data.append(dict(data))
    with open(output_csvfile, "w") as f:
        print("Writing role mapping data to", output_csvfile, end=' ')
        for data in all_role_data:
            w = csv.DictWriter(f, data.keys())
            if not header_printed:
                w.writeheader()
                header_printed = True
            w.writerow(data)
    print("\nDone")


if __name__ == '__main__':
    main()