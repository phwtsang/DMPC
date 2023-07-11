def main():
    choice = input('Encrytion (e) or Decryption (d): ')
    if choice == 'e':
        input_text = input('Enter plaintext: ')
        output = encrypt(input_text)
    else:
        input_text = input('Enter cyphertext: ')
        output = decrypt(input_text)

def encrypt()