import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.AmountToCallController import getAmountToCall
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class TestAmountToCallController(unittest.TestCase):
    def setUp(self):
        game_details = GameDetails()
        hand_details = HandDetails()

if __name__ == '__main__':
    unittest.main()
