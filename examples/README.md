# PrivX SDK Examples

The following examples demonstrates a typical usage scenario. The usage of examples requires Python 3.6+ 

Usage Python Virtual Environment simplify development 

```bash
python3 -m pip install virtualenv
python3 -m venv .env
source .env/bin/activate
pip install git+git://github.com/SSHcom/privx-sdk-for-python.git
```

## Register API Client

You have to register your API client with PrivX before usage. Open PrivX Web UI and go to

```
Settings > Deployment > Integrate With PrivX Using API Clients
```

Click `ADD API CLIENT`, give a human readable and permissions. The permissions for the client varies on the use case, check the PrivX documentation for permission explanation.

After the API client creation, you can find the secrets for the client
under credentials section. The example scripts must include the API client ID
("API Client ID") and secret ("API Client Secret"), config.py must include
the OAuth client secret ("OAuth Client Secret").

Fill in the missing fields in config.py
* HOSTNAME, the PrivX instance address, like "my.privx.intance.net"
* CA_CERT, the CA certificate, found on the API clients page ("TLS Trust Anchor")
* OAUTH_CLIENT_SECRET, found on the API clients page ("OAuth Client Secret")
