"""Author: Andy Rosales Elias. University of California, Santa Barbara. andy00@umail.ucsb.edu | Step 2: Reverse a string"""

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

retrieve_str = {'token':token}
initial_req = requests.post("http://challenge.code2040.org/api/reverse", json= retrieve_str)
string = initial_req.text
if len(string)>1:
    reversed_str = str(string)[::-1]
else:
    reversed_str = str(string)
payload = {'token':token, 'string': reversed_str}
final_req = requests.post("http://challenge.code2040.org/api/reverse/validate", json= payload)
print final_req.status_code, final_req.reason