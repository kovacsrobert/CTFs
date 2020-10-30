def hashfun(msg):
    digest = []
    for i in range(len(msg) - 4):
        digest.append(ord(msg[i]) ^ ord(msg[i + 4]))
    return digest

def reverse(msg):
	searchLength = msg + 4
	digest = []
    for i in range(len(msg) + 4):
        digest.append(ord(msg[i]) ^ ord(msg[i + 4]))
    return digest

print(hashfun("test_test_test_asd_asd_asd"))
print(hashfun2(hashfun("test_test_test_asd_asd_asd")))
# [10, 30, 31, 62, 27, 9, 4, 0, 1, 1, 4, 4, 7, 13, 8, 12, 21, 28, 12, 6, 60]

# test_test_test
# [43, 17, 22, 7, 43, 43, 17, 22, 7, 43]
