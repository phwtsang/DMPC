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
    input_len = len(input_text)
    output_list = list(input_text)
    input_list = list(input_text)
    #print(input_list)
    for i,char in enumerate(input_list):
        list_index = i*int(skip_key)%input_len
        #print(i, list_index)
        output_list[list_index] = char
    return ''.join(output_list)

def decrypt(input_text, skip_key):
    """
    implement the skip-over decryption algorithm
    """
    input_len = len(input_text)
    output_list = list(input_text)
    input_list = list(input_text)
    #print(input_list)
    for i,char in enumerate(input_list):
        list_index = i*(int(skip_key)-1)%input_len
        #print(i, list_index)
        output_list[list_index] = char
    return ''.join(output_list)

main()
