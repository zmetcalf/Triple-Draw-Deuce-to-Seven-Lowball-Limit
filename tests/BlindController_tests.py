import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.BlindController import postBlinds
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class BlindControllerTests(unittest.TestCase):
    def setUp(self):
        self.gameDetails = GameDetails()

    def testPostBlinds(self):
        return True
