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
    input_list = list(input_text)
    print(input_list)
    for i,char in enumerate(input_text):
        output_text[i] = char + output_text
    return output_text

def decrypt(input_text):
    """
    implement the skip-over encryption algorithm
    """
    output_text = input_text
    return output_text

main()
