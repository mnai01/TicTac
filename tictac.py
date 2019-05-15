board = [' ' for x in range(10)]


def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def getMove():
    for x in range(10):
        printBoard(board)
        playerMove = int(input("Select your move: "))

        if playerMove < 1 or playerMove > 9:
            print("move out of range: ")
            continue

        if board[playerMove] != ' ':
            print("space is already taken")
            continue
        else:
            board[playerMove] = 'x'


getMove()
