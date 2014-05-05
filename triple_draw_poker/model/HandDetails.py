from triple_draw_poker.model.Pot import Pot

class HandDetails:

    def __init__(self):
        self.pot = Pot()
        self.raised = 0
        self.street = 0
        self.number_of_streets = 4
        self.in_draw = False
        self.hands = []
        self.dealt_cards_index = 0

    def getDealtCardsIndex(self):
        return dealt_cards_index

    def getHands(self):
        return self.hands

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

    def getInDraw(self):
        return self.in_draw

    def setDealtCardsIndex(self, index):
        self.dealt_cards_index = index

    def addHand(self, hand):
        self.hands.append(hand)

    def incrementRaised(self):
        self.raised += 1

    def incrementStreet(self):
        self.street += 1

    def changeInDraw(self):
        self.in_draw = not self.in_draw
