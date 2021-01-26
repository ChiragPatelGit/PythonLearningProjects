import getpass

def UserInput():
    """
        This function prompts the user for the text to encrypt along with the
        shift amount for the encryption.
    """
    Message =""
    while Message.lstrip() =="" :
        # prompts user for the plaintext message and repeats prompt if nothing is typed besides space and enter
        Message = getpass.getpass("Enter a message to encrypt: ") # accepts user input but in hidden text
                
            

    ChosenShift = 0

    while int(ChosenShift) < 1 or int(ChosenShift) > 25: # loop until the user chooses a shift between 1 and 25
        ChosenShift=input("Enter the amount to shift between 1  and 25: ")
        if ChosenShift.isdigit() == False:
            ChosenShift = 0 # if the user input is not a number then reassign the shift amount to zero 
                            # to restart the iteration

    return Message, int(ChosenShift)


def CipherRun():
    """
    This function longs the actual logic to shift the text by the user chosen shift amount
    """
    ChosenData = UserInput() # retieving user input
    Msg, Shift = ChosenData # assigning the message text and shift amount
    Cipher = "" # placeholder for the encrypted text

    for char in Msg:
        if char.isalpha(): # checks if the charcter is a letter
            code = ord(char) + Shift # shifts the ordinal position by the requested shift amount
            if code > ord('z') and char.islower()==True: # if the char is lowercase and shift is beyound the letter z
                code = ord('a') + ((code-ord('z'))-1) # wrap back around to the beginning but take account that you are starting by 1 shift
            elif code > ord('Z') and char.isupper() == True: # if the char is upppercase and shift is beyound the letter Z
                code = ord('A') + ((code -ord('Z'))-1) # wrap back around to the beginning but take account that you are starting by 1 shift
            Cipher += chr(code) # add the character you land on b/c of the shift to the Cipher text
        else:
            Cipher +=char # add the non letter character to the cipher text
    print(Cipher)




     

CipherRun()