import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.FoldController import fold
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.Player import Player

class FoldControllerTests(unittest.TestCase):
    def setUp(self):
        self.gameDetails = GameDetails()

    def testFold(self):
        return True
