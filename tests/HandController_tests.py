import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.HandController import advanceHand, advanceStreet
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.HandDetails import HandDetails

class HandControllerTests(unittest.TestCase):
    def setUp(self):
        self.gameDetails = GameDetails()
        self.handDetails = HandDetails()

    def testAdvanceHandUnraised(self):
        self.gameDetails.getPlayers()[0].setActive()
        self.gameDetails.getPlayers()[0].setNonDealer()
        self.gameDetails.getPlayers()[1].setInactive()
        self.gameDetails.getPlayers()[1].setDealer()
        advanceHand(self.handDetails, self.gameDetails)
        self.assertFalse(self.gameDetails.getPlayers()[0].getActiveStatus())
        self.assertTrue(self.gameDetails.getPlayers()[1].getActiveStatus())
        advanceHand(self.handDetails, self.gameDetails)
        self.assertEqual(self.handDetails.getStreet(), 1)

    def testAdvanceHandRaisedRaiser(self):
        self.gameDetails.getPlayers()[0].setActive()
        self.gameDetails.getPlayers()[0].bet(100, 1)
        self.handDetails.incrementRaised()
        advanceHand(self.handDetails, self.gameDetails)
        self.assertFalse(self.gameDetails.getPlayers()[0].getActiveStatus())
        self.assertTrue(self.gameDetails.getPlayers()[1].getActiveStatus())

    def testAdvanceHandRaisedCaller(self):
        self.gameDetails.getPlayers()[0].setActive()
        self.gameDetails.getPlayers()[0].bet(100, 0)
        self.handDetails.incrementRaised()
        advanceHand(self.handDetails, self.gameDetails)
        self.gameDetails.getPlayers()[1].bet(100, 0)
        advanceHand(self.handDetails, self.gameDetails)
        self.assertEqual(self.handDetails.getStreet(), 2) # TODO Fix regression - should this be one?
        self.assertTrue(self.gameDetails.getPlayers()[0].getActiveStatus())
        self.assertFalse(self.gameDetails.getPlayers()[1].getActiveStatus())

    def testAdvanceStreet(self):
        advanceStreet(self.handDetails) # First Draw - Flop
        self.assertEqual(self.handDetails.getStreet(), 1)
        advanceStreet(self.handDetails) # Second Draw - Turn
        self.assertEqual(self.handDetails.getStreet(), 2)
        advanceStreet(self.handDetails) # Third Draw - River
        self.assertEqual(self.handDetails.getStreet(), 3)
        self.assertEqual(advanceStreet(self.handDetails), 'Showdown')
