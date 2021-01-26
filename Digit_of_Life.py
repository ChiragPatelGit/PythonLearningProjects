def UserPrompt():
    """
    This function asks for the User's Birthdate and returns it
     in string from once it is validated.

    """

    Bdate = input("Enter you birthday in the format of MMDDYYYY: ")

    if Bdate.isdigit() and len(Bdate) == 8:
        return Bdate
    else:
        print("That is not a valid Birthdate.")
        UserPrompt()


def CalcDateDigit(NumToReduce):
    """
    This function calculates the single digit representation of a date

    """
    resultNum = 0 # placeholder for the sum of all the digits in the number

    for char in NumToReduce:
        # add each digit in the NumToReduce string to the resultNum
        resultNum += int(char)

    resultNumStr = str(resultNum) # converts the resultNum to a string 
    
    if len(resultNumStr) > 1:
        # if the number of digits in the resultNum is greater than run then re run the function with the new number, resultNumStr
        return CalcDateDigit(resultNumStr)

    return resultNumStr
    
    



Birthday = UserPrompt()

LifeDigit=CalcDateDigit(Birthday)

print(f"The Digit of Life is {LifeDigit}")


    

