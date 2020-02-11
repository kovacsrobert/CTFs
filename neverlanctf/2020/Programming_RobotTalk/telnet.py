from telnetlib import Telnet
import base64

tn = Telnet('challenges.neverlanctf.com', 1120)
while True:
	data = tn.read_until(b'Hello world', 1)
	if (data.find('flag') > 0):
		print("Finished with flag: " + data)
		break;
	cipherIndex = data.find('decrypt: ') + len('decrypt: ')
	cipher = data[cipherIndex:].encode()
	print('cipher: -' + cipher + '-')
	plainText = base64.b64decode(cipher)
	print('plainText: -' + plainText + '-')
	tn.write(plainText)
tn.close()