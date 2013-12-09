import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.GameController import GameController

class GameControllerTests(unittest.TestCase):

    def setUp(self):
        self.game_controller = GameController()
        self.game_controller.setupHand()

    def testHandDetails(self):
        self.assertEqual(self.game_controller.hand_details.getPot(),
                          self.game_controller.hand_details.pot)

if __name__ == '__main__':
    unittest.main()
