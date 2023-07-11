"""
implement the skip-over encryption algorithm
"""
def main():
    """
    implement the skip-over encryption algorithm
    """
    choice = input('Encrytion (e) or Decryption (d): ')
    if choice == 'e':
        input_text = input('Enter plaintext: ')
        output = encrypt(input_text)
        print(output)
    else:
        input_text = input('Enter cyphertext: ')
        output = decrypt(input_text)
        print(output)

def encrypt(input_text):
    """
    implement the skip-over encryption algorithm
    """
    output_text = ''
    input_list = input_text.split()
    print(input_list)
    for char in input_text:
        output_test +=char
    return output_text

def decrypt(input_text):
    """
    implement the skip-over encryption algorithm
    """
    return None

main()
