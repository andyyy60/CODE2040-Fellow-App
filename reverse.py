"""Author: Andy Rosales Elias. University of California, Santa Barbara. andy00@umail.ucsb.edu | Step 2: Reverse a string"""

import requests

retrieve_str = {'token':'afc2cb07854c50693f2607207c8b87c3'}
initial_req = requests.post("http://challenge.code2040.org/api/reverse", json= retrieve_str)
string = initial_req.text
if len(string)>1:
    reversed_str = str(string)[::-1]
else:
    reversed_str = string
payload = {'token':'afc2cb07854c50693f2607207c8b87c3', 'string': reversed_str}
final_req = requests.post("http://challenge.code2040.org/api/reverse/validate", json= payload)
print final_req.status_code, final_req.reason