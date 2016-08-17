"""Author: Andy Rosales Elias. University of California, Santa Barbara. andy00@umail.ucsb.edu | Step 1: Registration"""

import requests

payload = {'token':'afc2cb07854c50693f2607207c8b87c3','github':'https://github.com/andyyy60/CODE2040-Fellow-App'}
post_req = requests.post("http://challenge.code2040.org/api/register", json= payload)
print post_req.status_code, post_req.reason