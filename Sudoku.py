def VerifyRowValue(row):
    """
    This verifies if the row is valid or not.
    """

    validRow = True
    
    if row.isdigit() == False:
        #The row is not valid if it contains anything besides digits
        validRow = False

    if len(row) != 9:
        # The row is invalid if its length is not exactly nine characters long
        validRow = False

    for char in row:
        if char == "0":
            # The row is invalid if zero exists in the row.
            validRow = False

    return validRow
    
def DisplayBoard(BoardMatrix):
    """
        Displays populated board with boarders
    """
    hboarder = "-" * 37
   
    padding = "|" + "   |" * 8 + "   |"

    for i in range(len(BoardMatrix)):
        
        print(hboarder)
        print(padding)
        for j in range(len(BoardMatrix[i])):
            cellNbr = BoardMatrix[i][j]
            print(f"| {cellNbr} ", end="")
        
        print("|")
        print(padding)
    print(hboarder)
    
                
    
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


def VerticalDupCheck(Board):
   """
    This function checks if there are duplicate digits for each
    vertical number line
   """
   dups = False
   VerticalNbrLine = "" # temp var to hold the digits for each line
   j = 0 # the column index 
   while j < 9 and dups == False:
       # while there column index is not out greater than 8 
       # and no duplicates have been found so far

    for i in range(9): # traverses each row 
        # the column index remains the same, but is row index is incremented
        VerticalNbrLine += Board[i][j]

    if MultipleDigitOccurrences(VerticalNbrLine) == True:
        #if a digit duplicate is found in the Vertical Number line
        dups = True
        
    j += 1 # increments the column indes

    return dups
      
def horizontalDupCheck(Board):
    """
        Checks if there are any duplicate digits in any 
        horizontal number 
    """
    hDups = False # holds the determination of a duplicate
    for NbrStr in Board:
        # traverses each row in the board 
        hDups = MultipleDigitOccurrences(NbrStr)

        if hDups == True:
            break

    return hDups    
    


def checkDupIn3x3(board,x,y):
    """
    The function checks for duplicate numbers on
     any 3x3 grid on the board

    """
    NbrRepeats = False
    NbrsInGrid ="" # placeholder the numbers in the 3x3 grid instance

    for i in range(x,x+3,1):
        #travers the row starting at index x 
        # and ending at one less than x+3
        for j in range(y,y+3,1):
            # traverses the columns start at index y 
            # and ending at one less than y+3
            NbrsInGrid += board[i][j] #add the digit to the number string
    
    NbrRepeats = MultipleDigitOccurrences(NbrsInGrid) # check to see if any digits in the number string repeat
    
    if NbrRepeats == False:
        # if no digit repeats in the current 3x3 grid
        if y+3 < len(board[x]):
            # move horizontally to the next 3x3 grid
            return checkDupIn3x3(board,x, y+3)
        if y+3 == len(board[x]) and x+3 < len(board):
            # if you are at the horizontal end of the board
            # move down to the next 3x3 grid starting at the first 
            # column
            return checkDupIn3x3(board,x+3, 0)

    return NbrRepeats

    


def UserPrompt():
    """
        This function will get the user's board values and
        put them into a 2d list, which will be returned.
        If the input is invalid then the function will be recalled,
        until valid input is entered.
    """
    UserExit = False # to determine if the user does not want to play anymore
    Board = [[] for i in range(9)] # the sudoku board
    RowValue = "" # placeholder for when each row is being inputted
    print("Welcome to Sudoku")
    print("There must be only 9 rows with nine digits only.")
    print("Type end to end the game")
    print("Enter the board values line by line now:")

    for i in range(len(Board)):
        # traverse each row in the board to populate it based on user input
        RowValue = input()
        #print(f"Row {i+1} = {RowValue}")
        if RowValue.upper() == ("END"):
            # if the user wants to exit the program
            UserExit = True
            break
        else:
            while VerifyRowValue(RowValue) == False:
            # while valid row data is not inputed
                print("Please enter a valid row")
                RowValue = input()

        Board[i] = RowValue # once row data has been verified, assign it to the board
        

    return Board, UserExit



UserValues = UserPrompt()

UserBoard = UserValues[0]
UserExit = UserValues[1]


if UserExit == True:
    print("GoodBye")
else:
    dups = False

    vDup = VerticalDupCheck(UserBoard) # if any vertical numbers have duplicate digits
    hDup = horizontalDupCheck(UserBoard)   # if any horizontal numbers have duplicate digits
    sub3x3Dup = checkDupIn3x3(UserBoard,0,0) # if any of the 3x3 tiles (aka sub-squares) have duplicate digits

    print("The User's board is")
    DisplayBoard(UserBoard)


    # print(f"vDup: {vDup}")
    # print(f"hDup: {hDup}")
    # print(f"sub3x3Dup: {sub3x3Dup}")
    if vDup or hDup or sub3x3Dup:
        print("No, you don't have a valid Sudoku ")
    else:
        print("Yes, you do have a valid Sudoku")

