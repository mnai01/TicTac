import random
import copy

board = [' ' for x in range(10)]

####################################
# Title: printBoard(board)
# Description: Created a tic tac toe board with values from board array
####################################


def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

####################################
# Title: clearBoard(board)
# Description: Makes boared array values all blank
####################################


def clearBoard(board):
    # for loop that iteratres 10 times
    # to clear the whole board
    for i in range(10):
        board[i] = ' '

####################################
# Title: isFreeSpace(position)
# Description: find if specific position on the board is blank
# this represents an empty space
####################################


def isFreeSpace(position):
    # if the specified position on the board
    # is equal to ' '(which means the space is empty)
    # then this function will return true
    return board[position] == ' '

####################################
# Title: isBoardFul(Board)
# Description: Checks to see if the board arry is full
# if it is full then that means all spaces are taken
####################################


def isBoardFull(board):
    if board.count(' ') == 1:
        return True
    else:
        return False

####################################
# Title: insertLetter(letter, position)
# Description: places the letter X or O on specified position
# of the board array
####################################


def insertLetter(letter, position):
    # board at specifed position will now equal
    # the specifed letter
    board[position] = letter

####################################
# Title: playerMove(player)
# Description: allows the player to make a section
# on where they would like to place their next peice
####################################


def playerMove(player):
    continueTurn = True
    while continueTurn:
        # takes in the inpur of the user will only accept numbers from 1-9
        # since those are the spaced represented on the board
        playerMove = input(player + ' select your move (1-9): ')
        try:
            # convert the users input into an int
            playerMove = int(playerMove)
            # is playerMove is not 1-9 then skip this and ask the user
            # to select a num from 1-9
            if playerMove > 0 and playerMove < 10:
                # is the space selected by the player is not free
                # then ask player to select an empty space
                if isFreeSpace(playerMove):
                    # if it is a free spot then at the position use the players letter (X or O)
                    # and place it at the specified location
                    insertLetter(player, playerMove)
                    # end turn, exit the loop
                    continueTurn = False
                else:
                    print("Please choose an empty space")
            else:
                print("Please enter a number 1-9")
        except ValueError:
            print('Please enter a number 1-9')

####################################
# Title: checkWinner(board, letter)
# Description: used to see if the AI or player has won the game yet
####################################


def checkWinner(board, letter):
        # checks all 8 possible solutions to see if X or O is the winner
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

####################################
# Title: getOpenSpaces(board)
# Description: used to find available spaced
####################################


def getOpenSpaces(board):
    # list to be returned containing all available spaces
    availMoves = []
    # must enumerate board in order to iterate through it using indices and its values
    for x, letter in enumerate(board):
        if board[x] == ' ' and x != 0:
            availMoves.append(x)
    return availMoves

####################################
# Title: computerMove(completter)
# Description: used to execute the AI's move with there specified letter
#
####################################


def computerMove(completter):
    # sets possible moves to open spaces
    possibleMoves = getOpenSpaces(board)
    move = 0

