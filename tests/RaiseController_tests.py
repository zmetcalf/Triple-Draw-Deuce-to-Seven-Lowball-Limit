import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.RaiseController import raiseBet
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class TestRaiseController(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()
        self.hand_details = HandDetails()
        self.hand_details.incrementRaised()
        self.hand_details.incrementRaised()
        self.game_details.players[0].setActive()

    def testRaisePot(self):
        raiseBet(self.game_details, self.hand_details)
        self.assertEqual(self.hand_details.getRaised(), 3)

if __name__ == '__main__':
    unittest.main()


