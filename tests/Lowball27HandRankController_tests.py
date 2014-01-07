import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from tests.test_models.Card import Card

from triple_draw_poker.controller.Lowball27HandRankController import getWinner, \
      checkIfSuited
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class Lowball27HandRankControllerTests(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()
        self.hand_details = HandDetails()
        self.royal_flush = [
            Card('SPADE', 1),
            Card('SPADE', 13),
            Card('SPADE', 12),
            Card('SPADE', 11),
            Card('SPADE', 10)
        ]

        self.low_2_to_7 = [
            Card('HEART', 7),
            Card('CLUB', 2),
            Card('SPADE', 5),
            Card('SPADE', 3),
            Card('SPADE', 4)
        ]

        self.wheel = [
            Card('HEART', 13),
            Card('CLUB', 4),
            Card('SPADE', 5),
            Card('SPADE', 3),
            Card('SPADE', 2)
        ]

    def testGetWinner(self):
        return True

    def testCheckIfSuitedTrue(self):
        self.assertEqual(checkIfSuited(self.royal_flush), True)

    def testCheckIfSuitedFalse(self):
        self.assertEqual(checkIfSuited(self.low_2_to_7), False)

    def testCheckIfOrderedTrue(self):
        return True

    def testCheckIfOrderedFalse(self):
        return True

    def testCheckIfBroadwayTrue(self):
        return True

    def testCheckIfBroadwayFalse(self):
        return True

    def testCheckIfWheelTrue(self):
        self.assertEqual(checkIfSuited(self.wheel), True)

    def testCheckIfWheelFalse(self):
        return True
