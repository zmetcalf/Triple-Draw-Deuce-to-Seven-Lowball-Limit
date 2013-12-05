import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.PlayerController import advanceDealer, \
      setRaiser, changeActivePlayer
from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.Player import Player

class PlayerControllerTests(unittest.TestCase):
    def setUp(self):
        self.game_details = GameDetails()

    def testAdvanceDealerSimple(self):
        self.game_details.players[0].setDealer()
        self.game_details.players[1].setNonDealer()
        advanceDealer(self.game_details.getPlayers())
        self.assertFalse(self.game_details.players[0].getDealerStatus())
        self.assertTrue(self.game_details.players[1].getDealerStatus())

    def testAdvanceDealerRoundTheBend(self):
        self.game_details.players[0].setNonDealer()
        self.game_details.players[1].setDealer()
        advanceDealer(self.game_details.getPlayers())
        self.assertFalse(self.game_details.players[1].getDealerStatus())
        self.assertTrue(self.game_details.players[0].getDealerStatus())

    def testSetRaiser(self):
        self.game_details.players[0].setActive()
        self.game_details.players[1].setRaiser()
        setRaiser(self.game_details.getPlayers())
        self.assertTrue(self.game_details.players[0].getRaiserStatus())
        self.assertFalse(self.game_details.players[1].getRaiserStatus())

    def testChangeActivePlayerSimple(self):
        players = [Player(1), Player(1), Player(1), Player(1)]
        players[2].setActive()
        changeActivePlayer(players)
        self.assertFalse(players[0].getActiveStatus())
        self.assertFalse(players[1].getActiveStatus())
        self.assertFalse(players[2].getActiveStatus())
        self.assertTrue(players[3].getActiveStatus())

    def testChangeActivePlayerRoundTheBend(self):
        players = [Player(1), Player(1), Player(1), Player(1)]
        players[3].setActive()
        changeActivePlayer(players)
        self.assertTrue(players[0].getActiveStatus())
        self.assertFalse(players[1].getActiveStatus())
        self.assertFalse(players[2].getActiveStatus())
        self.assertFalse(players[3].getActiveStatus())

if __name__ == '__main__':
    unittest.main()
