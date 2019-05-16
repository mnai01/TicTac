board = [' ' for x in range(10)]

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def isFreeSpace(position):
    return board[position] == ' '
       
def isBoardFull(board):
    if board.count(' ') < 1:
        return True
    else:
        return False

def insertLetter(letter, position):
    board[position] = letter

def makeMove(player):
        continueTurn = True
        while continueTurn:
            playerMove = input("Select your move: ")
            try:
                playerMove = int(playerMove)

                if playerMove > 1 or playerMove < 10:
                    if isFreeSpace(playerMove):
                        insertLetter(player,playerMove)
                        continueTurn = False
                    else:
                        print("space is already taken")
                else:
                    print("Move is out of range")
            except:
                print('not a number')
           
                
            



def main():
    
    numberOfMoves = 0
    player = input("X or O: ")

    while not (isBoardFull(board)):
        printBoard(board)
        makeMove(player)

    print('board is full')


main()
