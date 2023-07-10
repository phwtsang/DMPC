"""
This program implements the phone keypad encrytion strategy
"""
KEYPAD_DICT = {
        '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']
    }

def main():
    """
    This is main()
    """
    to_do = input('Encryption (e) or Decryption (d): ')
    if to_do == 'e':
        output = encrypt(input('Enter plain text: '))
    if to_do == 'd':
        output = decrypt(input('Enter encrypted text: '))

    print(output)

def encrypt(input_text):
    """
    apply keypad encryption
    """
    print(input_text)
    return 'encrypt'

def decrypt(input_text):
    """
    undo keypad encryption
    """
    list_words = input_text.split(' ')
    for word in words:
        list_text = list_words.split(',')
        word = ''
        for letter in list_text:
            key = letter[0]
            key_value = int(letter[2:])
            key_letter_list = KEYPAD_DICT[key]
            key_letter = key_letter_list[key_value - 1]
            print(key_letter)
            word +=key_letter
    return word

main()
