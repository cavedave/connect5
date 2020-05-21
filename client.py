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

def player_number(play_num):
	if play_num ==1:
		print("First player waiting on second")		
	else:
		print("Second player game can start")
	pass

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

name = str(enter_name())
r = requests.post('http://127.0.0.1:5000/name/', data={'name': name})#name?name= +name)#,data=name
#http://127.0.0.1:5000/api/v1/name?name=David
#print(state["Player"])
print("r text")
#print(r.text)

state=json.loads(r.text)
player=state["Player"]
player=int(player)
print("you are player ")
print(player)

#print(r.text)
#print(state["game_over"])
#board =  create_board()

while True:
	if state["game_over"]==False:

		r = requests.get('http://127.0.0.1:5000/state/')#api/v1/
		#print("state is ")
		state= json.loads(r.text)
		#if state["myturn"]==player:
	#		print("MYTURN now we can play")
	#state= json.loads(r.text)
	#print(state["myturn"])
		#waiting =True

		#myturn=0
		#while True#myturn==1:#waiting==True:
		#state={}
		#r = requests.get('http://127.0.0.1:5000/api/v1/play')
		#print("it is your turn ")
		#state= json.loads(r.text)
		#print(r.text)
		#print(state["Player"])
			#print(type(state))'playersturn':0,
		if 	state["playersturn"]==player:
			#get a move and send it off
			print("They moved")
			print_board(state['board'])
			move = int(input("pick a column (0-8)"))
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
		time.sleep(3)
	else:
		print("Game Over")
		print("Winner is "+str(state["playersturn"]))
#name=enter_name()

#r = requests.get('http://127.0.0.1:5000/api/v1/resources/books/all')#https://httpbin.org/
#x = requests.post('http://127.0.0.1:8000/name', data = myobj)

#print(x.text)

#print(r.text)#[:200]

