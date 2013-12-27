import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.HandController import advanceHand
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
        self.assertEqual(advanceHand(self.handDetails, self.gameDetails), 'Next Street') # Change Later

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
        self.assertEqual(advanceHand(self.handDetails, self.gameDetails), 'Next Street') # Change Later
        self.assertTrue(self.gameDetails.getPlayers()[0].getActiveStatus())
        self.assertFalse(self.gameDetails.getPlayers()[1].getActiveStatus())
