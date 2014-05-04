import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.AmountToCallController import getAmountToCall
from triple_draw_poker.model.GameDetails import GameDetails

class AmountToCallControllerTests(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()
        self.game_details.getHandDetails().incrementRaised()
        self.game_details.getHandDetails().incrementRaised()
        self.game_details.players[0].setActive()

    def testRaisedPot(self):
        self.assertEqual(getAmountToCall(self.game_details), 2)

if __name__ == '__main__':
    unittest.main()
