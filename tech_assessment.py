"""Author: Andy Rosales Elias. University of California, Santa Barbara. andy00@umail.ucsb.edu | Tech Assessment"""

import requests, json, time


def get_token():
    # get the token from local disk for security reasons
    data = None
    try:
        data = json.loads(open('tokens.json').read())
    except Exception as e:
        pass
    return data


def validation(endpoint):
    """validates endpoint and returns server response"""
    token = get_token()['token']
    token_data = {'token': token}
    post_req = requests.post(endpoint, json=token_data)
    return post_req


def registration():
    """Step 1"""
    token = get_token()['token']
    if token == None: #Check for invalid token
        print "Invalid token!"
        return False
    payload = {'token': token, 'github': 'https://github.com/andyyy60/CODE2040-Fellow-App'}
    post_req = requests.post("http://challenge.code2040.org/api/register", json= payload)
    print post_req.status_code, post_req.reason


def reverse():
    """Step 2"""
    token = get_token()['token']
    if token == None: #Check for invalid token
        print "Invalid token!"
        return False
    initial_req = validation("http://challenge.code2040.org/api/reverse")
    string = initial_req.text
    if len(string) > 1:
        reversed_str = str(string)[::-1]
    else: #edge case, if the string length is less than or equal to 1 it's a palindrome
        reversed_str = str(string)
    payload = {'token': token, 'string': reversed_str}
    final_req = requests.post("http://challenge.code2040.org/api/reverse/validate", json= payload)
    print final_req.status_code, final_req.reason


def haystack():
    """Step 3"""
    token = get_token()['token']
    if token == None: #Check for invalid token
        print "Invalid token!"
        return False
    initial_req = validation("http://challenge.code2040.org/api/haystack")
    data = json.loads(initial_req.text)
    needle = data['needle']
    haystack = data['haystack']
    index = haystack.index(needle)
    # ALTERNATIVE APPROACH
    # for i in len(haystack):
    #     if haystack[i] == needle:
    #         index = i
    payload = {'token': token, 'needle': index}
    post_req = requests.post("http://challenge.code2040.org/api/haystack/validate", json= payload)
    print post_req.status_code, post_req.reason


def prefix():
    """Step 4"""
    token = get_token()['token']
    if token == None: #Check for invalid token
        print "Invalid token!"
        return False
    initial_req = validation("http://challenge.code2040.org/api/prefix")
    data = json.loads(initial_req.text)
    prefix = data['prefix']
    str_array = data['array']
    not_prefix = []
    for item in str_array:
        if item[:len(prefix)] != prefix: #checks from index 0 to length of prefix
            not_prefix.append(item)
    payload = {'token': token, 'array': not_prefix}
    post_req = requests.post("http://challenge.code2040.org/api/prefix/validate", json= payload)
    print post_req.status_code, post_req.reason

def dating():
    """Step 5"""
    token = get_token()['token']
    if token == None: #Check for invalid token
        print "Invalid token!"
        return False
    initial_req = validation("http://challenge.code2040.org/api/dating")
    data = json.loads(initial_req.text)
    datestamp = data['datestamp']
    interval = int(data['interval'])
    pattern = '%Y-%m-%dT%H:%M:%SZ'
    epoch = int(time.mktime(time.strptime(datestamp, pattern))) #turns datestamp value to seconds since the epoch
    new_epoch = epoch+interval #add the interval to initial date in seconds
    new_date = time.strftime(pattern, time.localtime(new_epoch)) #convert back to ISO
    payload = {'token':token, 'datestamp': str(new_date)}
    post_req = requests.post("http://challenge.code2040.org/api/dating/validate", json= payload)
    print post_req.status_code, post_req.reason, new_date, datestamp
