import random 

board = []
board2= []
 
board = range(0, 10) #creates the number of collums  for board 1

for i in board: #creates the board size
    board[i] = (["O"]* 10)
    
board2 = range(0, 10) #creates the number of collums for board 2
	
for i in board2:#creates the board size for board 2
    board2[i] = (["O"]* 10)
    
def print_board(board): #prints players 1's board
	for row in board:
		print " ".join(row)

def print_board2(board2): #prints players 2's board
	for row in board2:
		print " ".join(row)
    
    
from random import randint # Imports the random interger function from random module

import sys #for restart program

import os # for restart program

def restart_program(): # restart program
	python = sys.executable
	os.execl(python, python, * sys.argv)

"""if __name__ == "__main__":
	    answer = raw_input("Do you want to play again?")
		if answer.strip() in "y Y yes Yes YES".split():
		    restart_program()""" #this is the code to restart the programe

print "Let's play Battleship!" #prints when game starts
print"Player 2's board"
print_board(board)
print "Player 1's board"
print_board2(board2)
print "Player 1's turn"

print "Guess a row and collum."

def random_row(y):  
  return random.randint(0,len(y)-1) 

def random_col(x):
  return random.randint(0,len(x[0])-1) 
	
	
def verify_int(input): # Checks to see if input is an integer
    try: # Tries...
        val = int(input) # If input is an integer...
        return val # Returns input if it is an integer
    except ValueError: # If an error is returned...
        return 0 # Returns a "0"
	
	

ship_row = random_row(board) #makes the function equal to a more useable variable
ship_col = random_col(board) #makes the function equal to a more useable variable
ship_row2 = random_row(board2) #makes the function equal to a more useable variable
ship_col2 = random_col(board2) #makes the function equal to a more useable variable

	

one_direc = randint(1, 4) # Decides the direction of player 1's ship's second component
two_direc = randint(1, 4) # 1 = North, 2 = East, 3 = South, 4 = West

turn_player = 0 # 


while turn_player == 0: # Decides the location of player 1's ship's second component
    if one_direc == 1: # north
        one_sec_ship_row = ship_row - 1 # The row above is selected
        one_sec_ship_col = ship_col # The same column is selected
        if one_sec_ship_row < 0: # If the row selected is outside of the bounds...
            turn_player = 0 #restarts the 
            break# Begins the selectino of player 2's ship's second component
        else: # If the row selected is inside of the bounds...
            turn_player = 1 # Begins the selection of player 2's ship's second component
    elif one_direc == 2: # east
        one_sec_ship_row = ship_row
        one_sec_ship_col = ship_col + 1
        if one_sec_ship_col > 4:
            one_sec_ship_col = one_sec_ship_col - 2
            turn_player = 1
        else:
            turn_player = 1
    elif one_direc == 3: # south
        one_sec_ship_row = ship_row + 1
        one_sec_ship_col = ship_col
        if one_sec_ship_row > 10:
            one_sec_ship_row = one_sec_ship_row - 2
            turn_player = 1
        else:
            turn_player = 1
    elif one_direc == 4: # west
        one_sec_ship_row = ship_row
        one_sec_ship_col = ship_col - 1
        if one_sec_ship_col < 0:
            one_sec_ship_col = one_sec_ship_col + 2
            turn_player = 1
        else:
            turn_player = 1
    else:
        print "Error 1: Player 1 Ship, Component 2"
        
        

while turn_player == 1: # The same as above, but for ship 2
    if two_direc == 1:
        two_sec_ship_row = ship_row2 - 1
        two_sec_ship_col = ship_col2
        if two_sec_ship_row < 0:
            two_sec_ship_row = two_sec_ship_row + 2
            turn_player = 2 # Begins the actual game
        else:
            turn_player = 2
    elif two_direc == 2:
        two_sec_ship_row = ship_row2
        two_sec_ship_col = ship_col2 + 1
        if two_sec_ship_col > 10:
            two_sec_ship_col = two_sec_ship_col - 2
            turn_player = 2
        else:
            turn_player = 2
    elif two_direc == 3:
        two_sec_ship_row = ship_row2 + 1
        two_sec_ship_col = ship_col2
        if two_sec_ship_row > 10:
            two_sec_ship_row = two_sec_ship_row - 2
            turn_player = 2
        else:
            turn_player = 2
    elif two_direc == 4:
        two_sec_ship_row = ship_row2
        two_sec_ship_col = ship_col2 - 1
        if two_sec_ship_col < 0:
            two_sec_ship_col = two_sec_ship_col + 2
            turn_player = 2
        else:
            turn_player = 2
    else:
        print "Error 2: Player 2 Ship, Component 2"

turn_player = 2

while 1 == 1:
    while turn_player == 2:
        guess_col = verify_int(raw_input("Guess Col:")) 
        guess_col = guess_col -1
        guess_row = verify_int(raw_input("Guess Row:")) 
        guess_row = guess_row - 1
        guess = 0 #for the first turn  
        print "Player 1's turn"
        print_board(board)
        if guess_row == ship_row and guess_col == ship_col:
            board[guess_row][guess_col] = "X"
        if board[ship_row][ship_col] == "X" and board[one_sec_ship_row][one_sec_ship_col] == "X": 
            print ""
            print "Color me surprised, you actually won."
            turn_player = 4 # Begins the celebratory statement below
            break
        if (guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
			print "That's not even on the board."
        elif board[guess_row][guess_col] == "0" or board[guess_row][guess_col] == "X":
			print "You guessed that one already."
        else:
			print "You missed."
			board[guess_row][guess_col] = "0"
        print"Player 2's board"
        print_board(board)
        print "Player 1's board"
        print_board2(board2)
        print "Player 2's turn"
        turn_player = 3
		
	while turn_player == 3:
		guess_col2 = verify_int(raw_input("Guess Col:")) 
		guess_col2 = guess_col2 - 1
		guess_row2 = verify_int(raw_input("Guess Row:")) 
		guess_row2 = guess_row2 -1
		print "Player 2's turn"
		if guess_row2 == ship_row2 and guess_col2 == ship_col2:
		    board2[guess_row2][guess_col2] == "X"
        if board2[ship_row2][ship_col2] == "X"  and board2[two_sec_ship_row][two_sec_ship_col] == "X": 
            print "Color  me surprised, you actually won."
            turn_player = 5
            break
        if (guess_row2 < 0 or guess_row2 > 10) or (guess_col2 < 0 or guess_col2 > 10):
			print "That's not even on the board."
        if board2[guess_row2][guess_col2] == "0":
            print "You guessed that one already."
        else:
            print "You missed."
            board2[guess_row2][guess_col2] = "0"
        print"Player 2's board"
        print_board(board)
        print "Player 1's board"
        print_board2(board2)
        print "Player 1's turn"
        turn_player == 2
              
    if turn_player == 4:
        print "Player 1 wins"
    
    if turn_player == 5:
        print "player 2 wins"
			

