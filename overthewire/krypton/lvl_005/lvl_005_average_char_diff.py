import sys
import operator

# 97-122 Lowercase English alphabet letters (1-26)
def charDiff(c1, c2):
	c1Pos = ord(c1) - 96
	c2Pos = ord(c2) - 96
	result = (c2Pos - c1Pos) % 27
	print(f'difference between {c1}({c1Pos}) and {c2}({c2Pos}) is: {result}')
	return result

def toPythonChar(englishChar):
	return chr(englishChar + 96)


def averageCharDistance(base, encrypted):
	if len(base) != len(encrypted):
		print('Not same length')
		return
	average = {}
	for i in range(len(base)):
		diff = charDiff(base[i], encrypted[i])
		if diff in average:
			updateDict = {}
			updateDict[diff] = int(average.get(diff)) + 1
			average.update(updateDict)
		else:
			updateDict = {}
			updateDict[diff] = 1
			average.update(updateDict)
	#maxKey = max(average, key=average.get)
	#print('maxKey: ', maxKey)
	sortedAverage = {k: v for k, v in sorted(average.items(), key=lambda item: item[1], reverse=True)}
	#print('sortedAverage: ', sortedAverage)
	for key in sortedAverage:
		print(f'{toPythonChar(key)}({key}) was counted {sortedAverage[key]}')

if len(sys.argv) != 3:
	print('Usage: [command] base encrypted')
else:
	averageCharDistance(list(sys.argv[1].lower()), list(sys.argv[2].lower()))