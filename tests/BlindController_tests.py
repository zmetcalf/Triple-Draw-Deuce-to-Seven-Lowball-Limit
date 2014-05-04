import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.BlindController import postBlinds
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.Player import Player

class BlindControllerTests(unittest.TestCase):
    def setUp(self):
        self.gameDetails = GameDetails()

    def testPostBlinds(self):
        self.gameDetails.players = [Player(1000), Player(1000), Player(1000),
                                    Player(1000)]
        self.gameDetails.setActivePlayer(0)
        postBlinds(self.gameDetails)
        self.assertTrue(self.gameDetails.getHandDetails().getPot().getPot(), 15)
        self.assertTrue(self.gameDetails.players[3].getActiveStatus())
        self.assertEqual(self.gameDetails.getHandDetails().getRaised(), 1)
        self.assertEqual(self.gameDetails.players[1].getBankroll(), 995)
        self.assertEqual(self.gameDetails.players[2].getBankroll(), 990)

    def testPostBlindsHeadsUp(self):
        self.gameDetails.players[0].setDealer()
        self.gameDetails.players[1].setNonDealer()
        self.gameDetails.setActivePlayer(0)
        self.gameDetails.setInactivePlayer(1)
        postBlinds(self.gameDetails)
        self.assertTrue(self.gameDetails.getHandDetails().getPot().getPot(), 15)
        self.assertTrue(self.gameDetails.players[0].getActiveStatus())
        self.assertEqual(self.gameDetails.getHandDetails().getRaised(), 1)
        self.assertEqual(self.gameDetails.players[0].getBankroll(), 995)
        self.assertEqual(self.gameDetails.players[1].getBankroll(), 990)
