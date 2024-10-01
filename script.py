import csv
import json
from datetime import datetime
import copy

def create_json(csv_f):
    items = []
    base = {
        "passwordHistory": None,
        "revisionDate": None,
        "creationDate": None,
        "deletedDate": None,
        "id": None,
        "organizationId": None,
        "folderId": None,
        "type": 1,
        "reprompt": 0,
        "name": "hfw.vitap.ac.in",
        "notes": None,
        "favorite": False,
        "login": {
            "fido2Credentials": [],
            "uris": [
                {"match": None, "uri": "https://hfw.vitap.ac.in:8090/httpclient.html"},
                {"match": None, "uri": "172.18.10.10:1000/login?"}
            ],
            "username": None,
            "password": None,
            "totp": None
        },
        "collectionIds": None
    }
    
    t = datetime.utcnow().isoformat() + "Z"
    
    try:
        with open(csv_f, 'r') as f:
            r = csv.reader(f)
            h = next(r)
            if h != ['Username', 'Password']:
                print(f"CSV header mismatch, got {h}")
                return
            
            id_cnt = 1

            for row in r:
                if len(row) != 2:
                    print(f"Row format incorrect: {row}")
                    continue

                u, p = row
                item = copy.deepcopy(base)
                item["revisionDate"] = t
                item["creationDate"] = t
                item["id"] = f"random-id-{id_cnt}"
                item["login"]["username"] = u
                item["login"]["password"] = p

                items.append(item)
                id_cnt += 1

    except FileNotFoundError:
        print(f"File {csv_f} not found.")
    except Exception as e:
        print(f"{e}")
    
    login_data = {"encrypted": False, "items": items}
    
    try:
        with open('login.json', 'w') as jf:
            json.dump(login_data, jf, indent=4)
        print("login.json created!")
    except Exception as e:
        print(f"Error: {e}")

create_json('data.csv')
