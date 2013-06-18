import unittest
from GameHandler import GameHandler

class TestInit(unittest.TestCase):
    
    def setUp(self):
        self.gameHandler = GameHandler(8, 1000)

    def test_opponents(self):
        self.assertEqual(self.gameHandler.opponents, 8)
        
if __name__ == '__main__':
    unittest.main()
