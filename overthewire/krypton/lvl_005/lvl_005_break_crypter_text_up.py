import sys

def test(fileName, keyLength):
	output = []
	with open(fileName, "rt") as f:
		output = list(f.read())
	for counter in range(keyLength):
		print(f'counter: {counter}')
		for i in range(int(len(output) / keyLength)):
			c = output[(i * keyLength) + counter]
			if not c:
				continue
			print(c, end = '')
		print('\n')


if len(sys.argv) != 3:
	print('Usage: [command] inputFileName keyLength')
else:
	test(sys.argv[1], int(sys.argv[2]))