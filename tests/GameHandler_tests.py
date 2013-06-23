import unittest
from GameHandler import GameHandler

class TestInit(unittest.TestCase):
    
    def setUp(self):
        self.gameHandler = GameHandler(8, 1000)

    def test_opponents(self):
        self.assertEqual(self.gameHandler.opponents, 8)
        
class TestHeadsUp(unittest.TestCase):
    
    def setUp(self):
        self.gameHandler = GameHandler(1, 1000)
        
        
if __name__ == '__main__':
    unittest.main()
