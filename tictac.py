board = [' ' for x in range(10)]


def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def getMove():
    for x in range(10):

        # board is printed then it checks for winner (prefered order of execution)
        printBoard(board)

        # if true print then exit game
        if checkWinner():
            print("You are the winner")
            exit()

        # prompts user for next move
        playerMove = int(input("Select your move: "))

        # checks users move to see if its a valid value
        if playerMove < 1 or playerMove > 9:
            print("move out of range: ")
            continue

        # checks users move to see if its already taken.
        if board[playerMove] != ' ':
            print("space is already taken")
            continue
        else:
            board[playerMove] = 'x'


def checkWinner():
        # should not be =='x', maybe we will add a parameter so we can call the function once with O and once with X to check which letter wins
    if((board[1] == 'x' and board[2] == 'x' and board[3] == 'x') or
       (board[4] == 'x' and board[5] == 'x' and board[6] == 'x') or
        (board[7] == 'x' and board[8] == 'x' and board[9] == 'x') or
        (board[1] == 'x' and board[5] == 'x' and board[9] == 'x') or
        (board[7] == 'x' and board[5] == 'x' and board[3] == 'x') or
        (board[1] == 'x' and board[4] == 'x' and board[7] == 'x') or
        (board[2] == 'x' and board[5] == 'x' and board[8] == 'x') or
            (board[3] == 'x' and board[6] == 'x' and board[9] == 'x')):
        return(True)


getMove()
checkWinner()
