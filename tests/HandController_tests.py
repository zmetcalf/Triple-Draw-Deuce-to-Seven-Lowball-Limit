import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.HandController import advanceHand, advanceStreet
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class HandControllerTests(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()
        self.hand_details = HandDetails()

    def testAdvanceHandUnraised(self):
        self.game_details.getPlayers()[0].setActive()
        self.game_details.getPlayers()[0].setNonDealer()
        self.game_details.getPlayers()[1].setInactive()
        self.game_details.getPlayers()[1].setDealer()
        advanceHand(self.hand_details, self.game_details)
        self.assertFalse(self.game_details.getPlayers()[0].getActiveStatus())
        self.assertTrue(self.game_details.getPlayers()[1].getActiveStatus())
        advanceHand(self.hand_details, self.game_details)
        self.assertEqual(self.hand_details.getStreet(), 1)

    def testAdvanceHandRaisedRaiser(self):
        self.game_details.getPlayers()[0].setActive()
        self.game_details.getPlayers()[0].bet(100, 1)
        self.hand_details.incrementRaised()
        advanceHand(self.hand_details, self.game_details)
        self.assertFalse(self.game_details.getPlayers()[0].getActiveStatus())
        self.assertTrue(self.game_details.getPlayers()[1].getActiveStatus())

    def testAdvanceHandRaisedCaller(self):
        self.game_details.getPlayers()[0].setActive()
        self.game_details.getPlayers()[1].setInactive()
        self.game_details.getPlayers()[0].bet(100, 0)
        self.hand_details.incrementRaised()
        advanceHand(self.hand_details, self.game_details)
        self.assertEqual(self.game_details.getPlayers()[1].getBetThisStreet(), 0)
        self.assertEqual(self.hand_details.getRaised(), 1)
        self.assertEqual(self.hand_details.getStreet(), 0)
        self.game_details.getPlayers()[1].bet(100, 0)
        advanceHand(self.hand_details, self.game_details)
        self.assertEqual(self.hand_details.getStreet(), 1)
        self.assertTrue(self.game_details.getPlayers()[0].getActiveStatus())
        self.assertFalse(self.game_details.getPlayers()[1].getActiveStatus())

    def testAdvanceStreet(self):
        advanceStreet(self.hand_details, self.game_details) # First Draw - Flop
        self.assertEqual(self.hand_details.getStreet(), 1)
        advanceStreet(self.hand_details, self.game_details) # Second Draw - Turn
        self.assertEqual(self.hand_details.getStreet(), 2)
        advanceStreet(self.hand_details, self.game_details)# Third Draw - River
        self.assertEqual(self.hand_details.getStreet(), 3)
        self.assertTrue(advanceStreet(self.hand_details, self.game_details))
