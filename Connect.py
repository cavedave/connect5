import flask
from flask import request, jsonify, session

import json
import datetime
import numpy as np


ROW_NUM = 6
COL_NUM = 9


def new_game():
	global board 
	global state
	board= create_board()
	#print_board(board)
	state = {     
        "playersturn":3,
        "Player":3,
        "board":[],
        "game_over": "no",
        "current_player": 0}
	return True

def create_board():
	board = np.zeros((ROW_NUM,COL_NUM))
	return board

#put a piece in a location
def drop_piece(board, col, row, piece):
	board[row][col] = piece

#flip as 0 is top row of array and we want it to be bottom
def print_board(board):
	print(np.flip(board,0))

#return state. It probably shouldnt be global anyway and this is the path to
#localise it
def return_state():
	return state


def on_board(move):
	return 0<= move <9
on_board(6)

def has_space(board, move):
	return board[ROW_NUM-1][move]==0

def empty_square(board,move):
	#go down that column until you dont get zero
	empty =ROW_NUM-1;
	while board[empty][move]==0 and empty >=0:
		empty-=1
	return(empty+1)

def game_over(board,token):
	#check horizontal
	col =0;
	row =0;
	#print(token)
	while col< COL_NUM-4:
		while row<ROW_NUM:
			#print("col is "+str(col)+"row is "+str(row))
			#print("piece "+str(board[col][row]))
			#print("token "+str(token))
			if board[row][col]==token and board[row][col+1]==token and board[row][col+2]==token and board[row][col+3]==token and board[row][col+4]==token:
					#print("five in a row")
					return True
			row+=1
		col +=1
		row=0;	

	#check vertical
	col =0;
	row =0;
	while col< COL_NUM:
		while row<ROW_NUM-4:
			#print("col is "+str(col)+"row is "+str(row))
			#print("piece "+str(board[col][row]))
			#print("token "+str(token))
			if board[row][col]==token and board[row+1][col]==token and board[row+2][col]==token and board[row+3][col]==token and board[row+4][col]==token:
				#print("five in a row")
				return True
			row+=1
		col +=1
		row=0
	#check diagonal up
	col =0;
	row =0;
	while col< COL_NUM-4:
		while row<ROW_NUM-4:
			#print("col is "+str(col)+"row is "+str(row))
			#print("piece "+str(board[col][row]))
			#print("token "+str(token))
			if int(board[row][col])==token and board[row+1][col+1]==token and board[row+2][col+2]==token and board[row+3][col+3]==token and board[row+4][col+4]==token:
				#print("five in a row")
				return True
			row+=1
		col +=1
		row=0	
	#check diagonal down	
	col =0;
	row =4;
	while col< COL_NUM-4:
		while row<ROW_NUM:
			#print("col is "+str(col)+"row is "+str(row))
			#print("piece "+str(board[col][row]))
			#print("token "+str(token))
			if int(board[row][col])==token and board[row-1][col+1]==token and board[row-2][col+2]==token and board[row-3][col+3]==token and board[row-4][col+4]==token:
				#print("five in a row")
				return True
			row+=1
		col +=1
		row=0	
	return False


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "super secret key"#change in reality
app.permanent_session_lifetime = datetime.timedelta(days=365)
Player = 1 #what player is it
# Create some test data for our catalog in the form of a list of dictionaries.


@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return "Total visits: {}".format(session.get('visits'))


@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.route('/state/', methods=['GET'])
def show_state():
    return state

@app.route('/name/', methods=['POST'])
def api_name():
	global state
	#need to fix this for third etc player
	name = request.form['name']
	if state['Player']==1:
		new_game()
		state = {
		'Player':0,
		'playersturn':1,
        "board":board.tolist(),
        "game_over": False,
        "text":"You are player 2. Game can start"
		}
	else:
		state = {
		'Player':1,
		'playersturn':0,
        "board":"",
        "game_over": False,
        "text":"You are player 1. waiting on player 2"
		}

	#print(name)

	return state



@app.route('/move', methods=['GET'])
def api_play():
	global board
	global state

	playersturn=state['playersturn']

	if 'column' in request.args:
 		move= int(str(request.args['column']))
 		if(on_board(move) and (has_space(board, move))):
 			
 			row=empty_square(board,move)
 			drop_piece(board, move,row, playersturn+1)

 			if game_over(board,1):
 				state = {
		#'Player':Player,
		'playersturn':playersturn,
        "plays": 1,
        #"myturn": 0,
        "board":board.tolist(),
        "game_over": True,
		}
 				
 				return(state)
 			else:#game not over
 				#print("in game not over bit")
 				#playersturn=state['playersturn']
 				playersturn=playersturn+1
 				playersturn=playersturn%2
 				state = {
 		'playersturn':playersturn,
		'Player':Player,
        "plays": 1,
        #"myturn": 0,
        "board":board.tolist(),
        "game_over": False,
		}	
 			return(state)
 		else:
 			return("Not valid move")
	print("got to enter column again probably wrongly")		
	print("please enter a column")





@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


if __name__ ==  '__main__':
    state = new_game()
    state = {  
	    "playersturn":3,  
        "Player":3,
        "board":[],
        "game_over": "no"}
    app.run()


