import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.model.GameDetails import GameDetails

class GameDetailsTests(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()

    def testGetBetLevel(self):
        self.assertEqual(self.game_details.getBetLevel(), 10)

    def testGetNumberOfPlayers(self):
        self.assertEqual(self.game_details.getNumberOfPlayers(), 2)

if __name__ == '__main__':
    unittest.main()
