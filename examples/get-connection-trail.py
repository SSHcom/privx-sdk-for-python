# Import the PrivX python library.
import base64
import json
import privx_api
import config

# Replace with the ID of the connection to output
CID = "CONNECTION_ID"
FORMAT = "jsonl"

# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.HOSTPORT, config.CA_CERT,
                         config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")


def get_connection(cid: str) -> str:
    conn = api.get_connection(cid)
    if conn.ok():
        return conn.data()

    return conn.data()["details"]

def create_trail_session(cid: str, chid: str) -> str:
    sess = api.create_trail_log_session_id(cid,chid)
    if sess.ok():
        return sess.data()

    return sess.data()["details"]


def download_trail_log(cid: str, chid: str, sess: str, fmt: str) -> str:
    conn = api.download_trail_log(cid,chid,sess,fmt)
    if conn.ok():
        return conn.data()

    return conn.data()["details"]

def print_trail(trail: str) -> str:
    arr = trail.splitlines()
    ss = ""
    for i in arr:
        line = json.loads(i)
        if line["type"] == "stdin":
            s = base64.b64decode(line["data"]).decode("latin1")
            if s == "\r":
                print(line["ts"][0:19]+" "+ss)
                ss = ""
            else:
                ss += s

def main():
# Get the connection object
    conn = get_connection(CID)

    # Iterate channels
    for c in conn["trail"]["channels"]:
        if c["type"] == "shell":
    # Get a session ID for trail download
            sess = create_trail_session(CID,c["id"])
    # Get the trail
            dl = download_trail_log(CID,c["id"],sess["session_id"],FORMAT)
    # Parse the trail
            print("\r\nCommands for connection "+CID+" channel "+c["id"])
            print("----------------------------------------------------------------------")
            print_trail(dl)


if __name__ == '__main__':
    main()
