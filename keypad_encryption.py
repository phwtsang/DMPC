"""
This program implements the phone keypad encrytion strategy
"""
def main():
    """
    This is main()
    """
    keypad_dict = {
        2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'],
        5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'],
        8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']
    }

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
    print(input_text)
    return 'decrypt'

main()
