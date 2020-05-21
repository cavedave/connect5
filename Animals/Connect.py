
import numpy as np

#We need a board
#nine-column, six-row vertically suspended grid.

ROW_NUM = 6
COL_NUM = 9

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

#drop a piece down
#when column selected drop piece into last empty row
#def pick_column(col_picked):


board =  create_board()
game_finished = 0
turn = 0

while game_finished ==0:
	if turn == 0:
		move = int(input("Player One pick a column (0-8)"))
		if(on_board(move) and (has_space(board, move))):
			print("valid move")
			row=empty_square(board,move)
			drop_piece(board, move,row, 1)
			if game_over(board,1):
				print('Player One Won!!!')
		else:
			print("Not valid move")
			turn = 1;
		has_space(board, move)
	if turn == 1:
		move = int(input("Player Two pick a column (0-8)"))
		if(on_board(move) and (has_space(board, move))):
			print("valid move")
			row=empty_square(board,move)
			drop_piece(board, move,row, 2)#change to x o like description
			if game_over(board,2):
				print('Player Two Won!!!')
		else:
			print("Not valid move")
			turn = 0;
	print_board(board)
	turn +=1
	turn=turn%2

if __name__ == '__main__':
    print(MENU)		
		
