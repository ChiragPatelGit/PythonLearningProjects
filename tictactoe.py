from random import randrange

global FreeFields
FreeFields = []


def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #

    border = 3*("+" + 8*"-") + "+"
    topPadding = 3*("|" + 8*" ") + "|"
    SidePadding = "|" + 3*" "

    print(border)
    for row in range(len(board)):
        print(topPadding)
        for col in range(len(board[row])):

            #item at the field location
            item = str(board[row][col]) + 3*" "

            print(SidePadding, item, end="")
        print("|")  # character at the end of the row
        print(topPadding)
        print(border)


def EnterMove(board):

    #
    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision
    #

    UserMove = input(
        "Enter your move as a integer greater than 0 and less than 10: ")

    if int(UserMove) < 1 or int(UserMove) > 9:
        EnterMove(board)

    for row, col in FreeFields:  # traversing the list of empty fields
        # if the field is the number entered
        if board[row][col] == int(UserMove):
            board[row][col] = "O"  # assign O to that field
            DisplayBoard(board)
            return True  # True when a move was possible


def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    del FreeFields[:]  # start with a empty FreeFields list

    for row in range(len(board)):
        for col in range(len(board[row])):
            item = board[row][col]
            if(item != "X" and item != "O"):  # check for empty fields
                newTuple = (row, col)  # empty field indicies
                FreeFields.append(newTuple)

    print("FreeFields: ", FreeFields)

    return len(FreeFields) > 0  # True if there are any empty fields


def RowCount(SignSpots, index):
    count = 0
    for row, col in SignSpots:
        if row == index:
            count += 1
    return count


def ColCount(SignSpots, index):
    count = 0

    print("col", index)
    for row, col in SignSpots:
        if col == index:
            count += 1
    return count


def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #

    SignSpots = []  # list of fields which have the sign
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == sign:  # where on the board the sign matches
                placeTuple = row, col  # location of the sign on board
                # list of location of the sign on the board
                SignSpots.append(placeTuple)

        Won = False
        if len(SignSpots) > 2:
            SignSpots.sort()
            print("sign", sign)
            print("SignSpots", SignSpots)
            for row, col in SignSpots:
                if RowCount(SignSpots, row) == 3:
                    Won = True
                    break
                if ColCount(SignSpots, col) == 3:
                    Won = True
                    break
                if row == 1 and col == 1:
                    print("row", row, "col", col)
                    if ((0, 0) and (2, 2)) in SignSpots:
                        Won = True
                        break
                    if ((2, 0) and (0, 2)) in SignSpots:
                        Won = True
                        break

            return Won


def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #

    if MakeListOfFreeFields(board) == False:
        return
    print("FreeFields are", FreeFields)
    RandomSpot = randrange(len(FreeFields))
    print("RandomSpot", RandomSpot)
    print(len(FreeFields))
    tup = FreeFields[RandomSpot]  # find a random available field on the board
    # assign index values based on the available field found
    row, col = tup[0], tup[1]
    board[row][col] = "X"  # put an x at the field chosen
    DisplayBoard(board)  # display board

    return


board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

board[1][1] = "X"
DisplayBoard(board)
#MakeListOfFreeFields(board)
Winner = None

while MakeListOfFreeFields(board):

    EnterMove(board)  # prompts for the user's move

    if VictoryFor(board, "O") == True:
        print("O won")
        Winner = "O"
        break

    DrawMove(board)

    if VictoryFor(board, "X") == True:
        print("X won")
        Winner = "X"
        break


if Winner == None:
    print("No one won")
