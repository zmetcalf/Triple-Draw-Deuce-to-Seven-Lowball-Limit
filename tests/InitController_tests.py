import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.InitController import initHand
from triple_draw_poker.model.GameDetails import GameDetails

class InitControllerTests(unittest.TestCase):
    def setUp(self):
        self.gameDetails = GameDetails()

    def testHeadsUpInit(self):
        return False

if __name__ == '__main__':
    unittest.main()
