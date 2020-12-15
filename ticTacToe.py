#board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

#def drawGrid(board):
#    print("-------------------")
#    for i in range(3):
#        print("   |", end="")
#        for j in range(3):
#            print(f" {board[i][j]} |", end="")
#        if (i < 2):
#            print("\n   -------------")
#        else:
#            print("\n-------------------")


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
    value = 0
    while value not in range(1, 10):
        value = int(input(f"{player}, where to place your move? "))

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

# int main()
if __name__ == '__main__':
    
    # Store number of moves played to quit
    movesPlayed = 0
    # check whether a player has won
    wonState = False
    # Start the game by asking for player 1 to take a turn
    while True:
        turn = input("Player 1, choose between X and O: ")
        if (turn == 'X' or turn == 'O'):
            break

    while not wonState:
        # Draw the board they playing on
        drawGrid(board)
        # Get where the current player wants to put his piece
        value = askInput(turn)
        # Mark where the player wants to get marked
        board[value - 1] = turn
        # Count the number of times the game has been played
        movesPlayed += 1
        # Check if any player has won
        wonState = determineWin(board, movesPlayed)
        # Swap turn
        turn = swapTurn(turn)

    turn = swapTurn(turn)

    print(f"\n\nGAME WON by {turn}".format(swapTurn(turn)))
    drawGrid(board)
