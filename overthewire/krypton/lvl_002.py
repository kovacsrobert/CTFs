# 65-90 Uppercase English alphabet letters
# 97-122 Lowercase English alphabet letters

text = "YRIRY GJB CNFFJBEQ EBGGRA"

def moveChar(character):
    newChar = ord(character) + 1
    if newChar > 90 and newChar < 97:
        newChar = 97
    elif newChar > 122:
        newChar = 65
    return chr(newChar)


value = text
for i in range(50):
    print(value)
    newValue = ''
    for j in range(len(value)):
        if value[j] is not ' ':
            newValue += moveChar(value[j])
        else:
            newValue += ' '
    value = newValue
