import sys
import binascii
import bitarray
from pylfsr import LFSR


def encryptWithLfsr(sourceBytes):
	print(f'encryptWithLfsr - source: {binascii.hexlify(sourceBytes)}')
	L = LFSR(fpoly=[6,7], initstate=[1,0,0,0,0,0,0,0], verbose=False)
	sourceBitarray = bitarray.bitarray()
	sourceBitarray.frombytes(sourceBytes)
	cipherBitArray = bitarray.bitarray([L.next() for i in range(len(sourceBitarray))])
	print(f'encryptWithLfsr - cipher: {binascii.hexlify(cipherBitArray.tobytes())}')
	sourceBitarray ^= cipherBitArray
	resultBytes = sourceBitarray.tobytes()
	print(f'encryptWithLfsr - result: {binascii.hexlify(resultBytes)}')
	return resultBytes


if len(sys.argv) != 3:
	print('Usage: app.py sourceFile targetFile')
else:
	sourceFile = sys.argv[1]
	targetFile = sys.argv[2]
	with open(sourceFile, "rb") as f:
		sourceBytes = f.read()
		encrypt_result = encryptWithLfsr(sourceBytes)
		with open(targetFile, "wb") as f:
			output = f.write(encrypt_result)
	print(f'encryption done...')
