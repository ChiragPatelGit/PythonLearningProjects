#Caesar Cipher

Choice = input("Would you like to encrypt or decrypt a message:")

if Choice.upper() == "ENCRYPT":

    message = input("Enter your message: ")
    cipher = ''
    for char in message:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char)+1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    print(cipher)

elif Choice.upper() == "DECRYPT":
    cipher =  input ("Enter the encrypted message:")
    plaintext = ''
    
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) -1
        if code < ord('A'):
            code = ord('Z')
        plaintext += chr(code)
    
    print(plaintext)

