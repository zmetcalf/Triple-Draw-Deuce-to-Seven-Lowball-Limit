import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.ButtonController import getButtons
from triple_draw_poker.controller.RaiseController import raiseBet
from triple_draw_poker.model.GameDetails import GameDetails

class ButtonControllerTests(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()
        self.game_details.setActivePlayer(0)

    def testUnraised(self):
        test_list = [False, True, False, True, False]
        self.assertEqual(getButtons(self.game_details), test_list)

    def testRaised(self):
        test_list = [True, False, True, False, True]
        raiseBet(self.game_details)
        self.assertEqual(getButtons(self.game_details), test_list)

    def testCapped(self):
        test_list = [True, False, True, False, False]
        self.game_details.getHandDetails().raised = 4
        self.assertEqual(getButtons(self.game_details), test_list)

if __name__ == '__main__':
    unittest.main()
