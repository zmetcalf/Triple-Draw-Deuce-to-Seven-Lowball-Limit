import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.ButtonController import getButtons
from triple_draw_poker.controller.RaiseController import raiseBet
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class ButtonControllerTests(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()
        self.hand_details = HandDetails()
        self.game_details.setActivePlayer(0)

    def testUnraised(self):
        test_list = [False, True, False, True, False]
        self.assertEqual(getButtons(self.game_details, self.hand_details),
                                    test_list)

    def testRaised(self):
        test_list = [True, False, True, False, True]
        raiseBet(self.game_details, self.hand_details)
        self.assertEqual(getButtons(self.game_details, self.hand_details),
                                    test_list)

    def testCapped(self):
        test_list = [True, False, True, False, False]
        for _ in range(4):
            raiseBet(self.game_details, self.hand_details)
        self.assertEqual(getButtons(self.game_details, self.hand_details),
                                    test_list)

if __name__ == '__main__':
    unittest.main()
