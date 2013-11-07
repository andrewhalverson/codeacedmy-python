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

from random import randrange, uniform

import sys #for restart program

import os # for restart program

def restart_program(): # restart program
	python = sys.executable
	os.execl(python, python, * sys.argv)

""""four ships: a five-space battleship, a four-space cruiser, a three-space submarine, and a two-space destroyer."""

""""Some players use a five-space battleship, a three-space cruiser, and 2 two-space destroyers."""

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



ship4_row = random_row(board) #makes the function equal to a more useable variable  2 space ship
ship4_col = random_col(board) #makes the function equal to a more useable variable 2 space ship
ship4_row2 = random_row(board2) #makes the function equal to a more useable variable 2 space ship
ship4_col2 = random_col(board2) #makes the function equal to a more useable variable 2 space ship
ship1_row = random_row(board) # 5 space ship
ship1_col = random_col(board) # 5 space ship
ship1_row2 = random_row(board2) # 5 space ship
ship1_col2 = random_col(board2) # 5 space ship
ship2_row = random_row(board) #4 space ships
ship2_col = random_col(board)
ship2_row2 = random_row(board2)
ship2_col2 = random_col(board2)
ship3_row = random_row(board) # 3 space ship
ship3_col = random_col(board)
ship3_row2 = random_row(board2)
ship3_col2 = random_col(board2)

"""one_sec_ship2_row2<---number of board/player
        ^            ^
   section      Number of ship""" #read this! it is important for what the code means

one_direc = randint(1, 4)# Decides the direction of player 1's ship's second component
two_direc = randint(1, 4) # 1 = North, 2 = East, 3 = South, 4 = West






one_direc = uniform(1, 4)

"""battle ship, is suppose to have a 5 line row """



