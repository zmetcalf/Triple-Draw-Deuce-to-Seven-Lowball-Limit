import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from tests.test_models.Card import Card

from triple_draw_poker.controller.Lowball27HandRankController import getLowballWinner, \
      checkIfFlush, checkIfWheel, checkIfBroadway, checkIfStraight, \
      checkIfFourOfKind, checkIfThreeOfKind, checkIfFullHouse, checkIfPaired, \
      checkIfTwoPaired, getAceHighList, checkIfRoyalFlush, checkIfStraightFlush, \
      getBestHand
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

        self.straight_flush = [
            Card('SPADE', 7),
            Card('SPADE', 9),
            Card('SPADE', 8),
            Card('SPADE', 5),
            Card('SPADE', 6)
        ]

        self.straight_flush_low = [
            Card('SPADE', 1),
            Card('SPADE', 2),
            Card('SPADE', 4),
            Card('SPADE', 3),
            Card('SPADE', 5)
        ]

        self.four_of_kind = [
            Card('HEART', 12),
            Card('SPADE', 12),
            Card('CLUB', 12),
            Card('DIAMOND', 12),
            Card('SPADE', 10)
        ]

        self.four_of_kind_low = [
            Card('HEART', 11),
            Card('SPADE', 11),
            Card('CLUB', 11),
            Card('DIAMOND', 11),
            Card('SPADE', 10)
        ]

        self.full_house = [
            Card('HEART', 12),
            Card('SPADE', 10),
            Card('CLUB', 12),
            Card('DIAMOND', 12),
            Card('CLUB', 10)
        ]

        self.full_house_low = [
            Card('HEART', 10),
            Card('SPADE', 10),
            Card('CLUB', 12),
            Card('DIAMOND', 12),
            Card('CLUB', 10)
        ]

        self.flush = [
            Card('SPADE', 7),
            Card('SPADE', 10),
            Card('SPADE', 1),
            Card('SPADE', 5),
            Card('SPADE', 6)
        ]

        self.flush_low = [
            Card('CLUB', 7),
            Card('CLUB', 9),
            Card('CLUB', 1),
            Card('CLUB', 5),
            Card('CLUB', 6)
        ]

        self.straight = [
            Card('HEART', 7),
            Card('CLUB', 3),
            Card('SPADE', 5),
            Card('DIAMOND', 6),
            Card('SPADE', 4)
        ]

        self.three_of_kind = [
            Card('HEART', 12),
            Card('SPADE', 13),
            Card('CLUB', 12),
            Card('DIAMOND', 12),
            Card('SPADE', 10)
        ]

        self.three_of_kind_low = [
            Card('HEART', 10),
            Card('SPADE', 13),
            Card('CLUB', 10),
            Card('DIAMOND', 12),
            Card('SPADE', 10)
        ]

        self.two_pair = [
            Card('HEART', 12),
            Card('SPADE', 10),
            Card('CLUB', 12),
            Card('DIAMOND', 3),
            Card('CLUB', 10)
        ]

        self.two_pair_low = [
            Card('HEART', 2),
            Card('SPADE', 10),
            Card('CLUB', 2),
            Card('DIAMOND', 3),
            Card('CLUB', 10)
        ]

        self.two_pair_low_kick = [
            Card('HEART', 12),
            Card('SPADE', 10),
            Card('CLUB', 12),
            Card('DIAMOND', 2),
            Card('CLUB', 10)
        ]

        self.one_pair = [
            Card('HEART', 12),
            Card('SPADE', 1),
            Card('CLUB', 12),
            Card('DIAMOND', 3),
            Card('SPADE', 10)
        ]

        self.one_pair_low = [
            Card('HEART', 12),
            Card('SPADE', 1),
            Card('CLUB', 10),
            Card('DIAMOND', 3),
            Card('SPADE', 10)
        ]

        self.one_pair_low_kick = [
            Card('HEART', 12),
            Card('SPADE', 1),
            Card('CLUB', 12),
            Card('DIAMOND', 2),
            Card('SPADE', 10)
        ]

        self.high_card = [
            Card('HEART', 1),
            Card('CLUB', 2),
            Card('SPADE', 10),
            Card('SPADE', 3),
            Card('SPADE', 4)
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

    def testGetLowballWinner(self):
        return True

    def testGetBestHand(self):
        self.assertEqual(getBestHand(self.one_pair, self.low_2_to_7), 'one')
        self.assertEqual(getBestHand(self.one_pair, self.full_house), 'two')
        self.assertEqual(getBestHand(self.full_house_low, self.full_house),
                          'two')
        self.assertEqual(getBestHand(self.straight_flush,
                                      self.straight_flush_low), 'one')
        self.assertEqual(getBestHand(self.flush, self.flush_low), 'one')
        self.assertEqual(getBestHand(self.flush_low, self.flush), 'two')
        self.assertEqual(getBestHand(self.straight, self.wheel), 'one')
        self.assertEqual(getBestHand(self.high_card, self.low_2_to_7), 'one')
        self.assertEqual(getBestHand(self.three_of_kind,
                                      self.three_of_kind_low), 'one')
        self.assertEqual(getBestHand(self.two_pair_low_kick,
                                      self.two_pair), 'two')
        self.assertEqual(getBestHand(self.one_pair, self.one_pair_low), 'one')
        self.assertEqual(getBestHand(self.low_2_to_7, self.low_2_to_7), 'tie')

    def testGetAceHighList(self):
        ace_high_list = getAceHighList(self.royal_flush)
        self.assertEqual(ace_high_list[0].getRank(), 14)

    def testCheckIfRoyalFlushTrue(self):
        self.assertEqual(checkIfRoyalFlush(self.royal_flush), True)

    def testCheckIfRoyalFlushFalse(self):
        self.assertEqual(checkIfRoyalFlush(self.straight_flush), False)

    def testCheckIfStraightFlushTrue(self):
        self.assertEqual(checkIfStraightFlush(self.straight_flush), 9)

    def testCheckIfStraightFlushFalse(self):
        self.assertEqual(checkIfStraightFlush(self.straight), False)

    def testCheckIfFourOfKindTrue(self):
        self.assertEqual(checkIfFourOfKind(self.four_of_kind), 12)

    def testCheckIfFourOfKindFalse(self):
        self.assertEqual(checkIfFourOfKind(self.royal_flush), False)

    def testCheckIfFullHouseTrue(self):
        self.assertEqual(checkIfFullHouse(self.full_house), [12, 10])

    def testCheckIfFullHouseFalse(self):
        self.assertEqual(checkIfFullHouse(self.three_of_kind), False)

    def testCheckIfFlushTrue(self):
        self.assertEqual(checkIfFlush(self.royal_flush), [14, 13, 12, 11, 10])

    def testCheckIfFlushFalse(self):
        self.assertEqual(checkIfFlush(self.low_2_to_7), False)

    def testCheckIfStraightTrue(self):
        self.assertEqual(checkIfStraight(self.straight), 7)

    def testCheckIfStraightFalse(self):
        self.assertEqual(checkIfStraight(self.low_2_to_7), False)

    def testCheckIfThreeOfKindTrue(self):
        self.assertEqual(checkIfThreeOfKind(self.three_of_kind), 12)

    def testCheckIfThreeOfKindFalse(self):
        self.assertEqual(checkIfThreeOfKind(self.royal_flush), False)

    def testCheckIfTwoPairedTrue(self):
        self.assertEqual(checkIfTwoPaired(self.two_pair), [12, 10, 3])

    def testCheckIfTwoPairedFalse(self):
        self.assertEqual(checkIfTwoPaired(self.one_pair), False)

    def testCheckIfPairedTrue(self):
        self.assertEqual(checkIfPaired(self.one_pair), [12, 14, 10, 3])

    def testCheckIfPairedFalse(self):
        self.assertEqual(checkIfPaired(self.three_of_kind), False)

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
