import unittest

#from connect5 import connect5
#from Connect import Mammals
from Connect import *

 ############################
    #### setup and teardown ####
    ############################
#class BasicTests(unittest.TestCase):

import unittest
ROW_NUM = 6
COL_NUM = 9

class TestSum(unittest.TestCase):

    def test_on_board(self):
    	self.assertTrue(on_board(6), "6 is on the board")

    def test_drop_piece(self):
    	board = create_board()
    	drop_piece(board,1,1,1)
    	self.assertEqual(board[1][1],1, "piece added to board at 1 1")
    	drop_piece(board,1,1,2)
    	self.assertEqual(board[1][1],2, "piece added to board at 1 1")
   	

    def test_empty_square(self): #add more here later
    	board = create_board()
    	self.assertEqual(empty_square(board, 1),0, "column one of new board is empty")

    def test_game_over(self): #add more here later
    	#test horizontal
    	board = create_board()
    	self.assertFalse(game_over(board,1), "game should not be over horizontal")
    	drop_piece(board,1,1,1)
    	drop_piece(board,2,1,1)
    	drop_piece(board,3,1,1)
    	drop_piece(board,4,1,1)
    	drop_piece(board,5,1,1)
    	self.assertTrue(game_over(board,1), "game should be over horizontal")
    	#test vertical
    	board = create_board()
    	self.assertFalse(game_over(board,1), "game should not be over vertical")
    	drop_piece(board,1,1,1)
    	drop_piece(board,1,2,1)
    	drop_piece(board,1,3,1)
    	drop_piece(board,1,4,1)
    	drop_piece(board,1,5,1)
    	#print(board)
    	self.assertTrue(game_over(board,1), "game should be over vertical")
    	#test vertical that is wrong
    	board = create_board()
    	self.assertFalse(game_over(board,1), "game should not be over vertical")
    	drop_piece(board,1,2,1)
    	drop_piece(board,1,2,1)
    	drop_piece(board,1,2,1)
    	drop_piece(board,1,2,1)
    	drop_piece(board,1,2,1)
    	self.assertFalse(game_over(board,1), "game still should not be over vertical fake")
    	#test horizontal other token
    	board = create_board()
    	self.assertFalse(game_over(board,2), "game should not be over horizontal2 token ")
    	drop_piece(board,1,1,2)
    	drop_piece(board,2,1,2)
    	drop_piece(board,3,1,2)
    	drop_piece(board,4,1,2)
    	drop_piece(board,5,1,2)
    	self.assertTrue(game_over(board,2), "game should be over horizontal 2 token")
    	

    def test_game_diag(self): #add more here later
    	#test diagonal up
    	board = create_board()
    	self.assertFalse(game_over(board,1), "game should not be over diag up")
    	drop_piece(board,0,0,1)
    	drop_piece(board,1,1,1)
    	drop_piece(board,2,2,1)
    	drop_piece(board,3,3,1)
    	drop_piece(board,4,4,1)
    	self.assertTrue(game_over(board,1), "game should be over diag up")
    	#test diagonal down
    	board = create_board()
    	self.assertFalse(game_over(board,1), "game should not be over diag down")
    	drop_piece(board,0,4,1)
    	drop_piece(board,1,3,1)
    	drop_piece(board,2,2,1)
    	drop_piece(board,3,1,1)
    	drop_piece(board,4,0,1)
    	self.assertTrue(game_over(board,1), "game should be over diag down")

    def test_game_start(self): #add more here later
    	#test game starting
    	#board = create_board()

    	self.assertTrue(new_game(), "new game")
    	state= return_state()
    	#print(state)
    	#state should look like
 #{'plays': [], 'myturn': 1, 'Player': 3, 'board': [], 'game_over': 'no', 'current_player': 0}
    	self.assertEqual(state['Player'],3, "creating game creates a player")




    def test_has_space(self): #add more here later
    	board = create_board()
    	self.assertTrue(has_space(board, 1), "empty baord has space at 1")

    	

    def test_create_board(self):
    	self.assertEqual(create_board()[0][0],0, "empty square created board")
    	self.assertEqual(create_board()[5][5],0, "empty square created board 5 5")
    	self.assertEqual(create_board()[ROW_NUM-1][COL_NUM-1],0, "empty square created board")
    	self.assertEqual(create_board()[0][COL_NUM-1],0, "elast column mpty square created board")
    	self.assertEqual(create_board()[ROW_NUM-1][0],0, "last square empty square created board")


