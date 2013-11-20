import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class TestPot(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()
        self.hand_details = HandDetails(self.game_details)

    def testGetPot(self):
        self.assertEqual(self.hand_details.getPot(), 0)

if __name__ == '__main__':
    unittest.main()

