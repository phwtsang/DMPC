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
    word = ''
    for letter in input_text:
        for key, val in KEYPAD_DICT.items():
            if letter in val:
                print(key)
                for i, number in enumerate(val):
                    if
                word = word + key + ':' + 'i' + ','

    print(input_text)
    return word

def decrypt(input_text):
    """
    undo keypad encryption
    """
    sentence = ''
    list_words = input_text.split(' ')
    #print('list_words', list_words)
    for list_word in list_words:
        list_text = list_word.split(',')
        #print('list_text', list_text)
        word = ''
        for letter in list_text:
            key = letter[0]
            #key_value = int(letter[2:])
            key_letters = KEYPAD_DICT[key]
            key_value = int(letter[2:])%len(key_letters)
            key_letter = key_letters[key_value - 1]
            #print(key_letter)
            word +=key_letter
        sentence +=' '
        sentence +=word
    return sentence

main()
