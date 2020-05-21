import flask
from flask import request, jsonify, session
#from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

import json
import datetime
import numpy as np
#from flask_socketio import SocketIO, join_room, emit, send

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



