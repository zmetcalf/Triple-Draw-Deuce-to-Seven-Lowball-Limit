class PlayerHand:

    def __init__(self, player):
        self.player = player
        self.hand = []

    def getHand(self):
        return self.hand

    def getPlayer(self):
        return self.player

    def addCard(self, card):
        self.hand.append(card)

    def discardCard(self, card):
        self.hand.remove(card)
