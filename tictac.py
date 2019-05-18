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
    if board.count(' ') == 1:
        return True
    else:
        return False

def insertLetter(letter, position):
    board[position] = letter

def makeMove(player):
        continueTurn = True
        while continueTurn:
            playerMove = input( player + ' select your move (1-9): ')
            try:
                playerMove = int(playerMove)
                if playerMove > 0 and playerMove < 10:
                    if isFreeSpace(playerMove):
                        insertLetter(player,playerMove)
                        continueTurn = False
                    else:
                        print("Please choose an empty space")
                else:
                    print("Please enter a number 1-9")
            except ValueError:
                print('Please enter a number 1-9')
           
                
def checkWinner(board,letter):
     #checks all 8 possible solutions to see if X or O is the winner
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
   #default each player to a certain letter
   player = 'X'
   player2 = 'O'
   
   #print blank board for user to choose a spot
   printBoard(board)
   
   while not (isBoardFull(board)):
 
       #if player2 didnt win, player1 goes
        if not checkWinner(board,player2):
            makeMove(player)
            printBoard(board)
        else:
            print(player2 + ' is the winner')
            break

        #if player1 didnt win, player2 goes
        if not checkWinner(board,player):
            makeMove(player2)
            printBoard(board)
        else:
            print(player + ' is the winner')
            break   

   #display full board and notify players it was a tie
   if isBoardFull(board):
    printBoard(board)
    print('Its a tie! The board is full')


main()






