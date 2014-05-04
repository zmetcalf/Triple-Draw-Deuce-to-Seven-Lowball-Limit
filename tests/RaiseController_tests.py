import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.RaiseController import raiseBet
from triple_draw_poker.model.GameDetails import GameDetails

class RaiseControllerTests(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()
        self.game_details.getHandDetails().incrementRaised()
        self.game_details.getHandDetails().incrementRaised()
        self.game_details.players[0].setActive()

    def testRaisePot(self):
        raiseBet(self.game_details)
        self.assertEqual(self.game_details.getHandDetails().getRaised(), 3)

if __name__ == '__main__':
    unittest.main()