while 1==1:

	turn_player = 20

	ship1_one_direc = randint(1,4)




	while turn_player == 10:
		ship1_one_direc = randint(1,4)
		two_direc =randint(1,4)
		turn_player = 20

	while turn_player == 20:#choose which ship it is
		ship4_row = random_row(board) #makes the function equal to a more useable variable  2 space ship
		ship4_col = random_col(board)
		if ship1_one_direc == 1:
			one_sec_ship1_row = ship1_row
			one_sec_ship1_col = ship1_col
			two_sec_ship1_row = ship1_row - 1  #makes it the number above for each row another cordinate to symbolize going north or up
			two_sec_ship1_col = ship1_col
			three_sec_ship1_row = ship1_row - 2
			three_sec_ship1_col = ship1_col
			four_sec_ship1_row = ship1_row - 3
			four_sec_ship1_col = ship1_col
			five_sec_ship1_row = ship1_row - 4
			five_sec_ship1_col = ship1_col
			if two_sec_ship1_row < 0 or three_sec_ship1_row < 0 or four_sec_ship1_row < 0 or five_sec_ship1_row < 0:
				turn_player = 10
			else:#if it's inside the bounds
				turn_player = 21 #begins the code for the second 5 line ship
		if ship1_one_direc == 2:
			one_sec_ship1_row = ship1_row
			one_sec_ship1_col = ship1_col
			two_sec_ship1_row = ship1_row
			two_sec_ship1_col = ship1_col + 1
			three_sec_ship1_row = ship1_row
			three_sec_ship1_col = ship1_col + 2
			four_sec_ship1_row = ship1_row
			four_sec_ship1_col = ship1_col + 3
			five_sec_ship1_row = ship1_row
			five_sec_ship1_col = ship1_col + 4
			if two_sec_ship1_col > 9 or three_sec_ship1_col > 9 or four_sec_ship1_col > 9 or five_sec_ship1_col > 9:
				turn_player = 10
			else:
				turn_player = 21
		if ship1_one_direc == 3: # south/down
			one_sec_ship1_row = ship1_row
			one_sec_ship1_col = ship1_col
			two_sec_ship1_row = ship1_row + 1  #makes it the number above for each row another cordinate to symbolize going north or up
			two_sec_ship1_row = ship1_col
			three_sec_ship1_row = ship1_row + 2
			three_sec_ship1_col = ship1_col
			four_sec_ship1_row = ship1_row + 3
			four_sec_ship1_col = ship1_col
			five_sec_ship1_row = ship1_row + 4
			five_sec_ship1_col = ship1_col
			if two_sec_ship1_row > 9 or three_sec_ship1_row > 9 or four_sec_ship1_row > 9 or five_sec_ship1_row > 9:
				turn_player = 10
			else:
				turn_player = 21
		if ship1_one_direc == 4: #west/left
			one_sec_ship1_row = ship1_row
			one_sec_ship1_col = ship1_col
			two_sec_ship1_row = ship1_row
			two_sec_ship1_col = ship1_col - 1
			three_sec_ship1_row = ship1_row
			three_sec_ship1_col = ship1_col - 2
			four_sec_ship1_row = ship1_row
			four_sec_ship1_col = ship1_col - 3
			five_sec_ship1_row = ship1_row
			five_sec_ship1_col = ship1_col - 4
			if two_sec_ship1_col < 0 or three_sec_ship1_col < 0 or four_sec_ship1_col < 0 or five_sec_ship1_col < 0:
				turn_player = 10
			else:
				turn_player = 21
		else:
			turn_player = 10


	ship1_two_direc = random.randint(1,4)
	while turn_player == 11:
		one_direc = randint(1,4)
		ship1_two_direc = random.randint(1,4)
		turn_player = 21

	while turn_player == 21: #choose which ship it is
		ship4_row2 = random_row(board2) #makes the function equal to a more useable variable 2 space ship
		ship4_col2 = random_col(board2)
		if ship1_two_direc == 1: #north/up
			one_sec_ship1_row2 = ship1_row2
			one_sec_ship1_col2 = ship1_col2
			two_sec_ship1_row2 = ship1_row2 - 1  #makes it the number above for each row another cordinate to symbolize going north or up
			two_sec_ship1_col2 = ship1_col2
			three_sec_ship1_row2 = ship1_row2 - 2
			three_sec_ship1_col2 = ship1_col2
			four_sec_ship1_row2 = ship1_row2 - 3
			four_sec_ship1_col2 = ship1_col2
			five_sec_ship1_row2 = ship1_row2 - 4
			five_sec_ship1_col2 = ship1_col2
			if two_sec_ship1_row2 < 0 or three_sec_ship1_row2 < 0 or four_sec_ship1_row2 < 0 or five_sec_ship1_row2 < 0:
				turn_player = 11
				break
			else: #if it's inside the bounds
				turn_player = 22 #begins the code for the second 5 line ship
		elif ship1_two_direc == 2: #east/right
			one_sec_ship1_row2 = ship1_row2
			one_sec_ship1_col2 = ship1_col2
			two_sec_ship1_row2 = ship1_row2
			two_sec_ship1_col2 = ship1_col2 + 1
			three_sec_ship1_row2 = ship1_row2
			three_sec_ship1_col2 = ship1_col2 + 2
			four_sec_ship1_row2 = ship1_row2
			four_sec_ship1_col2 = ship1_col2 + 3
			five_sec_ship1_row2 = ship1_row2
			five_sec_ship1_col2 = ship1_col2 + 4
			if two_sec_ship1_col2 > 9 or three_sec_ship1_col2 > 9 or four_sec_ship1_col2 > 9 or five_sec_ship1_col2 > 9:
				turn_player = 11
				break
			else:
				turn_player = 22
		elif ship1_two_direc == 3: # south/down
			one_sec_ship1_row2 = ship1_row2
			one_sec_ship1_col2 = ship1_col2
			two_sec_ship1_row2 = ship1_row2 + 1  #makes it the number above for each row another cordinate to symbolize going north or up
			two_sec_ship1_col2 = ship1_col2
			three_sec_ship1_row2 = ship1_row2 + 2
			three_sec_ship1_col2 = ship1_col2
			four_sec_ship1_row2 = ship1_row2 + 3
			four_sec_ship1_col2 = ship1_col2
			five_sec_ship1_row2 = ship1_row2 + 4
			five_sec_ship1_col2 = ship1_col2
			if two_sec_ship1_row2 > 9 or three_sec_ship1_row2 > 9 or four_sec_ship1_row2 > 9 or five_sec_ship1_row2 > 9:
				turn_player = 11
				break
			else:
				turn_player = 22
		elif ship1_two_direc == 4: #west/left
			one_sec_ship1_row2 = ship1_row2
			one_sec_ship1_col2 = ship1_col2
			two_sec_ship1_row2 = ship1_row2
			two_sec_ship1_col2 = ship1_col2 - 1
			three_sec_ship1_row2 = ship1_row2
			three_sec_ship1_col2 = ship1_col2 - 2
			four_sec_ship1_row2 = ship1_row2
			four_sec_ship1_col2 = ship1_col2 - 3
			five_sec_ship1_row2 = ship1_row2
			five_sec_ship1_col2 = ship1_col2 - 4
			if two_sec_ship1_col2 < 0 or three_sec_ship1_col2 < 0 or four_sec_ship1_col2 < 0 or five_sec_ship1_col2 < 0:
				turn_player = 11
				break
			else:
				turn_player = 22
		else:
			turn_player = 11


	ship2_one_direc = randint(1,4)
	while turn_player ==12:
		ship2_one_direc = randint(1,4)
		two_direc =randint(1,4)
		turn_player = 22


	while turn_player == 22: #choose which ship it is
		ship2_row = random_row(board) #4 space ships
		ship2_col = random_col(board)
		if ship2_one_direc == 1: #north/up
			one_sec_ship2_row = ship2_row
			one_sec_ship2_col = ship2_col
			two_sec_ship2_row = ship2_row - 1  #makes it the number above for each row another cordinate to symbolize going north or up
			two_sec_ship2_col = ship2_col
			three_sec_ship2_row = ship2_row - 2
			three_sec_ship2_col = ship2_col
			four_sec_ship2_row = ship2_row - 3
			four_sec_ship2_col = ship2_col
			if two_sec_ship2_row < 0 or three_sec_ship1_row < 0 or four_sec_ship1_row < 0:
				turn_player = 12
				break
			if (one_sec_ship2_row == one_sec_ship1_row and one_sec_ship2_col == one_sec_ship1_col) or (one_sec_ship2_row == two_sec_ship1_row and one_sec_ship2_col == two_sec_ship1_col) or (one_sec_ship2_row == three_sec_ship1_row and one_sec_ship2_col == three_sec_ship1_col) or (one_sec_ship2_row == four_sec_ship1_row and one_sec_ship2_col == four_sec_ship1_col) or (one_sec_ship2_row == five_sec_ship1_row and one_sec_ship2_col == five_sec_ship1_col) or (two_sec_ship2_row == one_sec_ship1_row and two_sec_ship2_col == one_sec_ship1_col) or (two_sec_ship2_row == two_sec_ship1_row and two_sec_ship2_col == two_sec_ship1_col) or (two_sec_ship2_row == three_sec_ship1_row and two_sec_ship2_col == three_sec_ship1_col) or (two_sec_ship2_row == four_sec_ship1_row and two_sec_ship2_col == four_sec_ship1_col) or (two_sec_ship2_row == five_sec_ship1_row and two_sec_ship2_col == five_sec_ship1_col) or (three_sec_ship2_row == one_sec_ship1_row and three_sec_ship2_col == one_sec_ship1_col) or (three_sec_ship2_row == two_sec_ship1_row and three_sec_ship2_col == two_sec_ship1_col) or (three_sec_ship2_row == three_sec_ship1_row and three_sec_ship2_col == three_sec_ship1_col) or (three_sec_ship2_row == four_sec_ship1_row and three_sec_ship2_col == four_sec_ship1_col) or (three_sec_ship2_row == five_sec_ship1_row and three_sec_ship2_col == five_sec_ship1_col) or (four_sec_ship2_row == one_sec_ship1_row and four_sec_ship2_col == one_sec_ship1_col) or (four_sec_ship2_row == two_sec_ship1_row and four_sec_ship2_col == two_sec_ship1_col) or (four_sec_ship2_row == three_sec_ship1_row and four_sec_ship2_col == three_sec_ship1_col) or (four_sec_ship2_row == four_sec_ship1_row and four_sec_ship2_col == four_sec_ship1_col) or (four_sec_ship2_row == five_sec_ship1_row and four_sec_ship2_col == five_sec_ship1_col):
				turn_player = 12
				break
			else: #if it's inside the bounds
				turn_player = 23 #begins the code for the second 4 line ship
		elif ship2_one_direc == 2: #east/right
			one_sec_ship2_row = ship2_row
			one_sec_ship2_col = ship2_col
			two_sec_ship2_row = ship2_row
			two_sec_ship2_col = ship2_col + 1
			three_sec_ship2_row = ship2_row
			three_sec_ship2_col = ship2_col + 2
			four_sec_ship2_row = ship2_row
			four_sec_ship2_col = ship2_col + 3
			if two_sec_ship2_col > 9 or three_sec_ship2_col > 9 or four_sec_ship2_col > 9:
				turn_player = 12
				break
			if (one_sec_ship2_row == one_sec_ship1_row and one_sec_ship2_col == one_sec_ship1_col) or (one_sec_ship2_row == two_sec_ship1_row and one_sec_ship2_col == two_sec_ship1_col) or (one_sec_ship2_row == three_sec_ship1_row and one_sec_ship2_col == three_sec_ship1_col) or (one_sec_ship2_row == four_sec_ship1_row and one_sec_ship2_col == four_sec_ship1_col) or (one_sec_ship2_row == five_sec_ship1_row and one_sec_ship2_col == five_sec_ship1_col) or (two_sec_ship2_row == one_sec_ship1_row and two_sec_ship2_col == one_sec_ship1_col) or (two_sec_ship2_row == two_sec_ship1_row and two_sec_ship2_col == two_sec_ship1_col) or (two_sec_ship2_row == three_sec_ship1_row and two_sec_ship2_col == three_sec_ship1_col) or (two_sec_ship2_row == four_sec_ship1_row and two_sec_ship2_col == four_sec_ship1_col) or (two_sec_ship2_row == five_sec_ship1_row and two_sec_ship2_col == five_sec_ship1_col) or (three_sec_ship2_row == one_sec_ship1_row and three_sec_ship2_col == one_sec_ship1_col) or (three_sec_ship2_row == two_sec_ship1_row and three_sec_ship2_col == two_sec_ship1_col) or (three_sec_ship2_row == three_sec_ship1_row and three_sec_ship2_col == three_sec_ship1_col) or (three_sec_ship2_row == four_sec_ship1_row and three_sec_ship2_col == four_sec_ship1_col) or (three_sec_ship2_row == five_sec_ship1_row and three_sec_ship2_col == five_sec_ship1_col) or (four_sec_ship2_row == one_sec_ship1_row and four_sec_ship2_col == one_sec_ship1_col) or (four_sec_ship2_row == two_sec_ship1_row and four_sec_ship2_col == two_sec_ship1_col) or (four_sec_ship2_row == three_sec_ship1_row and four_sec_ship2_col == three_sec_ship1_col) or (four_sec_ship2_row == four_sec_ship1_row and four_sec_ship2_col == four_sec_ship1_col) or (four_sec_ship2_row == five_sec_ship1_row and four_sec_ship2_col == five_sec_ship1_col):
				turn_player = 12
				break
			else:
				turn_player = 23
		elif ship2_one_direc == 3: # south/down
			one_sec_ship2_row = ship2_row
			one_sec_ship2_col = ship2_col
			two_sec_ship2_row = ship2_row + 1  #makes it the number above for each row another cordinate to symbolize going north or up
			two_sec_ship2_row = ship2_col
			three_sec_ship2_row = ship2_row + 2
			three_sec_ship2_col = ship2_col
			four_sec_ship2_row = ship2_row + 3
			four_sec_ship2_col = ship2_col
			if two_sec_ship2_row > 9 or three_sec_ship2_row > 9 or four_sec_ship2_row > 9:
				turn_player = 12
				break
			if ((one_sec_ship2_row == one_sec_ship1_row and one_sec_ship2_col == one_sec_ship1_col) or (one_sec_ship2_row == two_sec_ship1_row and one_sec_ship2_col == two_sec_ship1_col) or (one_sec_ship2_row == three_sec_ship1_row and one_sec_ship2_col == three_sec_ship1_col) or (one_sec_ship2_row == four_sec_ship1_row and one_sec_ship2_col == four_sec_ship1_col) or (one_sec_ship2_row == five_sec_ship1_row and one_sec_ship2_col == five_sec_ship1_col) or (two_sec_ship2_row == one_sec_ship1_row and two_sec_ship2_col == one_sec_ship1_col) or (two_sec_ship2_row == two_sec_ship1_row and two_sec_ship2_col == two_sec_ship1_col) or (two_sec_ship2_row == three_sec_ship1_row and two_sec_ship2_col == three_sec_ship1_col) or (two_sec_ship2_row == four_sec_ship1_row and two_sec_ship2_col == four_sec_ship1_col) or (two_sec_ship2_row == five_sec_ship1_row and two_sec_ship2_col == five_sec_ship1_col) or (three_sec_ship2_row == one_sec_ship1_row and three_sec_ship2_col == one_sec_ship1_col) or (three_sec_ship2_row == two_sec_ship1_row and three_sec_ship2_col == two_sec_ship1_col) or (three_sec_ship2_row == three_sec_ship1_row and three_sec_ship2_col == three_sec_ship1_col) or (three_sec_ship2_row == four_sec_ship1_row and three_sec_ship2_col == four_sec_ship1_col) or (three_sec_ship2_row == five_sec_ship1_row and three_sec_ship2_col == five_sec_ship1_col) or (four_sec_ship2_row == one_sec_ship1_row and four_sec_ship2_col == one_sec_ship1_col) or (four_sec_ship2_row == two_sec_ship1_row and four_sec_ship2_col == two_sec_ship1_col) or (four_sec_ship2_row == three_sec_ship1_row and four_sec_ship2_col == three_sec_ship1_col) or (four_sec_ship2_row == four_sec_ship1_row and four_sec_ship2_col == four_sec_ship1_col) or (four_sec_ship2_row == five_sec_ship1_row and four_sec_ship2_col == five_sec_ship1_col)):
				turn_player = 12
				break
			else:
				turn_player = 23
		elif ship2_one_direc == 4: #west/left
			one_sec_ship2_row = ship2_row
			one_sec_ship2_col = ship2_col
			two_sec_ship2_row = ship2_row
			two_sec_ship2_col = ship2_col - 1
			three_sec_ship2_row = ship2_row
			three_sec_ship2_col = ship2_col - 2
			four_sec_ship2_row = ship2_row
			four_sec_ship2_col = ship2_col - 3
			if two_sec_ship2_col < 0 or three_sec_ship2_col < 0 or four_sec_ship2_col < 0 :
				turn_player = 12
				break
			if (one_sec_ship2_row == one_sec_ship1_row and one_sec_ship2_col == one_sec_ship1_col) or (one_sec_ship2_row == two_sec_ship1_row and one_sec_ship2_col == two_sec_ship1_col) or (one_sec_ship2_row == three_sec_ship1_row and one_sec_ship2_col == three_sec_ship1_col) or (one_sec_ship2_row == four_sec_ship1_row and one_sec_ship2_col == four_sec_ship1_col) or (one_sec_ship2_row == five_sec_ship1_row and one_sec_ship2_col == five_sec_ship1_col) or (two_sec_ship2_row == one_sec_ship1_row and two_sec_ship2_col == one_sec_ship1_col) or (two_sec_ship2_row == two_sec_ship1_row and two_sec_ship2_col == two_sec_ship1_col) or (two_sec_ship2_row == three_sec_ship1_row and two_sec_ship2_col == three_sec_ship1_col) or (two_sec_ship2_row == four_sec_ship1_row and two_sec_ship2_col == four_sec_ship1_col) or (two_sec_ship2_row == five_sec_ship1_row and two_sec_ship2_col == five_sec_ship1_col) or (three_sec_ship2_row == one_sec_ship1_row and three_sec_ship2_col == one_sec_ship1_col) or (three_sec_ship2_row == two_sec_ship1_row and three_sec_ship2_col == two_sec_ship1_col) or (three_sec_ship2_row == three_sec_ship1_row and three_sec_ship2_col == three_sec_ship1_col) or (three_sec_ship2_row == four_sec_ship1_row and three_sec_ship2_col == four_sec_ship1_col) or (three_sec_ship2_row == five_sec_ship1_row and three_sec_ship2_col == five_sec_ship1_col) or (four_sec_ship2_row == one_sec_ship1_row and four_sec_ship2_col == one_sec_ship1_col) or (four_sec_ship2_row == two_sec_ship1_row and four_sec_ship2_col == two_sec_ship1_col) or (four_sec_ship2_row == three_sec_ship1_row and four_sec_ship2_col == three_sec_ship1_col) or (four_sec_ship2_row == four_sec_ship1_row and four_sec_ship2_col == four_sec_ship1_col) or (four_sec_ship2_row == five_sec_ship1_row and four_sec_ship2_col == five_sec_ship1_col):
				turn_player = 12
				break
			else:
				turn_player = 23
		else:
			turn_player = 12

	ship2_two_direc = randint(1,4)
	while turn_player == 13:
		one_direc = randint(1,4)
		ship2_two_direc =randint(1,4)
		turn_player = 23
	
	
	while turn_player == 23: #choose which ship it is
		ship2_row2 = random_row(board2) #4 space ships
		ship2_col2 = random_col(board2)
		if ship2_two_direc == 1: #north/up
			one_sec_ship2_row2 = ship2_row2
			one_sec_ship2_col2 = ship2_col2
			two_sec_ship2_row2 = ship2_row2 - 1  #makes it the number above for each row another cordinate to symbolize going north or up
			two_sec_ship2_row2 = ship2_col2
			three_sec_ship2_row2 = ship2_row2 - 2
			three_sec_ship2_col2 = ship2_col2
			four_sec_ship2_row2 = ship2_row2 - 3
			four_sec_ship2_col2 = ship2_col2
			if two_sec_ship2_row2 < 0 or three_sec_ship1_row2 < 0 or four_sec_ship1_row2 < 0:
				turn_player = 13
				break
			if (one_sec_ship2_row2 == one_sec_ship1_row2 and one_sec_ship2_col2 == one_sec_ship1_col2) or (one_sec_ship2_row2 == two_sec_ship1_row2 and one_sec_ship2_col2 == two_sec_ship1_col2) or (one_sec_ship2_row2 == three_sec_ship1_row2 and one_sec_ship2_col2 == three_sec_ship1_col2) or (one_sec_ship2_row2 == four_sec_ship1_row2 and one_sec_ship2_col2 == four_sec_ship1_col2) or (one_sec_ship2_row2 == five_sec_ship1_row2 and one_sec_ship2_col2 == five_sec_ship1_col2) or (two_sec_ship2_row2 == one_sec_ship1_row2 and two_sec_ship2_col2 == one_sec_ship1_col2) or (two_sec_ship2_row2 == two_sec_ship1_row2 and two_sec_ship2_col2 == two_sec_ship1_col2) or (two_sec_ship2_row2 == three_sec_ship1_row2 and two_sec_ship2_col2 == three_sec_ship1_col2) or (two_sec_ship2_row2 == four_sec_ship1_row2 and two_sec_ship2_col2 == four_sec_ship1_col2) or (two_sec_ship2_row2 == five_sec_ship1_row2 and two_sec_ship2_col2 == five_sec_ship1_col2) or (three_sec_ship2_row2 == one_sec_ship1_row2 and three_sec_ship2_col2 == one_sec_ship1_col2) or (three_sec_ship2_row2 == two_sec_ship1_row2 and three_sec_ship2_col2 == two_sec_ship1_col2) or (three_sec_ship2_row2 == three_sec_ship1_row2 and three_sec_ship2_col2 == three_sec_ship1_col2) or (three_sec_ship2_row2 == four_sec_ship1_row2 and three_sec_ship2_col2 == four_sec_ship1_col2) or (three_sec_ship2_row2 == five_sec_ship1_row2 and three_sec_ship2_col2 == five_sec_ship1_col2) or (four_sec_ship2_row2 == one_sec_ship1_row2 and four_sec_ship2_col2 == one_sec_ship1_col2) or (four_sec_ship2_row2 == two_sec_ship1_row2 and four_sec_ship2_col2 == two_sec_ship1_col2) or (four_sec_ship2_row2 == three_sec_ship1_row2 and four_sec_ship2_col2 == three_sec_ship1_col2) or (four_sec_ship2_row2 == four_sec_ship1_row2 and four_sec_ship2_col2 == four_sec_ship1_col2) or (four_sec_ship2_row2 == five_sec_ship1_row2 and four_sec_ship2_col2 == five_sec_ship1_col2):
				turn_player = 13
				break
			else: #if it's inside the bounds
				turn_player = 24 #begins the code for the second 4 line ship
		elif ship2_two_direc == 2: #east/right
			one_sec_ship2_row2 = ship2_row2
			one_sec_ship2_col2 = ship2_col2
			two_sec_ship2_row2 = ship2_row2
			two_sec_ship2_col2 = ship2_col2 + 1
			three_sec_ship2_row2 = ship2_row2
			three_sec_ship2_col2 = ship2_col2 + 2
			four_sec_ship2_row2 = ship2_row2
			four_sec_ship2_col2 = ship2_col2 + 3
			if two_sec_ship2_col2 > 9 or three_sec_ship2_col2 > 9 or four_sec_ship2_col2 > 9:
				turn_player = 13
				break
			if (one_sec_ship2_row2 == one_sec_ship1_row2 and one_sec_ship2_col2 == one_sec_ship1_col2) or (one_sec_ship2_row2 == two_sec_ship1_row2 and one_sec_ship2_col2 == two_sec_ship1_col2) or (one_sec_ship2_row2 == three_sec_ship1_row2 and one_sec_ship2_col2 == three_sec_ship1_col2) or (one_sec_ship2_row2 == four_sec_ship1_row2 and one_sec_ship2_col2 == four_sec_ship1_col2) or (one_sec_ship2_row2 == five_sec_ship1_row2 and one_sec_ship2_col2 == five_sec_ship1_col2) or (two_sec_ship2_row2 == one_sec_ship1_row2 and two_sec_ship2_col2 == one_sec_ship1_col2) or (two_sec_ship2_row2 == two_sec_ship1_row2 and two_sec_ship2_col2 == two_sec_ship1_col2) or (two_sec_ship2_row2 == three_sec_ship1_row2 and two_sec_ship2_col2 == three_sec_ship1_col2) or (two_sec_ship2_row2 == four_sec_ship1_row2 and two_sec_ship2_col2 == four_sec_ship1_col2) or (two_sec_ship2_row2 == five_sec_ship1_row2 and two_sec_ship2_col2 == five_sec_ship1_col2) or (three_sec_ship2_row2 == one_sec_ship1_row2 and three_sec_ship2_col2 == one_sec_ship1_col2) or (three_sec_ship2_row2 == two_sec_ship1_row2 and three_sec_ship2_col2 == two_sec_ship1_col2) or (three_sec_ship2_row2 == three_sec_ship1_row2 and three_sec_ship2_col2 == three_sec_ship1_col2) or (three_sec_ship2_row2 == four_sec_ship1_row2 and three_sec_ship2_col2 == four_sec_ship1_col2) or (three_sec_ship2_row2 == five_sec_ship1_row2 and three_sec_ship2_col2 == five_sec_ship1_col2) or (four_sec_ship2_row2 == one_sec_ship1_row2 and four_sec_ship2_col2 == one_sec_ship1_col2) or (four_sec_ship2_row2 == two_sec_ship1_row2 and four_sec_ship2_col2 == two_sec_ship1_col2) or (four_sec_ship2_row2 == three_sec_ship1_row2 and four_sec_ship2_col2 == three_sec_ship1_col2) or (four_sec_ship2_row2 == four_sec_ship1_row2 and four_sec_ship2_col2 == four_sec_ship1_col2) or (four_sec_ship2_row2 == five_sec_ship1_row2 and four_sec_ship2_col2 == five_sec_ship1_col2):
				turn_plauer = 13
				break
			else:
				turn_player = 24
		elif ship2_two_direc == 3: # south/down
			one_sec_ship2_row2 = ship2_row2
			one_sec_ship2_col2 = ship2_col2
			two_sec_ship2_row2 = ship2_row2 + 1  #makes it the number above for each row another cordinate to symbolize going north or up
			two_sec_ship2_col2 = ship2_col2
			three_sec_ship2_row2 = ship2_row2 + 2
			three_sec_ship2_col2 = ship2_col2
			four_sec_ship2_row2 = ship2_row2 + 3
			four_sec_ship2_col2 = ship2_col2
			if two_sec_ship2_row2 > 9 or three_sec_ship2_row2 > 9 or four_sec_ship2_row2 > 9:
				turn_player = 13
				break
			if (one_sec_ship2_row2 == one_sec_ship1_row2 and one_sec_ship2_col2 == one_sec_ship1_col2) or (one_sec_ship2_row2 == two_sec_ship1_row2 and one_sec_ship2_col2 == two_sec_ship1_col2) or (one_sec_ship2_row2 == three_sec_ship1_row2 and one_sec_ship2_col2 == three_sec_ship1_col2) or (one_sec_ship2_row2 == four_sec_ship1_row2 and one_sec_ship2_col2 == four_sec_ship1_col2) or (one_sec_ship2_row2 == five_sec_ship1_row2 and one_sec_ship2_col2 == five_sec_ship1_col2) or (two_sec_ship2_row2 == one_sec_ship1_row2 and two_sec_ship2_col2 == one_sec_ship1_col2) or (two_sec_ship2_row2 == two_sec_ship1_row2 and two_sec_ship2_col2 == two_sec_ship1_col2) or (two_sec_ship2_row2 == three_sec_ship1_row2 and two_sec_ship2_col2 == three_sec_ship1_col2) or (two_sec_ship2_row2 == four_sec_ship1_row2 and two_sec_ship2_col2 == four_sec_ship1_col2) or (two_sec_ship2_row2 == five_sec_ship1_row2 and two_sec_ship2_col2 == five_sec_ship1_col2) or (three_sec_ship2_row2 == one_sec_ship1_row2 and three_sec_ship2_col2 == one_sec_ship1_col2) or (three_sec_ship2_row2 == two_sec_ship1_row2 and three_sec_ship2_col2 == two_sec_ship1_col2) or (three_sec_ship2_row2 == three_sec_ship1_row2 and three_sec_ship2_col2 == three_sec_ship1_col2) or (three_sec_ship2_row2 == four_sec_ship1_row2 and three_sec_ship2_col2 == four_sec_ship1_col2) or (three_sec_ship2_row2 == five_sec_ship1_row2 and three_sec_ship2_col2 == five_sec_ship1_col2) or (four_sec_ship2_row2 == one_sec_ship1_row2 and four_sec_ship2_col2 == one_sec_ship1_col2) or (four_sec_ship2_row2 == two_sec_ship1_row2 and four_sec_ship2_col2 == two_sec_ship1_col2) or (four_sec_ship2_row2 == three_sec_ship1_row2 and four_sec_ship2_col2 == three_sec_ship1_col2) or (four_sec_ship2_row2 == four_sec_ship1_row2 and four_sec_ship2_col2 == four_sec_ship1_col2) or (four_sec_ship2_row2 == five_sec_ship1_row2 and four_sec_ship2_col2 == five_sec_ship1_col2):
				turn_player = 13
				break
			else:
				turn_player = 24
		elif ship2_two_direc == 4: #west/left
			one_sec_ship2_row2 = ship2_row2
			one_sec_ship2_col2 = ship2_col2
			two_sec_ship2_row2 = ship2_row2
			two_sec_ship2_col2 = ship2_col2 - 1
			three_sec_ship2_row2 = ship2_row2
			three_sec_ship2_col2 = ship2_col2 - 2
			four_sec_ship2_row2 = ship2_row2
			four_sec_ship2_col2 = ship2_col2 - 3
			if two_sec_ship2_col2 < 0 or three_sec_ship2_col2 < 0 or four_sec_ship2_col2 < 0:
				turn_player = 13
				break
			if (one_sec_ship2_row2 == one_sec_ship1_row2 and one_sec_ship2_col2 == one_sec_ship1_col2) or (one_sec_ship2_row2 == two_sec_ship1_row2 and one_sec_ship2_col2 == two_sec_ship1_col2) or (one_sec_ship2_row2 == three_sec_ship1_row2 and one_sec_ship2_col2 == three_sec_ship1_col2) or (one_sec_ship2_row2 == four_sec_ship1_row2 and one_sec_ship2_col2 == four_sec_ship1_col2) or (one_sec_ship2_row2 == five_sec_ship1_row2 and one_sec_ship2_col2 == five_sec_ship1_col2) or (two_sec_ship2_row2 == one_sec_ship1_row2 and two_sec_ship2_col2 == one_sec_ship1_col2) or (two_sec_ship2_row2 == two_sec_ship1_row2 and two_sec_ship2_col2 == two_sec_ship1_col2) or (two_sec_ship2_row2 == three_sec_ship1_row2 and two_sec_ship2_col2 == three_sec_ship1_col2) or (two_sec_ship2_row2 == four_sec_ship1_row2 and two_sec_ship2_col2 == four_sec_ship1_col2) or (two_sec_ship2_row2 == five_sec_ship1_row2 and two_sec_ship2_col2 == five_sec_ship1_col2) or (three_sec_ship2_row2 == one_sec_ship1_row2 and three_sec_ship2_col2 == one_sec_ship1_col2) or (three_sec_ship2_row2 == two_sec_ship1_row2 and three_sec_ship2_col2 == two_sec_ship1_col2) or (three_sec_ship2_row2 == three_sec_ship1_row2 and three_sec_ship2_col2 == three_sec_ship1_col2) or (three_sec_ship2_row2 == four_sec_ship1_row2 and three_sec_ship2_col2 == four_sec_ship1_col2) or (three_sec_ship2_row2 == five_sec_ship1_row2 and three_sec_ship2_col2 == five_sec_ship1_col2) or (four_sec_ship2_row2 == one_sec_ship1_row2 and four_sec_ship2_col2 == one_sec_ship1_col2) or (four_sec_ship2_row2 == two_sec_ship1_row2 and four_sec_ship2_col2 == two_sec_ship1_col2) or (four_sec_ship2_row2 == three_sec_ship1_row2 and four_sec_ship2_col2 == three_sec_ship1_col2) or (four_sec_ship2_row2 == four_sec_ship1_row2 and four_sec_ship2_col2 == four_sec_ship1_col2) or (four_sec_ship2_row2 == five_sec_ship1_row2 and four_sec_ship2_col2 == five_sec_ship1_col2):
				turn_player = 13
				break
			else:
				turn_player = 24 #goes to player 1 ship 3
		else:
			turn_player = 13

	ship3_one_direc = randint(1,4)
	while turn_player == 14:
		ship3_one_direc = randint(1,4)
		two_direc =randint(1,4)
		turn_player = 24


	while turn_player == 24: # Decides the ship
		ship3_row = random_row(board) # 3 space ship
		ship3_col = random_col(board)
		if ship3_one_direc == 1: # north
			one_sec_ship3_row = ship3_row  # The same row is selected
			one_sec_ship3_col = ship3_col  #the same col is selected
			two_sec_ship3_row = ship3_row - 1 #the row up is selected
			two_sec_ship3_col = ship3_col #the same col is selected
			three_sec_ship3_row = ship3_row - 2
			three_sec_ship3_sec = ship3_row
			if two_sec_ship3_row < 0 or three_sec_ship3_row < 0: # If the row selected is outside of the bounds...
				turn_player = 14  #restarts the random ship selection for its location
				break
			if ((one_sec_ship3_row == one_sec_ship1_row and one_sec_ship3_col == one_sec_ship1_col) or (one_sec_ship3_row == two_sec_ship1_row and one_sec_ship3_col == two_sec_ship1_col) or (one_sec_ship3_row == three_sec_ship1_row and one_sec_ship3_col == three_sec_ship1_col) or (one_sec_ship3_row == four_sec_ship1_row and one_sec_ship3_col == four_sec_ship1_col) or (one_sec_ship3_row == five_sec_ship1_row and one_sec_ship3_col == five_sec_ship1_col) or (two_sec_ship3_row == one_sec_ship1_row and two_sec_ship3_col == one_sec_ship1_col) or (two_sec_ship3_row == two_sec_ship1_row and two_sec_ship3_col == two_sec_ship1_col) or (two_sec_ship3_row == three_sec_ship1_row and two_sec_ship3_col == three_sec_ship1_col) or (two_sec_ship3_row == four_sec_ship1_row and two_sec_ship3_col == four_sec_ship1_col) or (two_sec_ship3_row == five_sec_ship1_row and two_sec_ship3_col == five_sec_ship1_col) or (three_sec_ship3_row == one_sec_ship1_row and three_sec_ship3_col == one_sec_ship1_col) or (three_sec_ship3_row == two_sec_ship1_row and three_sec_ship3_col == two_sec_ship1_col) or (three_sec_ship3_row == three_sec_ship1_row and three_sec_ship3_col == three_sec_ship1_col) or (three_sec_ship3_row == four_sec_ship1_row and three_sec_ship3_col == four_sec_ship1_col) or (three_sec_ship3_row == five_sec_ship1_row and three_sec_ship3_col == five_sec_ship1_col) or (one_sec_ship3_row == one_sec_ship2_row and one_sec_ship3_col == one_sec_ship2_col) or (one_sec_ship3_row == two_sec_ship2_row and one_sec_ship3_col == two_sec_ship2_col) or (one_sec_ship3_row == three_sec_ship2_row and one_sec_ship3_col == three_sec_ship2_col) or (one_sec_ship3_row == four_sec_ship2_row and one_sec_ship3_col == four_sec_ship2_col) or (two_sec_ship3_row == one_sec_ship2_row and two_sec_ship3_col == one_sec_ship2_col) or (two_sec_ship3_row == two_sec_ship2_row and two_sec_ship3_col == two_sec_ship2_col) or (two_sec_ship3_row == three_sec_ship2_row and two_sec_ship3_col == three_sec_ship2_col) or (two_sec_ship3_row == four_sec_ship2_row and two_sec_ship3_col == four_sec_ship2_col) or (three_sec_ship3_row == one_sec_ship2_row and three_sec_ship3_col == one_sec_ship2_col) or (three_sec_ship3_row == two_sec_ship2_row and three_sec_ship3_col == two_sec_ship2_col) or (three_sec_ship3_row == three_sec_ship2_row and three_sec_ship3_col == three_sec_ship2_col) or (three_sec_ship3_row == four_sec_ship2_row and three_sec_ship3_col == four_sec_ship2_col)):
				turn_player = 14
				break
			else: # If the row selected is inside of the bounds...
				turn_player = 25 # Begins the selection of player 2's ship's second component
		elif ship3_one_direc == 2: # east
			one_sec_ship3_row = ship3_row
			one_sec_ship3_col = ship3_col
			two_sec_ship3_row = ship3_row
			two_sec_ship3_col = ship3_col + 1
			three_sec_ship3_row = ship3_row
			three_sec_ship3_col = ship3_col + 2
			if two_sec_ship3_col > 9 or three_sec_ship3_col > 9:
				turn_player = 14
				break
			if (one_sec_ship3_row == one_sec_ship1_row and one_sec_ship3_col == one_sec_ship1_col) or (one_sec_ship3_row == two_sec_ship1_row and one_sec_ship3_col == two_sec_ship1_col) or (one_sec_ship3_row == three_sec_ship1_row and one_sec_ship3_col == three_sec_ship1_col) or (one_sec_ship3_row == four_sec_ship1_row and one_sec_ship3_col == four_sec_ship1_col) or (one_sec_ship3_row == five_sec_ship1_row and one_sec_ship3_col == five_sec_ship1_col) or (two_sec_ship3_row == one_sec_ship1_row and two_sec_ship3_col == one_sec_ship1_col) or (two_sec_ship3_row == two_sec_ship1_row and two_sec_ship3_col == two_sec_ship1_col) or (two_sec_ship3_row == three_sec_ship1_row and two_sec_ship3_col == three_sec_ship1_col) or (two_sec_ship3_row == four_sec_ship1_row and two_sec_ship3_col == four_sec_ship1_col) or (two_sec_ship3_row == five_sec_ship1_row and two_sec_ship3_col == five_sec_ship1_col) or (three_sec_ship3_row == one_sec_ship1_row and three_sec_ship3_col == one_sec_ship1_col) or (three_sec_ship3_row == two_sec_ship1_row and three_sec_ship3_col == two_sec_ship1_col) or (three_sec_ship3_row == three_sec_ship1_row and three_sec_ship3_col == three_sec_ship1_col) or (three_sec_ship3_row == four_sec_ship1_row and three_sec_ship3_col == four_sec_ship1_col) or (three_sec_ship3_row == five_sec_ship1_row and three_sec_ship3_col == five_sec_ship1_col) or (one_sec_ship3_row == one_sec_ship2_row and one_sec_ship3_col == one_sec_ship2_col) or (one_sec_ship3_row == two_sec_ship2_row and one_sec_ship3_col == two_sec_ship2_col) or (one_sec_ship3_row == three_sec_ship2_row and one_sec_ship3_col == three_sec_ship2_col) or (one_sec_ship3_row == four_sec_ship2_row and one_sec_ship3_col == four_sec_ship2_col) or (two_sec_ship3_row == one_sec_ship2_row and two_sec_ship3_col == one_sec_ship2_col) or (two_sec_ship3_row == two_sec_ship2_row and two_sec_ship3_col == two_sec_ship2_col) or (two_sec_ship3_row == three_sec_ship2_row and two_sec_ship3_col == three_sec_ship2_col) or (two_sec_ship3_row == four_sec_ship2_row and two_sec_ship3_col == four_sec_ship2_col) or (three_sec_ship3_row == one_sec_ship2_row and three_sec_ship3_col == one_sec_ship2_col) or (three_sec_ship3_row == two_sec_ship2_row and three_sec_ship3_col == two_sec_ship2_col) or (three_sec_ship3_row == three_sec_ship2_row and three_sec_ship3_col == three_sec_ship2_col) or (three_sec_ship3_row == four_sec_ship2_row and three_sec_ship3_col == four_sec_ship2_col):
				turn_player = 14
				break
			else:
				turn_player = 25
		elif ship3_one_direc == 3: # south
			one_sec_ship3_row = ship3_row
			one_sec_ship3_col = ship3_col
			two_sec_ship3_row = ship3_row + 1
			two_sec_ship3_col = ship3_col
			three_sec_ship3_row = ship3_row + 2
			three_sec_ship3_col = ship3_col
			if two_sec_ship3_row > 9 or three_sec_ship3_row > 9:
				turn_player = 14
				break
			if (one_sec_ship3_row == one_sec_ship1_row and one_sec_ship3_col == one_sec_ship1_col) or (one_sec_ship3_row == two_sec_ship1_row and one_sec_ship3_col == two_sec_ship1_col) or (one_sec_ship3_row == three_sec_ship1_row and one_sec_ship3_col == three_sec_ship1_col) or (one_sec_ship3_row == four_sec_ship1_row and one_sec_ship3_col == four_sec_ship1_col) or (one_sec_ship3_row == five_sec_ship1_row and one_sec_ship3_col == five_sec_ship1_col) or (two_sec_ship3_row == one_sec_ship1_row and two_sec_ship3_col == one_sec_ship1_col) or (two_sec_ship3_row == two_sec_ship1_row and two_sec_ship3_col == two_sec_ship1_col) or (two_sec_ship3_row == three_sec_ship1_row and two_sec_ship3_col == three_sec_ship1_col) or (two_sec_ship3_row == four_sec_ship1_row and two_sec_ship3_col == four_sec_ship1_col) or (two_sec_ship3_row == five_sec_ship1_row and two_sec_ship3_col == five_sec_ship1_col) or (three_sec_ship3_row == one_sec_ship1_row and three_sec_ship3_col == one_sec_ship1_col) or (three_sec_ship3_row == two_sec_ship1_row and three_sec_ship3_col == two_sec_ship1_col) or (three_sec_ship3_row == three_sec_ship1_row and three_sec_ship3_col == three_sec_ship1_col) or (three_sec_ship3_row == four_sec_ship1_row and three_sec_ship3_col == four_sec_ship1_col) or (three_sec_ship3_row == five_sec_ship1_row and three_sec_ship3_col == five_sec_ship1_col) or (one_sec_ship3_row == one_sec_ship2_row and one_sec_ship3_col == one_sec_ship2_col) or (one_sec_ship3_row == two_sec_ship2_row and one_sec_ship3_col == two_sec_ship2_col) or (one_sec_ship3_row == three_sec_ship2_row and one_sec_ship3_col == three_sec_ship2_col) or (one_sec_ship3_row == four_sec_ship2_row and one_sec_ship3_col == four_sec_ship2_col) or (two_sec_ship3_row == one_sec_ship2_row and two_sec_ship3_col == one_sec_ship2_col) or (two_sec_ship3_row == two_sec_ship2_row and two_sec_ship3_col == two_sec_ship2_col) or (two_sec_ship3_row == three_sec_ship2_row and two_sec_ship3_col == three_sec_ship2_col) or (two_sec_ship3_row == four_sec_ship2_row and two_sec_ship3_col == four_sec_ship2_col) or (three_sec_ship3_row == one_sec_ship2_row and three_sec_ship3_col == one_sec_ship2_col) or (three_sec_ship3_row == two_sec_ship2_row and three_sec_ship3_col == two_sec_ship2_col) or (three_sec_ship3_row == three_sec_ship2_row and three_sec_ship3_col == three_sec_ship2_col) or (three_sec_ship3_row == four_sec_ship2_row and three_sec_ship3_col == four_sec_ship2_col):
				turn_player = 14
				break
			else:
				turn_player = 25
		elif ship3_one_direc == 4: # west
			one_sec_ship3_row = ship3_row
			one_sec_ship3_col = ship3_col
			two_sec_ship3_row = ship3_row
			two_sec_ship3_col = ship3_col - 1
			three_sec_ship3_row = ship3_row
			three_sec_ship3_col = ship3_col - 2
			if two_sec_ship3_col < 0 or three_sec_ship3_row < 0:
				turn_player = 14
				break
			if (one_sec_ship3_row == one_sec_ship1_row and one_sec_ship3_col == one_sec_ship1_col) or (one_sec_ship3_row == two_sec_ship1_row and one_sec_ship3_col == two_sec_ship1_col) or (one_sec_ship3_row == three_sec_ship1_row and one_sec_ship3_col == three_sec_ship1_col) or (one_sec_ship3_row == four_sec_ship1_row and one_sec_ship3_col == four_sec_ship1_col) or (one_sec_ship3_row == five_sec_ship1_row and one_sec_ship3_col == five_sec_ship1_col) or (two_sec_ship3_row == one_sec_ship1_row and two_sec_ship3_col == one_sec_ship1_col) or (two_sec_ship3_row == two_sec_ship1_row and two_sec_ship3_col == two_sec_ship1_col) or (two_sec_ship3_row == three_sec_ship1_row and two_sec_ship3_col == three_sec_ship1_col) or (two_sec_ship3_row == four_sec_ship1_row and two_sec_ship3_col == four_sec_ship1_col) or (two_sec_ship3_row == five_sec_ship1_row and two_sec_ship3_col == five_sec_ship1_col) or (three_sec_ship3_row == one_sec_ship1_row and three_sec_ship3_col == one_sec_ship1_col) or (three_sec_ship3_row == two_sec_ship1_row and three_sec_ship3_col == two_sec_ship1_col) or (three_sec_ship3_row == three_sec_ship1_row and three_sec_ship3_col == three_sec_ship1_col) or (three_sec_ship3_row == four_sec_ship1_row and three_sec_ship3_col == four_sec_ship1_col) or (three_sec_ship3_row == five_sec_ship1_row and three_sec_ship3_col == five_sec_ship1_col) or (one_sec_ship3_row == one_sec_ship2_row and one_sec_ship3_col == one_sec_ship2_col) or (one_sec_ship3_row == two_sec_ship2_row and one_sec_ship3_col == two_sec_ship2_col) or (one_sec_ship3_row == three_sec_ship2_row and one_sec_ship3_col == three_sec_ship2_col) or (one_sec_ship3_row == four_sec_ship2_row and one_sec_ship3_col == four_sec_ship2_col) or (two_sec_ship3_row == one_sec_ship2_row and two_sec_ship3_col == one_sec_ship2_col) or (two_sec_ship3_row == two_sec_ship2_row and two_sec_ship3_col == two_sec_ship2_col) or (two_sec_ship3_row == three_sec_ship2_row and two_sec_ship3_col == three_sec_ship2_col) or (two_sec_ship3_row == four_sec_ship2_row and two_sec_ship3_col == four_sec_ship2_col) or (three_sec_ship3_row == one_sec_ship2_row and three_sec_ship3_col == one_sec_ship2_col) or (three_sec_ship3_row == two_sec_ship2_row and three_sec_ship3_col == two_sec_ship2_col) or (three_sec_ship3_row == three_sec_ship2_row and three_sec_ship3_col == three_sec_ship2_col) or (three_sec_ship3_row == four_sec_ship2_row and three_sec_ship3_col == four_sec_ship2_col):
				turn_player = 14
				break
			else:
				turn_player = 25
		else:
			turn_player = 14

	ship3_two_direc =randint(1,4)
	while turn_player == 15:
		one_direc = randint(1,4)
		ship3_two_direc =randint(1,4)
		turn_player = 25

	while turn_player == 25: # Decides the ship
		ship3_row2 = random_row(board2) # 3 space ship
		ship3_col2 = random_col(board2)
		if ship3_two_direc == 1: # north
			one_sec_ship3_row2 = ship3_row2  # The same row is selected
			one_sec_ship3_col2 = ship3_col2  #the same col is selected
			two_sec_ship3_row2 = ship3_row2 - 1 #the row up is selected
			two_sec_ship3_col2 = ship3_col2 #the same col is selected
			three_sec_ship3_row2 = ship3_row2 - 2
			three_sec_ship3_col2 = ship3_col2
			if two_sec_ship3_row2 < 0 or three_sec_ship3_row2 < 0: # If the row selected is outside of the bounds...
				turn_player = 15  #restarts the random ship selection for its location
				break
			if (one_sec_ship3_row2 == one_sec_ship1_row2 and one_sec_ship3_col2 == one_sec_ship1_col2) or (one_sec_ship3_row2 == two_sec_ship1_row2 and one_sec_ship3_col2 == two_sec_ship1_col2) or (one_sec_ship3_row2 == three_sec_ship1_row2 and one_sec_ship3_col2 == three_sec_ship1_col2) or (one_sec_ship3_row2 == four_sec_ship1_row2 and one_sec_ship3_col2 == four_sec_ship1_col2) or (one_sec_ship3_row2 == five_sec_ship1_row2 and one_sec_ship3_col2 == five_sec_ship1_col2) or (two_sec_ship3_row2 == one_sec_ship1_row2 and two_sec_ship3_col2 == one_sec_ship1_col2) or (two_sec_ship3_row2 == two_sec_ship1_row2 and two_sec_ship3_col2 == two_sec_ship1_col2) or (two_sec_ship3_row2 == three_sec_ship1_row2 and two_sec_ship3_col2 == three_sec_ship1_col2) or (two_sec_ship3_row2 == four_sec_ship1_row2 and two_sec_ship3_col2 == four_sec_ship1_col2) or (two_sec_ship3_row2 == five_sec_ship1_row2 and two_sec_ship3_col2 == five_sec_ship1_col2) or (three_sec_ship3_row2 == one_sec_ship1_row2 and three_sec_ship3_col2 == one_sec_ship1_col2) or (three_sec_ship3_row2 == two_sec_ship1_row2 and three_sec_ship3_col2 == two_sec_ship1_col2) or (three_sec_ship3_row2 == three_sec_ship1_row2 and three_sec_ship3_col2 == three_sec_ship1_col2) or (three_sec_ship3_row2 == four_sec_ship1_row2 and three_sec_ship3_col2 == four_sec_ship1_col2) or (three_sec_ship3_row2 == five_sec_ship1_row2 and three_sec_ship3_col2 == five_sec_ship1_col2) or (one_sec_ship3_row2 == one_sec_ship2_row2 and one_sec_ship3_col2 == one_sec_ship2_col2) or (one_sec_ship3_row2 == two_sec_ship2_row2 and one_sec_ship3_col2 == two_sec_ship2_col2) or (one_sec_ship3_row2 == three_sec_ship2_row2 and one_sec_ship3_col2 == three_sec_ship2_col2) or (one_sec_ship3_row2 == four_sec_ship2_row2 and one_sec_ship3_col2 == four_sec_ship2_col2) or (two_sec_ship3_row2 == one_sec_ship2_row2 and two_sec_ship3_col2 == one_sec_ship2_col2) or (two_sec_ship3_row2 == two_sec_ship2_row2 and two_sec_ship3_col2 == two_sec_ship2_col2) or (two_sec_ship3_row2 == three_sec_ship2_row2 and two_sec_ship3_col2 == three_sec_ship2_col2) or (two_sec_ship3_row2 == four_sec_ship2_row2 and two_sec_ship3_col2 == four_sec_ship2_col2) or (three_sec_ship3_row2 == one_sec_ship2_row2 and three_sec_ship3_col2 == one_sec_ship2_col2) or (three_sec_ship3_row2 == two_sec_ship2_row2 and three_sec_ship3_col2 == two_sec_ship2_col2) or (three_sec_ship3_row2 == three_sec_ship2_row2 and three_sec_ship3_col2 == three_sec_ship2_col2) or (three_sec_ship3_row2 == four_sec_ship2_row2 and three_sec_ship3_col2 == four_sec_ship2_col2):
				turn_player = 15
				break
			else: # If the row selected is inside of the bounds...
				turn_player = 0 # Begins the selection of player 2's ship's second component
		elif ship3_two_direc == 2: # east
			one_sec_ship3_row2 = ship3_row2
			one_sec_ship3_col2 = ship3_col2
			two_sec_ship3_row2 = ship3_row2
			two_sec_ship3_col2 = ship3_col2 + 1
			three_sec_ship3_row2 = ship3_row2
			three_sec_ship3_col2 = ship3_col2 + 2
			if two_sec_ship3_col2 > 9 or three_sec_ship3_col2 > 9:
				turn_player = 15
				break
			if (one_sec_ship3_row2 == one_sec_ship1_row2 and one_sec_ship3_col2 == one_sec_ship1_col2) or (one_sec_ship3_row2 == two_sec_ship1_row2 and one_sec_ship3_col2 == two_sec_ship1_col2) or (one_sec_ship3_row2 == three_sec_ship1_row2 and one_sec_ship3_col2 == three_sec_ship1_col2) or (one_sec_ship3_row2 == four_sec_ship1_row2 and one_sec_ship3_col2 == four_sec_ship1_col2) or (one_sec_ship3_row2 == five_sec_ship1_row2 and one_sec_ship3_col2 == five_sec_ship1_col2) or (two_sec_ship3_row2 == one_sec_ship1_row2 and two_sec_ship3_col2 == one_sec_ship1_col2) or (two_sec_ship3_row2 == two_sec_ship1_row2 and two_sec_ship3_col2 == two_sec_ship1_col2) or (two_sec_ship3_row2 == three_sec_ship1_row2 and two_sec_ship3_col2 == three_sec_ship1_col2) or (two_sec_ship3_row2 == four_sec_ship1_row2 and two_sec_ship3_col2 == four_sec_ship1_col2) or (two_sec_ship3_row2 == five_sec_ship1_row2 and two_sec_ship3_col2 == five_sec_ship1_col2) or (three_sec_ship3_row2 == one_sec_ship1_row2 and three_sec_ship3_col2 == one_sec_ship1_col2) or (three_sec_ship3_row2 == two_sec_ship1_row2 and three_sec_ship3_col2 == two_sec_ship1_col2) or (three_sec_ship3_row2 == three_sec_ship1_row2 and three_sec_ship3_col2 == three_sec_ship1_col2) or (three_sec_ship3_row2 == four_sec_ship1_row2 and three_sec_ship3_col2 == four_sec_ship1_col2) or (three_sec_ship3_row2 == five_sec_ship1_row2 and three_sec_ship3_col2 == five_sec_ship1_col2) or (one_sec_ship3_row2 == one_sec_ship2_row2 and one_sec_ship3_col2 == one_sec_ship2_col2) or (one_sec_ship3_row2 == two_sec_ship2_row2 and one_sec_ship3_col2 == two_sec_ship2_col2) or (one_sec_ship3_row2 == three_sec_ship2_row2 and one_sec_ship3_col2 == three_sec_ship2_col2) or (one_sec_ship3_row2 == four_sec_ship2_row2 and one_sec_ship3_col2 == four_sec_ship2_col2) or (two_sec_ship3_row2 == one_sec_ship2_row2 and two_sec_ship3_col2 == one_sec_ship2_col2) or (two_sec_ship3_row2 == two_sec_ship2_row2 and two_sec_ship3_col2 == two_sec_ship2_col2) or (two_sec_ship3_row2 == three_sec_ship2_row2 and two_sec_ship3_col2 == three_sec_ship2_col2) or (two_sec_ship3_row2 == four_sec_ship2_row2 and two_sec_ship3_col2 == four_sec_ship2_col2) or (three_sec_ship3_row2 == one_sec_ship2_row2 and three_sec_ship3_col2 == one_sec_ship2_col2) or (three_sec_ship3_row2 == two_sec_ship2_row2 and three_sec_ship3_col2 == two_sec_ship2_col2) or (three_sec_ship3_row2 == three_sec_ship2_row2 and three_sec_ship3_col2 == three_sec_ship2_col2) or (three_sec_ship3_row2 == four_sec_ship2_row2 and three_sec_ship3_col2 == four_sec_ship2_col2):
				turn_player = 15
				break
			else:
				turn_player = 0
		elif ship3_two_direc == 3:
			one_sec_ship3_row2 = ship3_row2
			one_sec_ship3_col2 = ship3_col2
			two_sec_ship3_row2 = ship3_row2 + 1
			two_sec_ship3_col2 = ship3_col2
			three_sec_ship3_row2 = ship3_row2 + 2
			three_sec_ship3_col2 = ship3_col2
			if two_sec_ship3_row2 > 9 or three_sec_ship3_col2 > 9:
				turn_player = 15
				break
			if (one_sec_ship3_row2 == one_sec_ship1_row2 and one_sec_ship3_col2 == one_sec_ship1_col2) or (one_sec_ship3_row2 == two_sec_ship1_row2 and one_sec_ship3_col2 == two_sec_ship1_col2) or (one_sec_ship3_row2 == three_sec_ship1_row2 and one_sec_ship3_col2 == three_sec_ship1_col2) or (one_sec_ship3_row2 == four_sec_ship1_row2 and one_sec_ship3_col2 == four_sec_ship1_col2) or (one_sec_ship3_row2 == five_sec_ship1_row2 and one_sec_ship3_col2 == five_sec_ship1_col2) or (two_sec_ship3_row2 == one_sec_ship1_row2 and two_sec_ship3_col2 == one_sec_ship1_col2) or (two_sec_ship3_row2 == two_sec_ship1_row2 and two_sec_ship3_col2 == two_sec_ship1_col2) or (two_sec_ship3_row2 == three_sec_ship1_row2 and two_sec_ship3_col2 == three_sec_ship1_col2) or (two_sec_ship3_row2 == four_sec_ship1_row2 and two_sec_ship3_col2 == four_sec_ship1_col2) or (two_sec_ship3_row2 == five_sec_ship1_row2 and two_sec_ship3_col2 == five_sec_ship1_col2) or (three_sec_ship3_row2 == one_sec_ship1_row2 and three_sec_ship3_col2 == one_sec_ship1_col2) or (three_sec_ship3_row2 == two_sec_ship1_row2 and three_sec_ship3_col2 == two_sec_ship1_col2) or (three_sec_ship3_row2 == three_sec_ship1_row2 and three_sec_ship3_col2 == three_sec_ship1_col2) or (three_sec_ship3_row2 == four_sec_ship1_row2 and three_sec_ship3_col2 == four_sec_ship1_col2) or (three_sec_ship3_row2 == five_sec_ship1_row2 and three_sec_ship3_col2 == five_sec_ship1_col2) or (one_sec_ship3_row2 == one_sec_ship2_row2 and one_sec_ship3_col2 == one_sec_ship2_col2) or (one_sec_ship3_row2 == two_sec_ship2_row2 and one_sec_ship3_col2 == two_sec_ship2_col2) or (one_sec_ship3_row2 == three_sec_ship2_row2 and one_sec_ship3_col2 == three_sec_ship2_col2) or (one_sec_ship3_row2 == four_sec_ship2_row2 and one_sec_ship3_col2 == four_sec_ship2_col2) or (two_sec_ship3_row2 == one_sec_ship2_row2 and two_sec_ship3_col2 == one_sec_ship2_col2) or (two_sec_ship3_row2 == two_sec_ship2_row2 and two_sec_ship3_col2 == two_sec_ship2_col2) or (two_sec_ship3_row2 == three_sec_ship2_row2 and two_sec_ship3_col2 == three_sec_ship2_col2) or (two_sec_ship3_row2 == four_sec_ship2_row2 and two_sec_ship3_col2 == four_sec_ship2_col2) or (three_sec_ship3_row2 == one_sec_ship2_row2 and three_sec_ship3_col2 == one_sec_ship2_col2) or (three_sec_ship3_row2 == two_sec_ship2_row2 and three_sec_ship3_col2 == two_sec_ship2_col2) or (three_sec_ship3_row2 == three_sec_ship2_row2 and three_sec_ship3_col2 == three_sec_ship2_col2) or (three_sec_ship3_row2 == four_sec_ship2_row2 and three_sec_ship3_col2 == four_sec_ship2_col2):
				turn_player = 15
				break
			else:
				turn_player = 0
		elif ship3_two_direc == 4:
			one_sec_ship3_row2 = ship3_row2
			one_sec_ship3_col2 = ship3_col2
			two_sec_ship3_row2 = ship3_row2
			two_sec_ship3_col2 = ship3_col2 - 1
			three_sec_ship3_row2 = ship3_row2
			three_sec_ship3_col2 = ship3_col2 - 1
			if two_sec_ship3_col2 < 0 or three_sec_ship3_col2 < 0:
				turn_player = 15
				break
			if (one_sec_ship3_row2 == one_sec_ship1_row2 and one_sec_ship3_col2 == one_sec_ship1_col2) or (one_sec_ship3_row2 == two_sec_ship1_row2 and one_sec_ship3_col2 == two_sec_ship1_col2) or (one_sec_ship3_row2 == three_sec_ship1_row2 and one_sec_ship3_col2 == three_sec_ship1_col2) or (one_sec_ship3_row2 == four_sec_ship1_row2 and one_sec_ship3_col2 == four_sec_ship1_col2) or (one_sec_ship3_row2 == five_sec_ship1_row2 and one_sec_ship3_col2 == five_sec_ship1_col2) or (two_sec_ship3_row2 == one_sec_ship1_row2 and two_sec_ship3_col2 == one_sec_ship1_col2) or (two_sec_ship3_row2 == two_sec_ship1_row2 and two_sec_ship3_col2 == two_sec_ship1_col2) or (two_sec_ship3_row2 == three_sec_ship1_row2 and two_sec_ship3_col2 == three_sec_ship1_col2) or (two_sec_ship3_row2 == four_sec_ship1_row2 and two_sec_ship3_col2 == four_sec_ship1_col2) or (two_sec_ship3_row2 == five_sec_ship1_row2 and two_sec_ship3_col2 == five_sec_ship1_col2) or (three_sec_ship3_row2 == one_sec_ship1_row2 and three_sec_ship3_col2 == one_sec_ship1_col2) or (three_sec_ship3_row2 == two_sec_ship1_row2 and three_sec_ship3_col2 == two_sec_ship1_col2) or (three_sec_ship3_row2 == three_sec_ship1_row2 and three_sec_ship3_col2 == three_sec_ship1_col2) or (three_sec_ship3_row2 == four_sec_ship1_row2 and three_sec_ship3_col2 == four_sec_ship1_col2) or (three_sec_ship3_row2 == five_sec_ship1_row2 and three_sec_ship3_col2 == five_sec_ship1_col2) or (one_sec_ship3_row2 == one_sec_ship2_row2 and one_sec_ship3_col2 == one_sec_ship2_col2) or (one_sec_ship3_row2 == two_sec_ship2_row2 and one_sec_ship3_col2 == two_sec_ship2_col2) or (one_sec_ship3_row2 == three_sec_ship2_row2 and one_sec_ship3_col2 == three_sec_ship2_col2) or (one_sec_ship3_row2 == four_sec_ship2_row2 and one_sec_ship3_col2 == four_sec_ship2_col2) or (two_sec_ship3_row2 == one_sec_ship2_row2 and two_sec_ship3_col2 == one_sec_ship2_col2) or (two_sec_ship3_row2 == two_sec_ship2_row2 and two_sec_ship3_col2 == two_sec_ship2_col2) or (two_sec_ship3_row2 == three_sec_ship2_row2 and two_sec_ship3_col2 == three_sec_ship2_col2) or (two_sec_ship3_row2 == four_sec_ship2_row2 and two_sec_ship3_col2 == four_sec_ship2_col2) or (three_sec_ship3_row2 == one_sec_ship2_row2 and three_sec_ship3_col2 == one_sec_ship2_col2) or (three_sec_ship3_row2 == two_sec_ship2_row2 and three_sec_ship3_col2 == two_sec_ship2_col2) or (three_sec_ship3_row2 == three_sec_ship2_row2 and three_sec_ship3_col2 == three_sec_ship2_col2) or (three_sec_ship3_row2 == four_sec_ship2_row2 and three_sec_ship3_col2 == four_sec_ship2_col2):
				turn_player = 15
				break
			else:
				turn_player = 0
		else:
			turn_player = 15

	ship4_one_direc = randint(1,4)
	while turn_player == 16:
		ship4_one_direc = randint(1,4)
		two_direc =randint(1,4)
		turn_player = 0


	while turn_player == 0: # Decides the location of player 1's ship's second component
		if ship4_one_direc == 1: # north
			one_sec_ship4_row = ship4_row  # The row is selected
			one_sec_ship4_col = ship4_col # The same column is selected
			two_sec_ship4_row = ship4_row - 1 # the row above is selected
			two_sec_ship4_col = ship4_col
			if two_sec_ship4_row < 0: # If the row selected is outside of the bounds...
				turn_player = 16 #restarts the
				break
			if (one_sec_ship4_row == one_sec_ship1_row and one_sec_ship4_col == one_sec_ship1_col) or (one_sec_ship4_row == two_sec_ship1_row and one_sec_ship4_col == two_sec_ship1_col) or (one_sec_ship4_row == three_sec_ship1_row and one_sec_ship4_col == three_sec_ship1_col) or (one_sec_ship4_row == four_sec_ship1_row and one_sec_ship4_col == four_sec_ship1_col) or (one_sec_ship4_row == five_sec_ship1_row and one_sec_ship4_col == five_sec_ship1_col) or (one_sec_ship4_row == one_sec_ship2_row and one_sec_ship2_col == one_sec_ship2_col) or (one_sec_ship4_row == two_sec_ship2_row and one_sec_ship2_col == two_sec_ship2_col) or (one_sec_ship4_row == three_sec_ship2_row and one_sec_ship2_col == three_sec_ship2_col) or (one_sec_ship4_row == four_sec_ship2_row and one_sec_ship2_col == four_sec_ship2_col) or (one_sec_ship4_row == one_sec_ship3_row and one_sec_ship2_col == one_sec_ship3_col) or (one_sec_ship4_row == two_sec_ship3_row and one_sec_ship2_col == two_sec_ship3_col) or (one_sec_ship4_row == three_sec_ship3_row and one_sec_ship2_col == three_sec_ship3_col) or (two_sec_ship4_row == one_sec_ship1_row and two_sec_ship4_col == one_sec_ship1_col) or (two_sec_ship4_row == two_sec_ship1_row and two_sec_ship4_col == two_sec_ship1_col) or (two_sec_ship4_row == three_sec_ship1_row and two_sec_ship4_col == three_sec_ship1_col) or (two_sec_ship4_row == four_sec_ship1_row and two_sec_ship4_col == four_sec_ship1_col) or (two_sec_ship4_row == five_sec_ship1_row and two_sec_ship4_col == five_sec_ship1_col) or (two_sec_ship4_row == one_sec_ship2_row and two_sec_ship2_col == one_sec_ship2_col) or (two_sec_ship4_row == two_sec_ship2_row and two_sec_ship2_col == two_sec_ship2_col) or (two_sec_ship4_row == three_sec_ship2_row and two_sec_ship2_col == three_sec_ship2_col) or (two_sec_ship4_row == four_sec_ship2_row and two_sec_ship2_col == four_sec_ship2_col) or (two_sec_ship4_row == one_sec_ship3_row and two_sec_ship2_col == one_sec_ship3_col) or (two_sec_ship4_row == two_sec_ship3_row and two_sec_ship2_col == two_sec_ship3_col) or (two_sec_ship4_row == three_sec_ship3_row and two_sec_ship2_col == three_sec_ship3_col):
				turn_player = 16
				break
			else: # If the row selected is inside of the bounds...
				turn_player = 1 # Begins the selection of player 2's ship's second component
		elif ship4_one_direc == 2: # east
			one_sec_ship4_row = ship4_row
			one_sec_ship4_col = ship4_col
			two_sec_ship4_row = ship4_row
			two_sec_ship4_col = ship4_col - 1
			if two_sec_ship4_col > 9:
				turn_player = 16
				break
			if (one_sec_ship4_row == one_sec_ship1_row and one_sec_ship4_col == one_sec_ship1_col) or (one_sec_ship4_row == two_sec_ship1_row and one_sec_ship4_col == two_sec_ship1_col) or (one_sec_ship4_row == three_sec_ship1_row and one_sec_ship4_col == three_sec_ship1_col) or (one_sec_ship4_row == four_sec_ship1_row and one_sec_ship4_col == four_sec_ship1_col) or (one_sec_ship4_row == five_sec_ship1_row and one_sec_ship4_col == five_sec_ship1_col) or (one_sec_ship4_row == one_sec_ship2_row and one_sec_ship2_col == one_sec_ship2_col) or (one_sec_ship4_row == two_sec_ship2_row and one_sec_ship2_col == two_sec_ship2_col) or (one_sec_ship4_row == three_sec_ship2_row and one_sec_ship2_col == three_sec_ship2_col) or (one_sec_ship4_row == four_sec_ship2_row and one_sec_ship2_col == four_sec_ship2_col) or (one_sec_ship4_row == one_sec_ship3_row and one_sec_ship2_col == one_sec_ship3_col) or (one_sec_ship4_row == two_sec_ship3_row and one_sec_ship2_col == two_sec_ship3_col) or (one_sec_ship4_row == three_sec_ship3_row and one_sec_ship2_col == three_sec_ship3_col) or (two_sec_ship4_row == one_sec_ship1_row and two_sec_ship4_col == one_sec_ship1_col) or (two_sec_ship4_row == two_sec_ship1_row and two_sec_ship4_col == two_sec_ship1_col) or (two_sec_ship4_row == three_sec_ship1_row and two_sec_ship4_col == three_sec_ship1_col) or (two_sec_ship4_row == four_sec_ship1_row and two_sec_ship4_col == four_sec_ship1_col) or (two_sec_ship4_row == five_sec_ship1_row and two_sec_ship4_col == five_sec_ship1_col) or (two_sec_ship4_row == one_sec_ship2_row and two_sec_ship2_col == one_sec_ship2_col) or (two_sec_ship4_row == two_sec_ship2_row and two_sec_ship2_col == two_sec_ship2_col) or (two_sec_ship4_row == three_sec_ship2_row and two_sec_ship2_col == three_sec_ship2_col) or (two_sec_ship4_row == four_sec_ship2_row and two_sec_ship2_col == four_sec_ship2_col) or (two_sec_ship4_row == one_sec_ship3_row and two_sec_ship2_col == one_sec_ship3_col) or (two_sec_ship4_row == two_sec_ship3_row and two_sec_ship2_col == two_sec_ship3_col) or (two_sec_ship4_row == three_sec_ship3_row and two_sec_ship2_col == three_sec_ship3_col):
				turn_player = 16
				break
			else:
				turn_player = 1
		elif ship4_one_direc == 3: # south
			one_sec_ship4_row = ship4_row
			one_sec_ship4_col = ship4_col
			two_sec_ship4_row = ship4_row + 1
			two_sec_ship4_col = ship4_col
			if one_sec_ship4_row > 9:
				turn_player = 16
				break
			if (one_sec_ship4_row == one_sec_ship1_row and one_sec_ship4_col == one_sec_ship1_col) or (one_sec_ship4_row == two_sec_ship1_row and one_sec_ship4_col == two_sec_ship1_col) or (one_sec_ship4_row == three_sec_ship1_row and one_sec_ship4_col == three_sec_ship1_col) or (one_sec_ship4_row == four_sec_ship1_row and one_sec_ship4_col == four_sec_ship1_col) or (one_sec_ship4_row == five_sec_ship1_row and one_sec_ship4_col == five_sec_ship1_col) or (one_sec_ship4_row == one_sec_ship2_row and one_sec_ship2_col == one_sec_ship2_col) or (one_sec_ship4_row == two_sec_ship2_row and one_sec_ship2_col == two_sec_ship2_col) or (one_sec_ship4_row == three_sec_ship2_row and one_sec_ship2_col == three_sec_ship2_col) or (one_sec_ship4_row == four_sec_ship2_row and one_sec_ship2_col == four_sec_ship2_col) or (one_sec_ship4_row == one_sec_ship3_row and one_sec_ship2_col == one_sec_ship3_col) or (one_sec_ship4_row == two_sec_ship3_row and one_sec_ship2_col == two_sec_ship3_col) or (one_sec_ship4_row == three_sec_ship3_row and one_sec_ship2_col == three_sec_ship3_col) or (two_sec_ship4_row == one_sec_ship1_row and two_sec_ship4_col == one_sec_ship1_col) or (two_sec_ship4_row == two_sec_ship1_row and two_sec_ship4_col == two_sec_ship1_col) or (two_sec_ship4_row == three_sec_ship1_row and two_sec_ship4_col == three_sec_ship1_col) or (two_sec_ship4_row == four_sec_ship1_row and two_sec_ship4_col == four_sec_ship1_col) or (two_sec_ship4_row == five_sec_ship1_row and two_sec_ship4_col == five_sec_ship1_col) or (two_sec_ship4_row == one_sec_ship2_row and two_sec_ship2_col == one_sec_ship2_col) or (two_sec_ship4_row == two_sec_ship2_row and two_sec_ship2_col == two_sec_ship2_col) or (two_sec_ship4_row == three_sec_ship2_row and two_sec_ship2_col == three_sec_ship2_col) or (two_sec_ship4_row == four_sec_ship2_row and two_sec_ship2_col == four_sec_ship2_col) or (two_sec_ship4_row == one_sec_ship3_row and two_sec_ship2_col == one_sec_ship3_col) or (two_sec_ship4_row == two_sec_ship3_row and two_sec_ship2_col == two_sec_ship3_col) or (two_sec_ship4_row == three_sec_ship3_row and two_sec_ship2_col == three_sec_ship3_col):
				turn_player = 16
				break
			else:
				turn_player = 1
		elif ship4_one_direc == 4: # west
			one_sec_ship4_row = ship4_row
			one_sec_ship4_col = ship4_col
			two_sec_ship4_row = ship4_row
			two_sec_ship4_col = ship4_col - 1
			if two_sec_ship4_col < 0:
				turn_player = 16
				break
			if (one_sec_ship4_row == one_sec_ship1_row and one_sec_ship4_col == one_sec_ship1_col) or (one_sec_ship4_row == two_sec_ship1_row and one_sec_ship4_col == two_sec_ship1_col) or (one_sec_ship4_row == three_sec_ship1_row and one_sec_ship4_col == three_sec_ship1_col) or (one_sec_ship4_row == four_sec_ship1_row and one_sec_ship4_col == four_sec_ship1_col) or (one_sec_ship4_row == five_sec_ship1_row and one_sec_ship4_col == five_sec_ship1_col) or (one_sec_ship4_row == one_sec_ship2_row and one_sec_ship2_col == one_sec_ship2_col) or (one_sec_ship4_row == two_sec_ship2_row and one_sec_ship2_col == two_sec_ship2_col) or (one_sec_ship4_row == three_sec_ship2_row and one_sec_ship2_col == three_sec_ship2_col) or (one_sec_ship4_row == four_sec_ship2_row and one_sec_ship2_col == four_sec_ship2_col) or (one_sec_ship4_row == one_sec_ship3_row and one_sec_ship2_col == one_sec_ship3_col) or (one_sec_ship4_row == two_sec_ship3_row and one_sec_ship2_col == two_sec_ship3_col) or (one_sec_ship4_row == three_sec_ship3_row and one_sec_ship2_col == three_sec_ship3_col) or (two_sec_ship4_row == one_sec_ship1_row and two_sec_ship4_col == one_sec_ship1_col) or (two_sec_ship4_row == two_sec_ship1_row and two_sec_ship4_col == two_sec_ship1_col) or (two_sec_ship4_row == three_sec_ship1_row and two_sec_ship4_col == three_sec_ship1_col) or (two_sec_ship4_row == four_sec_ship1_row and two_sec_ship4_col == four_sec_ship1_col) or (two_sec_ship4_row == five_sec_ship1_row and two_sec_ship4_col == five_sec_ship1_col) or (two_sec_ship4_row == one_sec_ship2_row and two_sec_ship2_col == one_sec_ship2_col) or (two_sec_ship4_row == two_sec_ship2_row and two_sec_ship2_col == two_sec_ship2_col) or (two_sec_ship4_row == three_sec_ship2_row and two_sec_ship2_col == three_sec_ship2_col) or (two_sec_ship4_row == four_sec_ship2_row and two_sec_ship2_col == four_sec_ship2_col) or (two_sec_ship4_row == one_sec_ship3_row and two_sec_ship2_col == one_sec_ship3_col) or (two_sec_ship4_row == two_sec_ship3_row and two_sec_ship2_col == two_sec_ship3_col) or (two_sec_ship4_row == three_sec_ship3_row and two_sec_ship2_col == three_sec_ship3_col):
				turn_player = 16
				break
			else:
				turn_player = 1
		else:
			turn_player = 16

	ship4_two_direc =randint(1,4)
	while turn_player == 17:
		one_direc = randint(1,4)
		ship4_two_direc =randint(1,4)
		turn_player = 1

	while turn_player == 1: # The same as above, but for ship 2
		if ship4_two_direc == 1:
			one_sec_ship4_row2 = ship4_row2
			one_sec_ship4_col2 = ship4_col2
			two_sec_ship4_row2 = ship4_row2 - 1
			two_sec_ship4_col2 = ship4_col2
			if two_sec_ship4_row2 < 0:
				turn_player = 17 # Begins the actual game
				break
			if (one_sec_ship4_row2 == one_sec_ship1_row2 and one_sec_ship4_col2 == one_sec_ship1_col2) or (one_sec_ship4_row2 == two_sec_ship1_row2 and one_sec_ship4_col2 == two_sec_ship1_col2) or (one_sec_ship4_row2 == three_sec_ship1_row2 and one_sec_ship4_col2 == three_sec_ship1_col2) or (one_sec_ship4_row2 == four_sec_ship1_row2 and one_sec_ship4_col2 == four_sec_ship1_col2) or (one_sec_ship4_row2 == five_sec_ship1_row2 and one_sec_ship4_col2 == five_sec_ship1_col2) or (one_sec_ship4_row2 == one_sec_ship2_row2 and one_sec_ship2_col2 == one_sec_ship2_col2) or (one_sec_ship4_row2 == two_sec_ship2_row2 and one_sec_ship2_col2 == two_sec_ship2_col2) or (one_sec_ship4_row2 == three_sec_ship2_row2 and one_sec_ship2_col2 == three_sec_ship2_col2) or (one_sec_ship4_row2 == four_sec_ship2_row2 and one_sec_ship2_col2 == four_sec_ship2_col2) or (one_sec_ship4_row2 == one_sec_ship3_row2 and one_sec_ship2_col2 == one_sec_ship3_col2) or (one_sec_ship4_row2 == two_sec_ship3_row2 and one_sec_ship2_col2 == two_sec_ship3_col2) or (one_sec_ship4_row2 == three_sec_ship3_row2 and one_sec_ship2_col2 == three_sec_ship3_col2) or (two_sec_ship4_row2 == one_sec_ship1_row2 and two_sec_ship4_col2 == one_sec_ship1_col2) or (two_sec_ship4_row2 == two_sec_ship1_row2 and two_sec_ship4_col2 == two_sec_ship1_col2) or (two_sec_ship4_row2 == three_sec_ship1_row2 and two_sec_ship4_col2 == three_sec_ship1_col2) or (two_sec_ship4_row2 == four_sec_ship1_row2 and two_sec_ship4_col2 == four_sec_ship1_col2) or (two_sec_ship4_row2 == five_sec_ship1_row2 and two_sec_ship4_col2 == five_sec_ship1_col2) or (two_sec_ship4_row2 == one_sec_ship2_row2 and two_sec_ship2_col2 == one_sec_ship2_col2) or (two_sec_ship4_row2 == two_sec_ship2_row2 and two_sec_ship2_col2 == two_sec_ship2_col2) or (two_sec_ship4_row2 == three_sec_ship2_row2 and two_sec_ship2_col2 == three_sec_ship2_col2) or (two_sec_ship4_row2 == four_sec_ship2_row2 and two_sec_ship2_col2 == four_sec_ship2_col2) or (two_sec_ship4_row2 == one_sec_ship3_row2 and two_sec_ship2_col2 == one_sec_ship3_col2) or (two_sec_ship4_row2 == two_sec_ship3_row2 and two_sec_ship2_col2 == two_sec_ship3_col2) or (two_sec_ship4_row2 == three_sec_ship3_row2 and two_sec_ship2_col2 == three_sec_ship3_col2):
				turn_player = 17
				break
			else:
				turn_player = 2
		elif ship4_two_direc == 2:
			one_sec_ship4_row2 = ship4_row2
			one_sec_ship4_col2 = ship4_col2
			two_sec_ship4_row2 = ship4_row2
			two_sec_ship4_col2 = ship4_col2 + 1
			if two_sec_ship4_col2 > 9:
				turn_player = 17
				break
			if (one_sec_ship4_row2 == one_sec_ship1_row2 and one_sec_ship4_col2 == one_sec_ship1_col2) or (one_sec_ship4_row2 == two_sec_ship1_row2 and one_sec_ship4_col2 == two_sec_ship1_col2) or (one_sec_ship4_row2 == three_sec_ship1_row2 and one_sec_ship4_col2 == three_sec_ship1_col2) or (one_sec_ship4_row2 == four_sec_ship1_row2 and one_sec_ship4_col2 == four_sec_ship1_col2) or (one_sec_ship4_row2 == five_sec_ship1_row2 and one_sec_ship4_col2 == five_sec_ship1_col2) or (one_sec_ship4_row2 == one_sec_ship2_row2 and one_sec_ship2_col2 == one_sec_ship2_col2) or (one_sec_ship4_row2 == two_sec_ship2_row2 and one_sec_ship2_col2 == two_sec_ship2_col2) or (one_sec_ship4_row2 == three_sec_ship2_row2 and one_sec_ship2_col2 == three_sec_ship2_col2) or (one_sec_ship4_row2 == four_sec_ship2_row2 and one_sec_ship2_col2 == four_sec_ship2_col2) or (one_sec_ship4_row2 == one_sec_ship3_row2 and one_sec_ship2_col2 == one_sec_ship3_col2) or (one_sec_ship4_row2 == two_sec_ship3_row2 and one_sec_ship2_col2 == two_sec_ship3_col2) or (one_sec_ship4_row2 == three_sec_ship3_row2 and one_sec_ship2_col2 == three_sec_ship3_col2) or (two_sec_ship4_row2 == one_sec_ship1_row2 and two_sec_ship4_col2 == one_sec_ship1_col2) or (two_sec_ship4_row2 == two_sec_ship1_row2 and two_sec_ship4_col2 == two_sec_ship1_col2) or (two_sec_ship4_row2 == three_sec_ship1_row2 and two_sec_ship4_col2 == three_sec_ship1_col2) or (two_sec_ship4_row2 == four_sec_ship1_row2 and two_sec_ship4_col2 == four_sec_ship1_col2) or (two_sec_ship4_row2 == five_sec_ship1_row2 and two_sec_ship4_col2 == five_sec_ship1_col2) or (two_sec_ship4_row2 == one_sec_ship2_row2 and two_sec_ship2_col2 == one_sec_ship2_col2) or (two_sec_ship4_row2 == two_sec_ship2_row2 and two_sec_ship2_col2 == two_sec_ship2_col2) or (two_sec_ship4_row2 == three_sec_ship2_row2 and two_sec_ship2_col2 == three_sec_ship2_col2) or (two_sec_ship4_row2 == four_sec_ship2_row2 and two_sec_ship2_col2 == four_sec_ship2_col2) or (two_sec_ship4_row2 == one_sec_ship3_row2 and two_sec_ship2_col2 == one_sec_ship3_col2) or (two_sec_ship4_row2 == two_sec_ship3_row2 and two_sec_ship2_col2 == two_sec_ship3_col2) or (two_sec_ship4_row2 == three_sec_ship3_row2 and two_sec_ship2_col2 == three_sec_ship3_col2):
				turn_player = 17
				break
			else:
				turn_player = 2
		elif ship4_two_direc == 3:
			one_sec_ship4_row2 = ship4_row2
			one_sec_ship4_col2 = ship4_col2
			two_sec_ship4_row2 = ship4_row2 + 1
			two_sec_ship4_col2 = ship4_col2
			if two_sec_ship4_row2 > 9:
				turn_player = 17
				break
			if (one_sec_ship4_row2 == one_sec_ship1_row2 and one_sec_ship4_col2 == one_sec_ship1_col2) or (one_sec_ship4_row2 == two_sec_ship1_row2 and one_sec_ship4_col2 == two_sec_ship1_col2) or (one_sec_ship4_row2 == three_sec_ship1_row2 and one_sec_ship4_col2 == three_sec_ship1_col2) or (one_sec_ship4_row2 == four_sec_ship1_row2 and one_sec_ship4_col2 == four_sec_ship1_col2) or (one_sec_ship4_row2 == five_sec_ship1_row2 and one_sec_ship4_col2 == five_sec_ship1_col2) or (one_sec_ship4_row2 == one_sec_ship2_row2 and one_sec_ship2_col2 == one_sec_ship2_col2) or (one_sec_ship4_row2 == two_sec_ship2_row2 and one_sec_ship2_col2 == two_sec_ship2_col2) or (one_sec_ship4_row2 == three_sec_ship2_row2 and one_sec_ship2_col2 == three_sec_ship2_col2) or (one_sec_ship4_row2 == four_sec_ship2_row2 and one_sec_ship2_col2 == four_sec_ship2_col2) or (one_sec_ship4_row2 == one_sec_ship3_row2 and one_sec_ship2_col2 == one_sec_ship3_col2) or (one_sec_ship4_row2 == two_sec_ship3_row2 and one_sec_ship2_col2 == two_sec_ship3_col2) or (one_sec_ship4_row2 == three_sec_ship3_row2 and one_sec_ship2_col2 == three_sec_ship3_col2) or (two_sec_ship4_row2 == one_sec_ship1_row2 and two_sec_ship4_col2 == one_sec_ship1_col2) or (two_sec_ship4_row2 == two_sec_ship1_row2 and two_sec_ship4_col2 == two_sec_ship1_col2) or (two_sec_ship4_row2 == three_sec_ship1_row2 and two_sec_ship4_col2 == three_sec_ship1_col2) or (two_sec_ship4_row2 == four_sec_ship1_row2 and two_sec_ship4_col2 == four_sec_ship1_col2) or (two_sec_ship4_row2 == five_sec_ship1_row2 and two_sec_ship4_col2 == five_sec_ship1_col2) or (two_sec_ship4_row2 == one_sec_ship2_row2 and two_sec_ship2_col2 == one_sec_ship2_col2) or (two_sec_ship4_row2 == two_sec_ship2_row2 and two_sec_ship2_col2 == two_sec_ship2_col2) or (two_sec_ship4_row2 == three_sec_ship2_row2 and two_sec_ship2_col2 == three_sec_ship2_col2) or (two_sec_ship4_row2 == four_sec_ship2_row2 and two_sec_ship2_col2 == four_sec_ship2_col2) or (two_sec_ship4_row2 == one_sec_ship3_row2 and two_sec_ship2_col2 == one_sec_ship3_col2) or (two_sec_ship4_row2 == two_sec_ship3_row2 and two_sec_ship2_col2 == two_sec_ship3_col2) or (two_sec_ship4_row2 == three_sec_ship3_row2 and two_sec_ship2_col2 == three_sec_ship3_col2):
				turn_player = 17
				break
			else:
				turn_player = 2
		elif ship4_two_direc == 4:
			one_sec_ship4_row2 = ship4_row2
			one_sec_ship4_col2 = ship4_col2
			two_sec_ship4_row2 = ship4_row2
			two_sec_ship4_col2 = ship4_col2 -1
			if two_sec_ship4_col2 < 0:
				turn_player = 17
				break
			if (one_sec_ship4_row2 == one_sec_ship1_row2 and one_sec_ship4_col2 == one_sec_ship1_col2) or (one_sec_ship4_row2 == two_sec_ship1_row2 and one_sec_ship4_col2 == two_sec_ship1_col2) or (one_sec_ship4_row2 == three_sec_ship1_row2 and one_sec_ship4_col2 == three_sec_ship1_col2) or (one_sec_ship4_row2 == four_sec_ship1_row2 and one_sec_ship4_col2 == four_sec_ship1_col2) or (one_sec_ship4_row2 == five_sec_ship1_row2 and one_sec_ship4_col2 == five_sec_ship1_col2) or (one_sec_ship4_row2 == one_sec_ship2_row2 and one_sec_ship2_col2 == one_sec_ship2_col2) or (one_sec_ship4_row2 == two_sec_ship2_row2 and one_sec_ship2_col2 == two_sec_ship2_col2) or (one_sec_ship4_row2 == three_sec_ship2_row2 and one_sec_ship2_col2 == three_sec_ship2_col2) or (one_sec_ship4_row2 == four_sec_ship2_row2 and one_sec_ship2_col2 == four_sec_ship2_col2) or (one_sec_ship4_row2 == one_sec_ship3_row2 and one_sec_ship2_col2 == one_sec_ship3_col2) or (one_sec_ship4_row2 == two_sec_ship3_row2 and one_sec_ship2_col2 == two_sec_ship3_col2) or (one_sec_ship4_row2 == three_sec_ship3_row2 and one_sec_ship2_col2 == three_sec_ship3_col2) or (two_sec_ship4_row2 == one_sec_ship1_row2 and two_sec_ship4_col2 == one_sec_ship1_col2) or (two_sec_ship4_row2 == two_sec_ship1_row2 and two_sec_ship4_col2 == two_sec_ship1_col2) or (two_sec_ship4_row2 == three_sec_ship1_row2 and two_sec_ship4_col2 == three_sec_ship1_col2) or (two_sec_ship4_row2 == four_sec_ship1_row2 and two_sec_ship4_col2 == four_sec_ship1_col2) or (two_sec_ship4_row2 == five_sec_ship1_row2 and two_sec_ship4_col2 == five_sec_ship1_col2) or (two_sec_ship4_row2 == one_sec_ship2_row2 and two_sec_ship2_col2 == one_sec_ship2_col2) or (two_sec_ship4_row2 == two_sec_ship2_row2 and two_sec_ship2_col2 == two_sec_ship2_col2) or (two_sec_ship4_row2 == three_sec_ship2_row2 and two_sec_ship2_col2 == three_sec_ship2_col2) or (two_sec_ship4_row2 == four_sec_ship2_row2 and two_sec_ship2_col2 == four_sec_ship2_col2) or (two_sec_ship4_row2 == one_sec_ship3_row2 and two_sec_ship2_col2 == one_sec_ship3_col2) or (two_sec_ship4_row2 == two_sec_ship3_row2 and two_sec_ship2_col2 == two_sec_ship3_col2) or (two_sec_ship4_row2 == three_sec_ship3_row2 and two_sec_ship2_col2 == three_sec_ship3_col2):
				turn_player = 17
				break
			else:
				turn_player = 2
		else:
			turn_player = 17
	
	


	while turn_player == 2:
		guess_col = verify_int(raw_input("Guess Col:"))
		guess_col = guess_col -1
		guess_row = verify_int(raw_input("Guess Row:"))
		guess_row = guess_row - 1
		guess = 0 #for the first turn
		print "Player 1's turn"
		print_board(board)
		if (guess_row == one_sec_ship4_row and guess_col == one_sec_ship4_col) or (guess_row == two_sec_ship4_row and guess_col == two_sec_ship4_col):
			board[guess_row][guess_col] = "X"
		if board[one_sec_ship4_row][one_sec_ship4_col] == "X" and board[two_sec_ship4_row][two_sec_ship4_col] == "X":
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
		if (guess_row2 == one_sec_ship4_row2 and guess_col2 == one_sec_ship4_col2) or (guess_row2 == two_sec_ship4_row2 and guess_col2 == two_sec_ship4_col2):
			board2[guess_row2][guess_col2] == "X"
		if board2[one_sec_ship4_row2][one_sec_ship4_col2] == "X"  and board2[two_sec_ship4_row2][two_sec_ship4_col2] == "X":
			print "Color  me surprised, you actually won."
			turn_player = 5
			break
		if (guess_row2 < 0 or guess_row2 > 10) or (guess_col2 < 0 or guess_col2 > 10):
			print "That's not even on the board."
		elif board2[guess_row2][guess_col2] == "0" or board2[guess_row2][guess_col2] == "X":
			print "You guessed that one already."
		else:
			print "You missed."
			board2[guess_row2][guess_col2] = "0"
		print"Player 2's board"
		print_board(board)
		print "Player 1's board"
		print_board2(board2)
		print "Player 1's turn"
		turn_player = 2

	if turn_player == 4:
		print "Player 1 wins"

	if turn_player == 5:
		print "player 2 wins"