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
    if board.count(' ') <= 1:
        return True
    else:
        return False

def insertLetter(letter, position):
    board[position] = letter

def makeMove(player):
        continueTurn = True
        while continueTurn:
            playerMove = input( player + ' select your move: ')
            try:
                playerMove = int(playerMove)
                if playerMove > 0 and playerMove < 10:
                    if isFreeSpace(playerMove):
                        insertLetter(player,playerMove)
                        continueTurn = False
                    else:
                        print("space is already taken")
                else:
                    print("Move is out of range")
            except ValueError:
                print('not a number')
           
                
def checkWinner(board,letter):
        # should not be x, maybe we will add a parameter so we can call the function once with O and once with X to check which letter wins
    if((board[1] ==letter and board[2] ==letter and board[3] ==letter) or
       (board[4] ==letter and board[5] ==letter and board[6] ==letter) or
        (board[7] ==letter and board[8] ==letter and board[9] ==letter) or

        (board[1] ==letter and board[4] ==letter and board[7] ==letter) or
        (board[2] ==letter and board[5] ==letter and board[8] ==letter) or
        (board[3] ==letter and board[6] ==letter and board[9] ==letter) or

        (board[1] ==letter and board[5] ==letter and board[9] ==letter) or
        (board[3] ==letter and board[5] ==letter and board[7] ==letter)):
        return True            



def main():
   player = 'X'
   player2 = 'O'
   printBoard(board)
   
   while not (isBoardFull(board)):
       makeMove(player)
       printBoard(board)

       if checkWinner(board,player):
           print('Game over, ' + player + ' is the')
           break
       makeMove(player2)
       printBoard(board)

       if checkWinner(board,player2):
           print('Game over, ' + player2 + ' is the winner')
           break
main()






