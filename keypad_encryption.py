def main():
    """
    This program implements the phone keypad encrytion strategy
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
        ouput = decrypt(input('Enter encrypted text: '))

def encrypt(input_text):
    print(input_text)

def decrypt(input_text):
    print(input_text)