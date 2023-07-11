def main():
    choice = input('Encrytion (e) or Decryption (d): ')
    if choice == 'e':
        output = encrypt(choice)
    else:
        choice == 'd':
        output = decrypt(choice)