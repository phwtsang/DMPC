"""
permutation encryption
"""
def main():
    """
    main function
    """
    choice = input('Encryption(e) or Decryption(d): ')
    if choice == 'e':
        print(perm_encrypt())
    elif choice == 'd':
        print(perm_decrypt())
    else:
        print("I don't understand your choice.")

def perm_encrypt():
    """
    perm_encrypt function
    """
    input_text = input('Enter plaintext: ')
    encrypt_key = input('Enter encryption key: ')
    key_len = len(encrypt_key)
    input_list = list(input_text)

def perm_decrypt():
    """
    perm_decrypt function
    """
    input_text = input('Enter ciphertext: ')
    encrypt_key = input('Enter encryption key: ')
    output_list = []
    key_list = list(encrypt_key)
    key_len = len(encrypt_key)
    input_list = list(input_text)
    for i, num in enumerate(key_list):


main()
