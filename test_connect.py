import unittest

#from connect5 import connect5
#from Connect import Mammals
from Connect import app

 ############################
    #### setup and teardown ####
    ############################
#class BasicTests(unittest.TestCase):

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

    def test_on_board(self):
    	self.assertEqual(on_board(6)== 6, "6 is on the board")

    def test_create_board(self):
    	self.assertEqual(create_board()== 0, "empty square created board")


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

