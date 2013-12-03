import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.model.GameDetails import GameDetails

class GameDetailsTests(unittest.TestCase):
    def setUp(self):
        self.gameDetails = GameDetails()

    def testGetBetLevel(self):
        self.assertEqual(self.gameDetails.getBetLevel(), 10)

    def testGetNumberOfPlayers(self):
        self.assertEqual(self.gameDetails.getNumberOfPlayers(), 2)

    def testAdvanceDealerSimple(self):
        self.gameDetails.players[0].setDealer()
        self.gameDetails.players[1].setNonDealer()
        self.gameDetails.advanceDealer()
        self.assertFalse(self.gameDetails.players[0].getDealerStatus())
        self.assertTrue(self.gameDetails.players[1].getDealerStatus())

    def testAdvanceDealerRoundTheBend(self):
        self.gameDetails.players[0].setNonDealer()
        self.gameDetails.players[1].setDealer()
        self.gameDetails.advanceDealer()
        self.assertFalse(self.gameDetails.players[1].getDealerStatus())
        self.assertTrue(self.gameDetails.players[0].getDealerStatus())

if __name__ == '__main__':
    unittest.main()
