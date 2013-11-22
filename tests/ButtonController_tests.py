import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.ButtonController import getButtons
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class ButtonControllerTests(unittest.TestCase):
    def setUp(self):
        game_details = GameDetails()
        hand_details = HandDetails()

if __name__ == '__main__':
    unittest.main()
