import sys

cipherText = 'spvk{tln_lqn_heckxf}'
key = 'neverlanctf'
flag = 'flag'

# 97-122 Lowercase English alphabet letters (1-26)
def char_value(c):
    return ord(c) - 96


def to_python_char(char):
    return chr(char + 97)


def add_char(c1, c2):
    return to_python_char((char_value(c1) + char_value(c2)) % 26)


def sub_char(c1, c2):
    return to_python_char((char_value(c1) - char_value(c2)) % 26)


result = ''
keyIndex = 0
for i in range(len(cipherText)):
    c = cipherText[i]
    if cipherText[i] == '{' or c == '}' or c == '_':
        result += c
    else:
        result += sub_char(c, key[keyIndex % len(key)])
        keyIndex += 1
print(result)

#for i in range(4):
#    c1 = cipherText[i]
#    c2 = flag[i]
#    print('+: ' + add_char(c1, c2))
#    print('-: ' + sub_char(c1, c2))
