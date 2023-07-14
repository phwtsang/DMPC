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
    output_list = list(input_text)
    key_list = list(encrypt_key)
    key_len = len(encrypt_key)
    input_list = list(input_text)
    #print(input_list)
    for i, char in enumerate(input_list):
        i_mod = i%key_len
        i_quotient = i//key_len
        #print(i, i_mod, int(key_list[i_mod])-1)
        output_list[i] = input_list[key_len*i_quotient+int(key_list[i_mod])-1]
    return ''.join(output_list)


main()
