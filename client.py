import http.client
import json
import time
import numpy as np
import requests

ROW_NUM = 6
COL_NUM = 9



def print_board(board):
	print(np.flip(board,0))

def create_board():
	board = np.zeros((ROW_NUM,COL_NUM))
	return board

def enter_name():
	name= input("Please enter your name:")
	return name



def display_board(board):
	print(np.flip(board,0))

def status(game_over,turn):
	if game_over and turn ==0:
		print('Player One Won!!!')
	if game_over and turn ==1:
		print('Player Two Won!!!')

def game_over():
	pass

#board= create_board()
state = {
    'playersturn':3,
    #"board":board,
    "game_over":"no",
    "Player":0,
    } 

try:
	name = str(enter_name())
    break
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

r = requests.post('http://127.0.0.1:5000/name/', data={'name': name})


state=json.loads(r.text)
player=state["Player"]
player=int(player)
	#hack on player number fix later.
if player ==0:
	print("you are player 2")
else:
	print("you are player 1")
#print(player)


while state["game_over"]==False:

		r = requests.get('http://127.0.0.1:5000/state/')#api/v1/
		#print("state is ")
		state= json.loads(r.text)

		if 	state["playersturn"]==player:
			#get a move and send it off
			print("They moved")
			print_board(state['board'])
			try:
				move = int(input("pick a column (0-8)"))
        	break
        		except ValueError:
        			print("Oops!  That was no valid number.  Try again...")

			r = requests.get('http://127.0.0.1:5000/move?column='+str(move))
			#see if valid move cam back
			#print out board
			#
			#print(r.text)
			state= json.loads(r.text)
		#print(r.text)
			#print(state['board'])
			print_board(state['board'])
			#print_board(board)
		
		#waiting =False
		time.sleep(1)
	
print("Game Over")
print("Winner is "+str(state["playersturn"]))


