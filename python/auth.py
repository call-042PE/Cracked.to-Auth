import requests
import json
import uuid
import os

premiumplus = ['11', '12', '93', '96', '97', '99', '100', '101', '4', '3', '6', '94', '92']

def ctoauth():
    if os.path.isfile('key.dat'):
        current_hwid = uuid.getnode()
        f = open('key.dat', 'r')
        auth = f.read()
        data = {
            "a": "auth",
            "k": str(auth),
            "hwid": str(current_hwid)
        }
        checkauth = requests.post('https://cracked.to/auth.php', data=data)
        with checkauth:
            json1 = json.loads(checkauth.text)
            if '"auth":true' in checkauth.text:
                #Upgraded users check starts here
                if any(json1["group"] in s for s in premiumplus):
                    print("Welcome: " + json1["username"])
                else:
                    print("You need to be Premium+ to use this tool sir.")
                    exit()
                #Upgraded users check ends here
            else:
                print(checkauth.text)
                exit()
    else:
        authkey = str(input('Insert Cracked.to Auth Key: '))
        current_hwid = uuid.getnode()

        data = {
            "a": "auth",
            "k": str(authkey),
            "hwid": str(current_hwid)
        }

        checkauth = requests.post('https://cracked.to/auth.php', data=data)

        with checkauth:
            json2 = json.loads(checkauth.text)
            if '"auth":true' in checkauth.text:
                #Upgraded users check starts here
                if any(json2["group"] in s for s in premiumplus):
                    f = open('key.dat', 'w')
                    f.write(authkey)
                    print("Welcome: " + json2["username"])
                else:
                    print("You need to be Premium+ to use this tool sir.")
                    exit()
                #Upgraded users check ends here
            else:
                print(checkauth.text)
                exit()
