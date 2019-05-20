import random
import copy

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

def playerMove (player):
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
 if ((board[1] == letter and board[2] == letter and board[3] == letter) or
  (board[4] == letter and board[5] == letter and board[6] == letter) or
  (board[7] == letter and board[8] == letter and board[9] == letter) or

  (board[1] == letter and board[4] == letter and board[7] == letter) or
  (board[2] == letter and board[5] == letter and board[8] == letter) or
  (board[3] == letter and board[6] == letter and board[9] == letter) or

  (board[1] == letter and board[5] == letter and board[9] == letter) or
  (board[3] == letter and board[5] == letter and board[7] == letter)):
   return True
 else:
   return False


def getOpenSpaces(board):
 #list to be returned containing all available spaces
 availMoves = []

 #must enumerate board in order to iterate through it using indices and its values
 for x,letter in enumerate(board):
  if board[x] == ' ' and x != 0:
    availMoves.append(x)
 return availMoves


def computerMove(completter):
 possibleMoves = getOpenSpaces(board)
 move = 0

 while True:
  for letter in ('X','O'):
   for x in possibleMoves:
    boardCopy = copy.copy(board)
    boardCopy[x] = letter
    if checkWinner(boardCopy,letter):
     move = x
     insertLetter(completter,move)
     print('Computer moved to space ' + str(move))
     return

  if 5 in possibleMoves:
   move = 5
   insertLetter(completter,move)
   print('Computer moved to space ' + str(move))
   break

  openCorners = []
  for x in possibleMoves:
   if x in [1,3,7,9]:
    openCorners.append(x)
  move = random.choice(openCorners)
  #maybe make a function here to pick a better corner than random
  insertLetter(completter,move)
  print('Computer moved to space ' + str(move))
  break

  



def main():
 print('Use numbers 1-9 to place your X\'s or O\'s.')
 print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
 print('----------')
 print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
 print('----------')
 print(' ' + '7'+ ' | ' + '9' + ' | ' + '9')
 while True:
    player = input('\nWould you like to be X or O: ')    
    if player.upper() not in ('X','O'):
        continue
    else:
        player = player.upper()
        if player =='X':
            computer = 'O'
            break
        else:
            computer = 'X'
            break

 printBoard(board)

 while not (isBoardFull(board)):
       #if the computer didnt win, player1 goes
        if not checkWinner(board,computer):
            playerMove(player)
            printBoard(board)
        else:
            print(computer + ' is the winner')
            break

        #if player1 didnt win, the computer goes
        if not checkWinner(board,player):
            if isBoardFull(board):
                break
            else:    
                computerMove(computer)
                printBoard(board)
        else:
            print(player + ' is the winner')
            break   

   #display full board and notify players it was a tie
 if isBoardFull(board):
    printBoard(board)
    print('Its a tie! The board is full')



main()