#flas test that should be in their own filr
    # executed prior to each test
    def setUp(self):
        #app.config['TESTING'] = True
        #app.config['WTF_CSRF_ENABLED'] = False
        #app.config['DEBUG'] = False
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        #    os.path.join(app.config['BASEDIR'], TEST_DB)
        new_game()
        self.app = app.test_client()
        #db.drop_all()
        #db.create_all()
 
        # Disable sending emails during unit testing
        #mail.init_app(app)
        #self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
#    def test_valid_user_registration(self):
#    	response = self.register('patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
#    	self.assertEqual(response.status_code, 200)
#    	self.assertIn(b'Thanks for registering!', response.data)

    def test_add_name(self):
       	self.assertTrue(new_game(), "new game")
       	state= return_state()
       	response = self.name()
       	self.assertEqual(response.status_code, 200)
       	self.assertIn(b'{\n  "Player": 1, \n  "board": "", \n  "game_over": false, \n  "playersturn": 0, \n  "text": "You are player 1. waiting on player 2"\n}\n', response.data)


# @app.route('/move', methods=['GET'])
#r = requests.get('http://127.0.0.1:5000/move?column='+str(move))
    def test_move(self):
       	self.assertTrue(new_game(), "new game")
       	state= return_state()
       	response = self.move()
       	self.assertEqual(response.status_code, 200)
       	self.assertIn(b'{\n  "Player": 1, \n  "board": [\n    [\n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      1.0, \n      0.0, \n      0.0, \n      0.0\n    ], \n    [\n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0\n    ], \n    [\n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0\n    ], \n    [\n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0\n    ], \n    [\n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0\n    ], \n    [\n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0, \n      0.0\n    ]\n  ], \n  "game_over": false, \n  "playersturn": 0, \n  "plays": 1\n}\n', response.data)

    def test_valid_state(self):
    	response = self.state()
    	self.assertEqual(response.status_code, 200)
    	self.assertIn(b'{\n  "Player": 3, \n  "board": [], \n  "current_player": 0, \n  "game_over": "no", \n  "playersturn": 3\n}\n', response.data)

#    def test_add_name(self):
#    	response = self.name()
#    	self.assertEqual(response.status_code, 200)
#    	self.assertIn(b'{\n  "Player": 3, \n  "board": [], \n  "current_player": 0, \n  "game_over": "no", \n  "myturn": 1, \n  "plays": []\n}\n', response.data)



    def state(self):
        return self.app.get(
            '/state',
            follow_redirects=True
        )

    def move(self):
        return self.app.get(
            '/move?column=5',
            follow_redirects=True
        )

    def name(self):
        return self.app.post(
            '/name/',
            data=dict(name='David'),
            follow_redirects=False
        )


#Do some sort if integration test of everything together

    def test_entire_Game(self): #add more here later
    	#this isnt here yet
    	board = create_board()
	 	drop_piece(board,0,0,1)
    	drop_piece(board,1,1,1)
    	drop_piece(board,2,2,1)
    	drop_piece(board,3,3,1)
    	drop_piece(board,4,4,1)
    	self.assertTrue(game_over(board,1), "This should be a full game")



###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()


#def test_sum():
#	assert sum([1, 2, 3]) == 6, "Should be 6"

#def test_on_board(self):
#	assert on_board(6)== 6, "6 is on the board"

#if __name__ == "__main__":
#    test_sum()
#    test_on_board()
#    print("Everything passed")

#	pass


#if __name__ == "__main__":
#	test_on_board()
#   	unittest.main()
		#self.assertEqual(on_board(6), 6, "6 is on the board")

    # executed prior to each test
    #def setUp(self):
        #app.config['TESTING'] = True
        #app.config['WTF_CSRF_ENABLED'] = False
        #app.config['DEBUG'] = False
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        #os.path.join(app.config['BASEDIR'], TEST_DB)
    ##    self.app = app.test_client()
        #db.drop_all()
        #db.create_all()
 
        # Disable sending emails during unit testing
        #mail.init_app(app)
        #self.assertEqual(app.debug, False)

    # executed after each test
    #def tearDown(self):
    #    pass
 	

 
###############
#### tests ####
###############
 
    #def test_main_page(self):
    #    response = self.app.get('/', follow_redirects=True)
     #   self.assertEqual(response.status_code, 200)
 
 


#class TestSum(unittest.TestCase):
#	myMammal = Mammals()
#	myMammal.printMembers()
    #def test_sum(self):
    #    self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    #def test_sum_tuple(self):
    #    self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")


    


# Import classes from your brand new package


 
# Create an object of Mammals class & call a method of it

 
# Create an object of Birds class & call a method of it

