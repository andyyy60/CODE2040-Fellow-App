"""Author: Andy Rosales Elias. University of California, Santa Barbara. andy00@umail.ucsb.edu | Step 1: Registration"""

import requests, json

def get_token() :
    # get the token from local disk for security reasons
    data = None
    try:
        data = json.loads(open('tokens.json').read())
    except Exception as e:
        pass
    return data

token = get_token()['token']

payload = {'token':token,'github':'https://github.com/andyyy60/CODE2040-Fellow-App'}
post_req = requests.post("http://challenge.code2040.org/api/register", json= payload)
print post_req.status_code, post_req.reason