# This loop checks each letter in all positions of the board chekcing which one is a winning solution.
# If it find a solution it will take that position to either win or block the opponent
# It then checks to see if the middle is open and takes that spot if it can
# If it cannot, it checks which corners are open and randomly picks one
# This has a time complexity of O(n^2) since we have to check both letters in all positions
    while True:
        # creates array, 1st index is the comps letter, 2nd index is the players letter
        if completter == 'X':
            testLetters = ['X', 'O']
        else:
            testLetters = ['O', 'X']

        # for loop to check with each letter
        for letter in (testLetters):
            # iterates throught each possible place on the board. X representing the space possibleMoves represeting all the possibilities
            # The first iteration is always the computers letter
            for x in possibleMoves:
                # makes copy of board
                boardCopy = copy.copy(board)
                # testing each space with x (being ether X or O)
                # sets each possible space in boardCopy to letter
                boardCopy[x] = letter
                # If check winner is true take that spot to ether win or block a win
                if checkWinner(boardCopy, letter):
                    move = x
                    insertLetter(completter, move)
                    print('Computer moved to space ' + str(move))
                    return
        # if middle position is possible, pick it
        if 5 in possibleMoves:
            if testLetters[1]:
                move = 5
                insertLetter(completter, move)
                print('Computer moved to space ' + str(move))
                break

        # If conor is available pick it.
        # This is O(n) since we have to loop through all of the possible solutions
        openCorners = []
        # for loop to iteratre through possibleMoves[]
        for x in possibleMoves:
            # if 1,3,7,9 is in possibleMoves add it to openCorners[]
            if x in [1, 3, 7, 9]:
                openCorners.append(x)
        # If openCorners is not empty
        if openCorners:
            # maybe make a function here to pick a better corner than random
            # move equals random corner
            move = random.choice(openCorners)
            # insert the move
            insertLetter(completter, move)
            print('Computer moved to space ' + str(move))
            break
        # if no corners
        else:
            openEdges = []
            # for loop to iteratre through possibleMoves[]
            for x in possibleMoves:
                # if 2,4,6,8 is in possibleMoves add it to openEdges[]
                if x in [2, 4, 6, 8]:
                    openEdges.append(x)
            # move equals random corner
            move = random.choice(openEdges)
            # Was missing
            # Fixed Skip when move to space 4
            # insert the move
            insertLetter(completter, move)
            print('Computer moved to space ' + str(move))
            break

####################################
# Title: gameOver()
# Description: Once there is a winner the game will be over and a rematch can be
# initialized if user selects Yes
####################################


def gameOver():
    while True:
        playAgain = input('Would you like to play again (y/n): ')
        # makes sure user enters valid responce
        if playAgain.upper() not in ('Y', 'N', 'YES', 'NO'):
            print("Enter yes or no (y/n)")
            continue
        else:
            # converts their responce to Capital and checks if its Y or YES
            if playAgain.upper() in ('Y', 'YES'):
                return True
            else:
                return False

####################################
# Title: Main()
# Description: Where all the testing/main execution goes bringing the whole project together
####################################


def main():
    # Set to false when user says they do not want to play anymore, other wise
    # the game is keep running
    gameState = True

    # Instructions for user displayed on the screen
    print('Use numbers 1-9 to place your X\'s or O\'s.')
    print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
    print('----------')
    print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
    print('----------')
    print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
    while gameState:
        while True:
            player = input('\nWould you like to be X or O: ')
            if player.upper() not in ('X', 'O'):
                continue
            else:
                player = player.upper()
                if player == 'X':
                    computer = 'O'
                    break
                else:
                    computer = 'X'
                    break
        while True:
            playerTurn = input('\nWould you like to go first? Y or N: ')

            # Checks to see if player wants to go first
            if playerTurn.upper() not in ('Y', 'N'):
                continue
            else:
                playerTurn = playerTurn.upper()
                if playerTurn == 'Y':
                    while not (isBoardFull(board)):

                        # if computer didnt win, the player goes
                        if not checkWinner(board, computer):  # player):
                            playerMove(player)
                            printBoard(board)
                        else:
                            print(computer + ' is the winner')
                            clearBoard(board)
                            gameState = gameOver()
                            break

                            # if the player didnt win, computer goes
                        if not checkWinner(board, player):  # computer):
                            if isBoardFull(board):
                                break
                            else:
                                computerMove(computer)
                                printBoard(board)
                        else:
                            print(player + ' is the winner')
                            clearBoard(board)
                            gameState = gameOver()
                            break
                else:
                    while not (isBoardFull(board)):

                        # if player1 didnt win, the computer goes
                        if not checkWinner(board, player):

                            if isBoardFull(board):
                                break
                            else:
                                computerMove(computer)
                                printBoard(board)
                        else:
                            print(player + ' is the winner')
                            clearBoard(board)
                            gameState = gameOver()
                            break
                            # if the computer didnt win, player1 goes
                        if not checkWinner(board, computer):
                            if isBoardFull(board):
                                break
                            else:
                                playerMove(player)
                                printBoard(board)
                        else:
                            print(computer + ' is the winner')
                            clearBoard(board)
                            gameState = gameOver()
                            break
            break
        # display full board and notify players it was a tie
        if isBoardFull(board):
            printBoard(board)
            print('Its a tie! The board is full')
            clearBoard(board)
            gameState = gameOver()


main()
