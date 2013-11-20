from triple_draw_poker.model.GameDetails import GameDetails
from triple_draw_poker.model.Pot import Pot

class HandDetails:

    def __init__(self, GameDetails):
        self.game_details = GameDetails
        self.pot = Pot()
        self.raised = False

    def getPot(self):
        return self.pot.getPot()
