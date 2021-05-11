# Requires Python 3.6+
import csv
import sys

# Import the configs.
import config

# Import the PrivX python library.
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
api.authenticate("API client ID", "API client secret")


def get_host_data():
    offset = 0
    limit = 1000
    resp = api.search_hosts(offset=offset, limit=limit)
    if resp.ok():
        data_load = resp.data()
        data_items = data_load["items"]
        count = data_load["count"] - limit
        while count > 0:
            offset = offset + limit
            resp = api.search_hosts(offset=offset, limit=limit)
            data_load = resp.data()
            if resp.ok():
                data_items = data_items + data_load["items"]
                count = count - limit
        hosts_data = {}
        all_data = []
        data = "audit_enabled,created,updated"
        data_list = data.split(",")
        for host_data in data_items:
            hosts_data["common_name"] = host_data["common_name"]
            hosts_data["addresses"] = ",".join([a for a in host_data["addresses"]])
            hosts_data["users"] = ",".join(
                [
                    u["principal"] if u["principal"] else "DirectoryUser"
                    for u in host_data["principals"]
                ]
            )
            hosts_data["protocol"] = ",".join(
                list(dict.fromkeys([p["service"] for p in host_data["services"]]))
            )
            for p in data_list:
                if p in ("created", "updated"):
                    host_data[p] = host_data[p].split(".")[0]
                hosts_data[p] = host_data[p]
            all_data.append(dict(hosts_data))
        return all_data
    else:
        error = "Get hosts Connection data operation failed:"
        process_error(error)


def export_host_data():
    output_csvfile = "hosts_data.csv"
    hosts_data = get_host_data()
    if len(hosts_data) == 0:
        print("no host data")
    else:
        host_keys = hosts_data[0].keys()
        print("Writing hosts data to", output_csvfile, end=" ")
        with open(output_csvfile, "w") as f:
            w = csv.DictWriter(f, host_keys)
            w.writeheader()
            for data in hosts_data:
                w.writerow(data)
    print("\nDone")


def process_error(messages):
    print(messages)
    sys.exit(2)


def main():
    export_host_data()


if __name__ == "__main__":
    main()
