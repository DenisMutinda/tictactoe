import random # For picking random move for AI

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def drawGrid(board):
    print("---------------------")
    print(f"  | {board[0]} | {board[1]} | {board[2]} |")
    print("---------------------")
    print(f"  | {board[3]} | {board[4]} | {board[5]} |")
    print("---------------------")
    print(f"  | {board[6]} | {board[7]} | {board[8]} |")
    print("---------------------")

# Ask player for square number to play.
# The number is checked to ascertain that it is within the range of 1 - 9.
def askInput(player):
    while True: 
        value = int(input(f"{player}, where to place your move? "))
        if (value >=1 and value <= 9):
            break

    return value

# Determine if somebody has won.
# Moves played have exceeded 9, then it is a stalemate.
def determineWin(board, movesPlayed):
    #pass
    if movesPlayed >= 9:
        return True
    # Check individual squares here.
    elif board[0] == board[1] and board[1] == board[2]:
        return True
    elif board[3] == board[4] and board[4] == board[5]:
        return True
    elif board[6] == board[7] and board[7] == board[8]:
        return True
    elif board[0] == board[3] and board[3] == board[6]:
        return True
    elif board[1] == board[4] and board[4] == board[7]:
        return True
    elif board[2] == board[5] and board[5] == board[8]:
        return True
    elif board[0] == board[4] and board[4] == board[8]:
        return True
    elif board[2] == board[4] and board[4] == board[6]:
        return True
    else:
        return False

# Ensure turn taking in the game
def swapTurn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'

# Check to ensure people are not overwriting each other
def moveValidity(position, turn):
    # Mark where the player wants to play as long as it has not already being filled.
    if board[position] == 'X' or board[position] == 'O':
        return False
    # Default Case
    board[position] = turn
    return True

# In case the player has no friends ;(
def aiPlayer(movesPlayed, wonState):
    # Ask human for input
    while True:
        humanSymbol = input("Human, choose between X and O: ")
        if (humanSymbol == 'X' or humanSymbol == 'O'):
            turn = humanSymbol
            break

    while not wonState:
        #Draw board
        drawGrid(board)

        #Get where hooman wants to play
        while True:
            if turn == humanSymbol:
                value = askInput(turn)
                value -= 1
                played = moveValidity(value, turn)
                if played == True:
                    break
            else:
                #Generate random number within grid range for Computer to play
                value = random.randint(0, 8)
                played = moveValidity(value, turn)
                if played == True:
                    print("Computer played {moveNumber}".format(moveNumber = value+1))
                    break

        # Count the number of times the game has been played
        movesPlayed += 1
        # Check if any player has won
        wonState = determineWin(board, movesPlayed)
        # Swap turn
        turn = swapTurn(turn)

    turn = swapTurn(turn)

    if movesPlayed < 9:
        print(f"\n\nGAME WON by {turn}".format(swapTurn(turn)))
        drawGrid(board)
    else:
        print("\n\nGAME ended in a STALEMATE")
        drawGrid(board)
    
# In case player has company
def twoPlayer(movesPlayed, wonState):
    # Start the game by asking for player 1 to take a turn
    while True:
        turn = input("Player 1, choose between X and O: ")
        if (turn == 'X' or turn == 'O'):
            break

    while not wonState:
        # Draw the board they playing on
        drawGrid(board)
        
        # Get where the current player wants to put his piece
        while True:
            value = askInput(turn)
            value -= 1
            played = moveValidity(value, turn)
            if played == True:
                break

        # Count the number of times the game has been played
        movesPlayed += 1
        # Check if any player has won
        wonState = determineWin(board, movesPlayed)
        # Swap turn
        turn = swapTurn(turn)

    turn = swapTurn(turn)

    if movesPlayed < 9:
        print(f"\n\nGAME WON by {turn}".format(swapTurn(turn)))
        drawGrid(board)
    else:
        print("\n\nGAME ended in a STALEMATE")
        drawGrid(board)

# int main()
if __name__ == '__main__':
    
    # Store number of moves played to quit
    movesPlayed = 0
    # check whether a player has won
    wonState = False

    # I want to choose between 1p and 2p
    while True:
        playerNumbers = int(input("How many players will be playing, 1 or 2? "))
        if playerNumbers == 1:
            aiPlayer(movesPlayed, wonState)
            break
        elif playerNumbers == 2:
            twoPlayer(movesPlayed, wonState)
            break


