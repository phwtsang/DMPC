def main():
    """
    implement the skip-over encryption algorithm
    """
    choice = input('Encrytion (e) or Decryption (d): ')
    if choice == 'e':
        input_text = input('Enter plaintext: ')
        output = encrypt(input_text)
    else:
        input_text = input('Enter cyphertext: ')
        output = decrypt(input_text)

def encrypt(input_text):
    """
    implement the skip-over encryption algorithm
    """
    pass

def decrypt(input_text):
    """
    implement the skip-over encryption algorithm
    """
    pass