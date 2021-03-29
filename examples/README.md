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

## Example execution of reporting scripts

Get role mapping data (Access Report)
```
$ python3 get-roles-mapping-report.py
Writing role mapping data to access_report.csv
Done
$ head -n2 access_report.csv
user_id,role_name,target_hosts,target_accounts
"jsingh,nhirbli,nsleiman,tnandy,pre-sales",partners-linux-admin,"ec2-18-120-215-133.eu-west-2.compute.amazonaws.com,ip-172-31-10-79.eu-west-2.compute.internal",centos
```

Get historical connection data (ALL users or individual user)
```
$ python3 get-access-report.py -h

get-access-report.py  -h or --help
get-access-report.py  -u user1
get-access-report.py  --user ALL
$ python3 get-access-report.py
Writing Connection data to ALL_connection_data.csv
Done
$ head -n3 ALL_connection_data.csv
user,type,mode,authentication_method,target_host_address,target_host_account,connected,disconnected
dwishart,RDP,UI,CERT,ec2-35-176-205-41.eu-west-2.compute.amazonaws.com,dwishart,2020-02-28T18:11:09,2020-02-28T18:12:29
nfsadmin,SSH,UI,CERT,ec2-35-177-231-225.eu-west-2.compute.amazonaws.com:22,centos,2020-10-01T09:16:03,2020-10-01T09:21:07


$ python3 get-access-report.py -u kkumar
Writing Connection data to kkumar_connection_data.csv
Done
$ head -n3 kkumar_connection_data.csv
user,type,mode,authentication_method,target_host_address,target_host_account,connected,disconnected
kkumar,SSH,UI,CERT,extender1/ec2-3-10-55-30.eu-west-2.compute.amazonaws.com:22,centos,2020-02-12T12:31:33,2020-02-12T12:31:38
kkumar,SSH,UI,CERT,ec2-18-130-138-218.eu-west-2.compute.amazonaws.com:22,centos,2020-09-21T09:41:49,2020-09-21T17:37:26
```

Get hosts data
```
$ python3 get-hosts-report.py
Writing hosts data to hosts_data.csv
Done
$ head -n3 hosts_data.csv
common_name,addresses,users,protocol,audit_enabled,created,updated,updated_by
Ora2PG-VISA,ip-172-31-43-205.eu-west-2.compute.internal,centos,SSH,False,2020-09-16T14:50:13,2021-03-29T12:53:05,
Ora2PG-DOCS,ip-172-31-42-16.eu-west-2.compute.internal,centos,SSH,False,2020-09-29T10:03:47,2021-03-29T12:53:05,
```
