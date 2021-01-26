def MultipleDigitOccurrences(NbrStr):
    """
        This function checks of a given digit (between 1 and 9 ) occurs more 
        than once in a Number String
    """
    duplicate = False  # holds the condition of if any digit is a dulplicate  
    for i in range(1,10):
        if NbrStr.count(str(i)) > 1:
            duplicate = True
            break
    return duplicate


Number = input("Enter  a number string: ")

Dups = MultipleDigitOccurrences(Number)

print(Dups)
    