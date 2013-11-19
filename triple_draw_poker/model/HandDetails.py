from triple_draw_poker.model.Pot import Pot

class HandDetails:

    def __init__(self):
        self.pot = Pot()
        self.raised = False

    def getPot(self):
        return self.pot.getPot()
