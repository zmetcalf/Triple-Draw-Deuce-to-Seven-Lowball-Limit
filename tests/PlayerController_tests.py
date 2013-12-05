import sys
import unittest

sys.path.append('../../Triple-Draw-Deuce-to-Seven-Lowball-Limit')

from triple_draw_poker.controller.PlayerController import advanceDealer, \
      setRaiser
from triple_draw_poker.model.GameDetails import GameDetails

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

if __name__ == '__main__':
    unittest.main()
