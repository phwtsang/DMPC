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
        skip_key = input('Enter Skip Key: ')
        output = encrypt(input_text, skip_key)
        print(output)
    else:
        input_text = input('Enter cyphertext: ')
        skip_key = input('Enter Skip Key: ')
        output = decrypt(input_text, skip_key)
        print(output)

def encrypt(input_text, skip_key):
    """
    implement the skip-over encryption algorithm
    """
    output_text = ''
    output_list = list(input_text)
    input_list = list(input_text)
    #print(input_list)
    for i,char in enumerate(input_list):
        list_index = (i*skip_key)%11
        print(i, list_index)
        output_list[list_index] = char
    return output_text.join(output_list)

def decrypt(input_text, skip_key):
    """
    implement the skip-over encryption algorithm
    """
    output_text = input_text
    return output_text

main()
