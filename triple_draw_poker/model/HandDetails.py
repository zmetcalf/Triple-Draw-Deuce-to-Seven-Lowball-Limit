from triple_draw_poker.model.Pot import Pot

class HandDetails:

    def __init__(self):
        self.pot = Pot()
        self.raised = 0
        self.street = 0

    def getPot(self):
        return self.pot.getPot()

    def getRaised(self):
        return self.raised

    def getStreetPremium(self):
        if self.street < 3:
            return 2
        return 1

    def incrementRaised(self):
        self.raised += 1

