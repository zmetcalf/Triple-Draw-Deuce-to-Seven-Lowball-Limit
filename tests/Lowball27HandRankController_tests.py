import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from tests.test_models.Card import Card

from triple_draw_poker.controller.Lowball27HandRankController import getWinner, \
      checkIfSuited, checkIfWheel, checkIfBroadway, checkIfStraight, \
      checkIfFourOfKind, checkIfThreeOfKind, checkIfFullHouse, checkIfPaired, \
      checkIfTwoPaired
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

        self.four_of_kind = [
            Card('HEART', 12),
            Card('SPADE', 12),
            Card('CLUB', 12),
            Card('DIAMOND', 12),
            Card('SPADE', 10)
        ]

        self.full_house = [
            Card('HEART', 12),
            Card('SPADE', 10),
            Card('CLUB', 12),
            Card('DIAMOND', 12),
            Card('CLUB', 10)
        ]

        self.three_of_kind = [
            Card('HEART', 12),
            Card('SPADE', 13),
            Card('CLUB', 12),
            Card('DIAMOND', 12),
            Card('SPADE', 10)
        ]

        self.straight = [
            Card('HEART', 7),
            Card('CLUB', 3),
            Card('SPADE', 5),
            Card('DIAMOND', 6),
            Card('SPADE', 4)
        ]

        self.two_pair = [
            Card('HEART', 12),
            Card('SPADE', 10),
            Card('CLUB', 12),
            Card('DIAMOND', 3),
            Card('CLUB', 10)
        ]

        self.one_pair = [
            Card('HEART', 12),
            Card('SPADE', 1),
            Card('CLUB', 12),
            Card('DIAMOND', 3),
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
            Card('HEART', 1),
            Card('CLUB', 4),
            Card('SPADE', 5),
            Card('SPADE', 3),
            Card('SPADE', 2)
        ]

    def testGetWinner(self):
        return True

    def testCheckIfFourOfKindTrue(self):
        self.assertEqual(checkIfFourOfKind(self.four_of_kind), 12)

    def testCheckIfFourOfKindFalse(self):
        self.assertEqual(checkIfFourOfKind(self.royal_flush), False)

    def testCheckIfFullHouseTrue(self):
        self.assertEqual(checkIfFullHouse(self.full_house), [12, 10])

    def testCheckIfFullHouseFalse(self):
        self.assertEqual(checkIfFullHouse(self.three_of_kind), False)

    def testCheckIfThreeOfKindTrue(self):
        self.assertEqual(checkIfThreeOfKind(self.three_of_kind), 12)

    def testCheckIfThreeOfKindFalse(self):
        self.assertEqual(checkIfThreeOfKind(self.royal_flush), False)

    def testCheckIfTwoPairedTrue(self):
        self.assertEqual(checkIfTwoPaired(self.two_pair), [10, 12])

    def testCheckIfTwoPairedFalse(self):
        self.assertEqual(checkIfTwoPaired(self.one_pair), False)

    def testCheckIfPairedTrue(self):
        self.assertEqual(checkIfPaired(self.one_pair), 12)

    def testCheckIfPairedFalse(self):
        self.assertEqual(checkIfPaired(self.three_of_kind), False)

    def testCheckIfSuitedTrue(self):
        self.assertEqual(checkIfSuited(self.royal_flush), True)

    def testCheckIfSuitedFalse(self):
        self.assertEqual(checkIfSuited(self.low_2_to_7), False)

    def testCheckIfStraightTrue(self):
        self.assertEqual(checkIfStraight(self.straight), 7)

    def testCheckIfStraightFalse(self):
        self.assertEqual(checkIfStraight(self.low_2_to_7), False)

    def testCheckIfBroadwayTrue(self):
        self.assertEqual(checkIfBroadway(self.royal_flush), 14)
        self.assertEqual(checkIfStraight(self.royal_flush), 14)

    def testCheckIfBroadwayFalse(self):
        self.assertEqual(checkIfBroadway(self.wheel), False)

    def testCheckIfWheelTrue(self):
        self.assertEqual(checkIfWheel(self.wheel), 5)
        self.assertEqual(checkIfStraight(self.wheel), 5)

    def testCheckIfWheelFalse(self):
        self.assertEqual(checkIfWheel(self.royal_flush), False)
