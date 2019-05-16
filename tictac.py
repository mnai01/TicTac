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



def main():
    player = input("X or O: ")

    while not (isBoardFull(board)):
        printBoard(board)
        makeMove(player)

    print('board is full')


main()






