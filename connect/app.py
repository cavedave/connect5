import flask
from flask import request, jsonify, session
#from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

import json
import datetime
import numpy as np
#from flask_socketio import SocketIO, join_room, emit, send
#import connect.connect as connect

#from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session


#socketio = SocketIO(app)
#We need a board
#nine-column, six-row vertically suspended grid.

ROW_NUM = 6
COL_NUM = 9
#global state
#state = {        "plays": [],
  #      "myturn": 1,
  #      "Player":0,
  #      "board":[],
  #      "game_over": "no",
#        "current_player": 0}

def new_game():
	global board 
	global state
	board= create_board()
	print_board(board)
	state = {        "plays": [],
        "myturn": 1,
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

def on_board(move):
	return 0<= move <9


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
	print(token)
	while col< COL_NUM-4:
		while row<ROW_NUM:
			#print("col is "+str(col)+"row is "+str(row))
			print("piece "+str(board[col][row]))
			print("token "+str(token))
			if board[row][col]==token and board[row][col+1]==token and board[row][col+2]==token and board[row][col+3]==token and board[row][col+4]==token:
					print("five in a row")
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
				print("five in a row")
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
				print("five in a row")
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
				print("five in a row")
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

#@app.route('/api/v1/name', methods=['PUT'])
#def api_name():
#	jsondata = request.get_json()
#	print(jsondata)
#	return(True)
	#data = json.loads(jsondata)
	#return jsonify(data)

@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.route('/state/', methods=['GET'])
def show_state():
    #data = request.form['data']
    return state

@app.route('/name/', methods=['POST'])
def api_name():
	global state
	print("state is ")
	print(state)
	#need to fix this for third etc player
	name = request.form['name']
	if state['Player']==1:
		new_game()
		state = {
		'Player':0,
		'playersturn':1,
        "myturn": 1,
        "board":board.tolist(),
        "game_over": False,
        "text":"You are player 2. Game can start"
		}
	else:
		state = {
		'Player':1,
		'playersturn':0,
        "myturn": 0,
        "board":"",
        "game_over": False,
        "text":"You are player 1. waiting on player 2"
		}

	#print(name)
	return state
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
  #  if 'name' in request.args:
  #  	global Player
  #  	print("session is ")
  #  	print(Player)
    	#print(flask.session['_id'])
#use stdin. Session where two players join in. Can you have a session 
  #  	name= str(request.args['name'])
  #  	print(request.args['name'])
  #  	if Player ==1:
    		
   # 		print("Waiting on Player 2")
    #		Player+=1
    #		print(Player)   	
    #		state={#"board":board.tolist(),
    #		"Player":1,
	#		"myturn":0,
     #   	"game_over": False
      #  	}	
    	#	return state

    #	else:
    #		print(Player)
    #		print("New game called")
    #		new_game()
    #		state = {
     #   "plays": 1,
     #   "myturn": 1,
     #   "board":board,
     #   "game_over": False,
     #   "current_player": 0,
     #   "player":"You are player 2. Game can start"
#		}
    #		return state
    		
    #	Player+=1
    #	Player=Player%2

    #return "Got to end of Function"
        #id = int(request.args['id'])
    #else:
    #    return "Error: No id field provided. Please specify an id."	
    #return jsonify(name)


@app.route('/move', methods=['GET'])
def api_play():
	global board
	global state
	#board = create_board()
	#print_board(board)
	game_finished = 0
	turn = 0
	playersturn=state['playersturn']
	#print("player is ")
	#print(state['Player'])
	playersturn=playersturn+1
	playersturn=playersturn%2
	#print("player is ")
	#print(Player)
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
        "myturn": 0,
        "board":board.tolist(),
        "game_over": True,
		}
 				
 				return(state)
 			state = {
 		'playersturn':playersturn,
		'Player':Player,
        "plays": 1,
        "myturn": 0,
        "board":board.tolist(),
        "game_over": False,
		}	
 			return(state)
 		else:
 			return("Not valid move")
	print("got to enter column again probably wrongly")		
	print("please enter a column")
	#state = {
	#	'Player':Player,
    #    "plays": 1,
    #    "myturn": 0,
    #    "board":board.tolist(),
    #    "game_over": False,
	#	}

	#printing ok print(state)
	#return state


#@app.route('/api/v1/move', methods=['GET'])
#def api_move():
#	global board
#	if 'column' in request.args:
# 		move= int(str(request.args['column']))
# 		if(on_board(move) and (has_space(board, move))):
 			
# 			row=empty_square(board,move)
# 			drop_piece(board, move,row, 1)

# 			if game_over(board,1):
# 				print('Player One Won!!!')
# 				return("Game over state")
# 			state=	{"board":board.tolist(),
#				"myturn":False,
#		        "game_over": False
	   #     "plays": [],
       # "next_player": first_player,
       # "board":board.tolist()
#        }
# 			return(state)
# 		else:
# 			return("Not valid move")
#	print("got to enter column again probably wrongly")		
#	return "please enter a column"
			#turn = 1;

	#name = {1:board}
    #name[ 1 ]=board
    #return "name"
	
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    #if 'name' in request.args:


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)



if __name__ ==  '__main__':
    state = new_game()
    state = {    
        "Player":3,
        "board":[],
        "game_over": "no"}
    app.run()


