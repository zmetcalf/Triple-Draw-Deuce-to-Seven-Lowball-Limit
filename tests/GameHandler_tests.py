import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.GameHandler import GameHandler

class TestInit(unittest.TestCase):

    def setUp(self):
        self.gameHandler = GameHandler(8, 1000, True)

    def test_opponents(self):
        self.assertEqual(self.gameHandler.opponents, 7)

class TestHeadsUp(unittest.TestCase):

    def setUp(self):
        self.gameHandler = GameHandler(2, 1000, True)
        self.gameHandler.postBlinds()

    def testDealer(self):
        self.assertTrue(self.gameHandler.players[0].getDealerStatus())

    def testPointerAfterBlinds(self):
        self.gameHandler.advancePointer()
        self.assertEqual(self.gameHandler.pointer, 1)

    def testActiveStatusAfterBlinds(self):
        self.assertTrue(self.gameHandler.players[0].getActiveStatus())

    def testChangeActionPlayer(self):
        self.gameHandler.changeActionPlayer()
        self.assertTrue(self.gameHandler.players[1].getActiveStatus())

    def test_raise_count(self):
        self.assertEqual(self.gameHandler.raiseCount, 0)

    def test_SB_bankroll(self):
        self.assertEqual(self.gameHandler.players[0].getBankroll(), 995)

    def test_SB_intialbet_CheckDraw(self):
        self.gameHandler.setAction("CheckDraw", 0)
        self.assertTrue(self.gameHandler.players[1].getActiveStatus())
        self.assertEqual(self.gameHandler.players[1].getBankroll(), 990)
        self.assertEqual(self.gameHandler.players[0].getBankroll(), 990)

    def test_BB_initialbet_raise(self):
        self.gameHandler.setAction("CheckDraw", 0)
        self.assertTrue(self.gameHandler.activeCheck)
        self.assertEqual(self.gameHandler.raiseCount, 1)
        self.assertTrue(self.gameHandler.players[1].getIsBB())
        self.gameHandler.setAction("BetRaise", 1)
        self.assertTrue(self.gameHandler.players[0].getActiveStatus())
        self.assertEqual(self.gameHandler.players[0].getBankroll(), 990)
        self.assertEqual(self.gameHandler.players[1].getBankroll(), 980)

    def test_raise_everything(self):
        self.gameHandler.setAction("BetRaise", 0)
        self.gameHandler.setAction("BetRaise", 1)
        self.gameHandler.setAction("BetRaise", 0)
        self.gameHandler.setAction("CheckDraw", 1)
        self.assertEqual(self.gameHandler.players[0].getBankroll()
                            and self.gameHandler.players[1].getBankroll(), 960)

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

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.gameHandler = GameHandler(2, 1000, True)

    def test_bet(self):
        self.gameHandler.postBlinds()
        self.gameHandler.bet(100)
        self.assertEqual(self.gameHandler.players[0].getBankroll(), 895)

if __name__ == '__main__':
    unittest.main()
