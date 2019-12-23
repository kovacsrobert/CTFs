# 65-90 Uppercase English alphabet letters

def add_char(original, offset):
    original_pos = ord(original) - 65
    offset_pos = ord(offset) - 65
    result_char = chr((original_pos + offset_pos) % 26 + 65)
    return result_char


def sub_char(original, offset):
    original_pos = ord(original) - 65
    offset_pos = ord(offset) - 65
    result_char = chr((original_pos - offset_pos) % 26 + 65)
    return result_char


def encrypt(plain):
	cipher = list(plain)[:]
	password = 'EICTDGYIYZKTHNSIRFXYCPFUEOCKRN'
	for i in range(len(plain)):
		cipher[i] = add_char(plain[i], password[i % len(password)])
	return ''.join(cipher)


def decrypt(cipher):
	plain = list(cipher)[:]
	password = 'EICTDGYIYZKTHNSIRFXYCPFUEOCKRN'
	for i in range(len(plain)):
		plain[i] = sub_char(cipher[i], password[i % len(password)])
	return ''.join(plain)


def test(plain):
	print('{0} -> {1} -> {2}'.format(plain, encrypt(plain), decrypt(encrypt(plain))))


test('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
test('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
test('LFSRISNOTRANDOM')
