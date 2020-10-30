from itertools import permutations

def hashfun(msg):
	digest = []
	for i in range(len(msg) - 1):
		digest.append(ord(msg[i]) ^ ord(msg[i + 1]))
	return digest

def reverse(msg):
	reversed_hashes = msg[:]
	reversed_hashes.reverse()
	possibleLastCharList = list(permutations('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',4))
	for i in range(len(possibleLastCharList)):
		reversed_chars = []
		reversed_chars.append(str(possibleLastCharList[i][0]))
		reversed_chars.append(str(possibleLastCharList[i][1]))
		reversed_chars.append(str(possibleLastCharList[i][2]))
		reversed_chars.append(str(possibleLastCharList[i][3]))
		for j in range(len(reversed_hashes)):
			possibleCurrentCharInt = ord(reversed_chars[j]) ^ reversed_hashes[j]
			#print(possibleCurrentCharInt)
			possibleCurrentChar = chr(possibleCurrentCharInt)
			reversed_chars.append(possibleCurrentChar)
		reversed_chars.reverse()
		test_str = str(reversed_chars)
		if (test_str.startswith('flag')):
			print(str(test_str))

print(reverse([10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]))
# [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]

# test_test_test
# [43, 17, 22, 7, 43, 43, 17, 22, 7, 43]
