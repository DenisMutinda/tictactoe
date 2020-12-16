#include <stdio.h>
#include <stdbool.h>    // All this for just Boolean data type.

void printBoard(int movesPlayed, char turn);
char turnDetermine(char turn);   // Flip the turn.
void state(int playerChoice, char turn);
bool winner(int movesPlayed);

char board[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};    // A 9-Element array for the board.

int main(){
  char turn;
  int playerChoice, movesPlayed = 1;
  bool gameWon = false;

  printf("Player Numero Uno is either X's or O's: ");
  scanf(" %c", &turn);
  getchar();    // Consume the 'Return'

  while(!gameWon){
    clrscr();   // Clear the screen
    printBoard(movesPlayed, turn);
    printf("What square to fill with an %c sire? ", turn);
    scanf("%i", &playerChoice);
    getchar();    // Consume the 'Return'
    state(playerChoice, turn);
    movesPlayed++;
    gameWon = winner(movesPlayed);
    turn = turnDetermine(turn); // Flip turn each round.
  }

  printf("Ciao\n");
  return(0);
}

void printBoard(int movesPlayed, char turn){
  for( int i = 0, place = 0; i < 3; i++, place +=3 ){
    printf("- - - - - - -\n");
    printf("| %c | %c | %c |\n", board[place], board[place + 1], board[place + 2]);
  }
  printf("- - - - - - -\n");

  printf("Move: %i\tTurn: %c\n", movesPlayed, turn);
}

char turnDetermine(char turn){
  if (turn == 'X'){
    return 'O';
  } else {
    return 'X';
  }
}

void state(int playerChoice, char turn){
  playerChoice -= 1;

  // If said square is not filled by either X or O, step inside loop.
  // Inside loop, it is filled with the character passed to this routine.
  if ( board[playerChoice] != 'X' || board[playerChoice] != 'O' ){
    board[playerChoice] = turn;
  }
}

bool winner(int movesPlayed){

  if ( board[0] == board[1] && board[1] == board [2]) {
    return true;
  }

  if( board[0] == board[3] && board[3] == board[6] ) {
    return true;
  }

  if ( board[0] == board[4] && board[4] == board[8] ){
    return true;
  }

  if( board[3] == board[4] && board[4] == board[5]) {
    return true;
  }

  if ( board[1] == board[4] && board[4] == board[7]) {
    return true;
  }

  if (board[6] == board[4] && board[4] == board[2]){
    return true;
  }

  if (board[6] == board[7] && board[7] == board[8]){
    return true;
  }

  if (board[2] == board[5] && board[5] == board[8]){
    return true;
  }

  if (movesPlayed == 10){
    return true;
  }

  return false;
}
