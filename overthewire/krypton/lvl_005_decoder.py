import sys


def parse_input(key_length, files):
    string_output = ["" for x in range(key_length)]
    print(f'keyLength: {key_length}')
    print('')
    for file in files:
        print(f'file: {file}')
        with open(file, "rt") as f:
            output = f.read().lower()
            print(f'output: {output}')
            for counter in range(key_length):
                # print(f'counter: {counter}')
                for i in range(int(len(output) / key_length) + 1):
                    index = (i * key_length) + counter
                    if index >= len(output):
                        continue
                    c = output[index]
                    if not c:
                        continue
                    string_output[counter] += c
            # for counter in range(key_length):
            #     print(f'string_output[{counter}], length {len(string_output[counter])}: {string_output[counter]}')
        print('')
    return string_output


# 97-122 Lowercase English alphabet letters (1-26)
def char_diff(c1, c2):
    c1_pos = ord(c1) - 96
    c2_pos = ord(c2) - 96
    result = (c2_pos - c1_pos) % 26
    # print(f'difference between {c1}({c1_pos}) and {c2}({c2_pos}) is: {result}')
    return result


def to_python_char(char):
    return chr(char + 97)


def find_e_letter_offsets(letter_input_list):
    best_cipher = []
    for i in range(len(letter_input_list)):
        # print(f'checking max letters for {i}. input')
        max_letter_frequency_dict = {}
        for j in range(len(letter_input_list[i])):
            current_letter = letter_input_list[i][j]
            # print(f'current_letter: {current_letter}')
            if current_letter in max_letter_frequency_dict:
                max_letter_frequency_dict.update(
                    {current_letter: int(max_letter_frequency_dict.get(current_letter)) + 1})
            else:
                max_letter_frequency_dict.update({current_letter: 1})
        sorted_max_letter_frequency_dict = {k: v for k, v in
                                            sorted(max_letter_frequency_dict.items(), key=lambda item: item[1],
                                                   reverse=True)}
        # for key in sorted_max_letter_frequency_dict:
        #     print(f'{key} was counted {sorted_max_letter_frequency_dict[key]}')
        picked_max_frequency_letter = next(iter(sorted_max_letter_frequency_dict.keys()))
        offset_max_frequency_letter = to_python_char(char_diff('e', picked_max_frequency_letter))
        best_cipher.append(offset_max_frequency_letter)
        # print('')
    # print('')
    print(f'best_cipher: {best_cipher}')
    return best_cipher


def decrypt(encrypted_text_list, cipher_letters):
    result = ''
    print(f'decrypting: {encrypted_text_list}')
    for index in range(len(encrypted_text_list)):
        current_letter = encrypted_text_list[index]
        current_letter_cipher = cipher_letters[index % len(cipher_letters)]
        result += to_python_char(char_diff(current_letter_cipher, current_letter))
    return result


if len(sys.argv) < 4:
    print('Usage: app.py keyLength encrypted_text inputFile [inputFile]')
else:
    decrypt_result = decrypt(list(sys.argv[2].lower().replace(" ", "")),
                             find_e_letter_offsets(parse_input(int(sys.argv[1]), sys.argv[3:])))
    print(f'decrypt_result: {decrypt_result}')
