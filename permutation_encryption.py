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
    pass

def perm_decrypt():
    """
    perm_decrypt function
    """
    pass

main()
