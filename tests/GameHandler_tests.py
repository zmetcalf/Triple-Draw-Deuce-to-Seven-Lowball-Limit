import unittest
from GameHandler import GameHandler

class TestInit(unittest.TestCase):
    
    def setUp(self):
        self.gameHandler = GameHandler(8, 1000, True)

    def test_opponents(self):
        self.assertEqual(self.gameHandler.opponents, 7)
        
class TestHeadsUp(unittest.TestCase):
    
    def setUp(self):
        self.gameHandler = GameHandler(2, 1000, True)
        
    def testDealer(self):
        self.assertTrue(self.gameHandler.players[0].getDealerStatus())
        
    def testPointerAfterBlinds(self):
        self.gameHandler.postBlinds()
        self.gameHandler.advancePointer()
        self.assertEqual(self.gameHandler.pointer, 1)
        
    def testActiveStatusAfterBlinds(self):
        self.gameHandler.postBlinds()
        self.assertTrue(self.gameHandler.players[0].getActiveStatus())
        
    def testChangeActionPlayer(self):
        self.gameHandler.postBlinds()
        self.gameHandler.changeActionPlayer()
        self.assertTrue(self.gameHandler.players[1].getActiveStatus())
        
class TestRingGame(unittest.TestCase):
    
    def setUp(self):
        self.gameHandler = GameHandler(8, 1000, True)
        
    def testDealer(self):
        self.assertTrue(self.gameHandler.players[0].getDealerStatus())
        
    def testPointer(self):
        self.assertEqual(self.gameHandler.pointer, 1)
    
    def testPointerAfterBlinds(self):
        self.gameHandler.postBlinds()
        self.gameHandler.advancePointer()
        self.assertEqual(self.gameHandler.pointer, 4)
    
    def testActiveStatusAfterBlinds(self):
        self.gameHandler.postBlinds()
        self.assertTrue(self.gameHandler.players[3].getActiveStatus())
        
    def testChangeActionPlayer(self):
        self.gameHandler.postBlinds()
        self.gameHandler.changeActionPlayer()
        self.assertTrue(self.gameHandler.players[4].getActiveStatus())
        
if __name__ == '__main__':
    unittest.main()
