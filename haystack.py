"""Author: Andy Rosales Elias. University of California, Santa Barbara. andy00@umail.ucsb.edu | Step 3: Needle in a haystack"""

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

retrieve_str = {'token': token}
initial_req = requests.post("http://challenge.code2040.org/api/haystack", json= retrieve_str)
data = json.loads(initial_req.text)
needle = data['needle']
haystack = data['haystack']
index = haystack.index(needle)
#ALTERNATIVE APPROACH
# for i in len(haystack):
#     if haystack[i] == needle:
#         index = i
payload = {'token':token,'needle': index}
post_req = requests.post("http://challenge.code2040.org/api/haystack/validate", json= payload)
print post_req.status_code, post_req.reason