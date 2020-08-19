# Prints board
def printGame(board):

  print(board[0],"|",board[1],"|",board[2])
  print("-","-","-","-","-")
  print(board[3],"|",board[4],"|",board[5])
  print("-","-","-","-","-")
  print(board[6],"|",board[7],"|",board[8])

# Gets random player and symbol
def random():

  import random
  # to get a random player between 1 and 2
  player1 = random.randint(1,2)
  player2 = random.randint(1,2)


 # to get a random symbol between 1 and 2
  symbol1 = random.randint(1,2)
  symbol2 = random.randint(1,2)

  while(player2 == player1):
    player2 = random.randint(1,2)

  while(symbol2 == symbol1):
    symbol2 = random.randint(1,2)

  if(symbol1 == 1):
    symbol1 = "X"
  if(symbol1 == 2):
    symbol1 = "O"
  if(symbol2 == 1):
    symbol2 = "X"
  if(symbol2 == 2):
    symbol2 = "O"

  return player1, player2, symbol1, symbol2

# Checks if board is full by going through the board and checking if its all Xs and Os
def boardFull(boardA):
  
  for i in range(9):
    if(boardA[i] != "O") or (boardA[i] != "X"):
      return False
    else:
      return True
    
      
# Checks if a player won
def testWin(board):

   if(board[0] == board[1] == board[2]) != True and (board[3] == board[4] == board[5]) != True and (\
board[6] == board[7] == board[8]) != True and (board[0] == board[3] == board[6]) != True and (board[1]  == board[4] == board[7]) != True and (board[2] == board[5] == board[8]) != True and (board[0] == board[4] == board[8]) != True and (board[6] == board[4] == board[2]) != True:
     return True
   else:
     return False
   
# Plays game
def game(player1, player2, symbol1, symbol2, board):

# Player 1 when first, input where to go on tic tac toe board and tests to see if there is a winner
  winner = 0
  numTurns = 0
  while(winner == 0):
    if(player1 == 1):
      if(testWin(board) == True):
        print("Player 1, it is your turn ")
        turn = int(input("Enter number between 0-8 "))
        while(turn < 0) or (turn > 8) or (board[turn] == "X") or (board[turn] == "O"):
          turn = int(input("Enter number between 0-8 or enter number that isn't taken already "))
          

        board[turn] = symbol1
       
        printGame(board)
        numTurns += 1
# Tests if game was a tie        
        if(numTurns == 9) and (testWin(board) == True):
          print("Its a Tie")
          winner = 3
          play = input("Do you want to play again? 0/1 no/yes ")
          return play
      else:
        winner = 1
        print("Winner is Player 2")  
        play = input("Do you want to play again? 0/1 no/yes ")
        return play

              
            
             
# Player 2, input where to go on tic tac toe board and tests to see if there is a winner
      
      if(winner != 1) and (winner != 3):
        if(testWin(board) == True):
          print("Player 2, it is your turn ")
          turn = int(input("Enter number between 0-8 "))
          while(turn < 0) or (turn > 8) or (board[turn] == "X") or (board[turn] == "O"):
            turn = int(input("Enter number between 0-8 or enter number that isn't taken already "))

          board[turn] = symbol2

          printGame(board)
          numTurns += 1
        else:
          winner = 2
          print("Winner is Player 1")
          play = input("Do you want to play again? 0/1 no/yes ")
          return play

# Player 2 when first, input where to go on tic tac toe board and tests to see if there is a winner

    if(player2 == 1):
      if(testWin(board) == True):
        print("Player 2, it is your turn ")
        turn = int(input("Enter number between 0-8 "))
        while(turn < 0) or (turn > 8) or (board[turn] == "X") or (board[turn] == "O"):
          turn = int(input("Enter number between 0-8 or enter number that isn't taken already "))

        board[turn] = symbol1

        printGame(board)
        numTurns += 1

        # Tests if game was a tie
        if(numTurns == 9) and (testWin(board) == True):
          print("Its a Tie")
          winner = 3
          play = input("Do you want to play again? 0/1 no/yes ")
          return play

      else:
        winner = 1
        print("Winner is Player 1")
        play = input("Do you want to play again? 0/1 no/yes ")
        return play


# Player 1, input where to go on tic tac toe board and tests to see if there is a winner 
      if(winner != 1) and (winner != 3):
        if(testWin(board) == True):

          print("Player 1, it is your turn ")
          turn = int(input("Enter number between 0-8 "))
          while(turn < 0) or (turn > 8) or (board[turn] == "X") or (board[turn] == "O"):
            turn = int(input("Enter number between 0-8 or enter number that isn't taken already "))

        
          board[turn] = symbol2

          printGame(board)
          numTurns += 1
        else:
          winner = 2
          print("Winner is player 2")
          play = input("Do you want to play again? 0/1 no/yes ")
          return play

  

def main():

  print("Welcome to Tic-Tac-Toe. This is for two players")


  boardA = [0,1,2,3,4,5,6,7,8]
  size = len(boardA)
  

  printGame(boardA)
  player1, player2, symbol1, symbol2 = random()
  play = game(player1, player2, symbol1, symbol2 ,boardA)

# Replays game, empties list and recreates it  
  while(play == "1"):
    boardA = []
    for i in range(9):
      boardA.append(i)
  
    play = game(player1, player2, symbol1, symbol2 ,boardA)
   
  if(play == "0"):
    print("Thanks for playing :) ")
main()
