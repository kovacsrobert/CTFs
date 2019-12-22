import sys
import subprocess
import binascii
import bitarray
from pylfsr import LFSR


def lsrf(text, key):
	textBitarray = bitarray.bitarray()
	textBitarray.frombytes(text)
	keyBitarray = bitarray.bitarray()
	keyBitarray.frombytes(key)
	resultBitarray = bitarray.bitarray()
	resultBitarray = textBitarray ^ keyBitarray
	print(f't: {textBitarray}')
	print(f'k: {keyBitarray}')
	print(f'c: {resultBitarray}')
	return resultBitarray.tobytes()


def executeEncryption(decoderPythonFile, sourceTempFile, targetTempFile, fileContent):
	with open(sourceTempFile, "wb") as f:
		f.write(fileContent.encode())
	subprocess.call([sys.executable, decoderPythonFile, sourceTempFile, targetTempFile])
	with open(targetTempFile, "rb") as f:
		return f.read()


def extractKey(decoderPythonFile, sourceTempFile, targetTempFile, fileContent):
	textBitArray = bitarray.bitarray()
	textBitArray.frombytes(fileContent.encode())
	encrypted = executeEncryption(decoderPythonFile, sourceTempFile, targetTempFile, fileContent)
	encryptedBitArray = bitarray.bitarray()
	encryptedBitArray.frombytes(encrypted)
	keyBitarray = textBitArray ^ encryptedBitArray
	return keyBitarray


def determineKey(decoderPythonFile, sourceTempFile, targetTempFile):
	finalKeyBitArray = bitarray.bitarray()
	for i in range(15):
		finalKeyBitArray.extend([0,0,0,0,0,0,0,0])
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'aaaaaaaaaaaaaaa')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'bbbbbbbbbbbbbbb')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'ccccccccccccccc')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'ddddddddddddddd')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'eeeeeeeeeeeeeee')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'fffffffffffffff')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'ggggggggggggggg')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'hhhhhhhhhhhhhhh')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'iiiiiiiiiiiiiii')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'jjjjjjjjjjjjjjj')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'kkkkkkkkkkkkkkk')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'lllllllllllllll')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'mmmmmmmmmmmmmmm')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'nnnnnnnnnnnnnnn')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'ooooooooooooooo')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'ppppppppppppppp')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'qqqqqqqqqqqqqqq')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'rrrrrrrrrrrrrrr')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'sssssssssssssss')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'ttttttttttttttt')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'uuuuuuuuuuuuuuu')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'vvvvvvvvvvvvvvv')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'wwwwwwwwwwwwwww')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'xxxxxxxxxxxxxxx')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'yyyyyyyyyyyyyyy')
	finalKeyBitArray |= extractKey(decoderPythonFile, sourceTempFile, targetTempFile, 'zzzzzzzzzzzzzzz')
	return finalKeyBitArray.tobytes()


if len(sys.argv) != 5:
	print('Usage: app.py decoderPythonFile sourceTempFile targetTempFile originalEncrypted')
else:
	decoderPythonFile = sys.argv[1]
	sourceTempFile = sys.argv[2]
	targetTempFile = sys.argv[3]
	originalEncrypted = sys.argv[4].lower().encode()
	key = determineKey(decoderPythonFile, sourceTempFile, targetTempFile)
	print('')
	print(f'key: {key}')
	plainText = lsrf(originalEncrypted, key)
	print(f'plainText: {plainText}')
