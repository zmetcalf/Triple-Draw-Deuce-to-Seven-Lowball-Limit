from triple_draw_poker.model.Pot import Pot

class HandDetails:

    def __init__(self):
        self.pot = Pot()
        self.raised = 0
        self.street = 0
        self.number_of_streets = 4

    def getPot(self):
        return self.pot

    def getRaised(self):
        return self.raised

    def getStreet(self):
        return self.street

    def getStreetPremium(self):
        if self.street < 3:
            return 2
        return 1

    def getNumberOfStreets(self):
        return self.number_of_streets

    def incrementRaised(self):
        self.raised += 1

    def incrementStreet(self):
        self.street += 1
