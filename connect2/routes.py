import connect.connect as connect
import flask
from flask import request, jsonify, session
#from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

import json
import datetime
import numpy as np
#http://127.0.0.1:5000/api/v1/state
#@app.route('/state/')
#def state():
#	return state

#...
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
		connect.new_game()
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
 		if(connect.on_board(move) and (connect.has_space(board, move))):
 			
 			row=connect.empty_square(board,move)
 			connect.drop_piece(board, move,row, playersturn+1)

 			if connect.game_over(board,1):
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
