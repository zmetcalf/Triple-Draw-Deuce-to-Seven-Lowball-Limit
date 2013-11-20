class Player:

    def __init__(self, initialRoll):
        self.is_player_view = False
        self.bankroll = initialRoll
        self.is_active = False
        self.is_dealer = False
        self.in_hand = True
        self.is_SB = False
        self.is_BB = False

    def getPlayerViewStatus(self):
        return self.is_player_view

    def getDealerStatus(self):
        return self.is_dealer

    def getActiveStatus(self):
        return self.is_active

    def getInHand(self):
        return self.in_hand

    def getIsSB(self):
        return self.is_SB

    def getIsBB(self):
        return self.is_BB

    def setPlayerViewStatus(self):
        self.is_player_view = True

    def setActive(self):
        self.is_active = True

    def setDealer(self):
        self.is_dealer = True

    def setInactive(self):
        self.is_active = False

    def setNonDealer(self):
        self.is_dealer = False

    def setOutOfHand(self):
        self.in_hand = False

    def setIsSB(self):
        self.is_SB = True

    def setIsBB(self):
        self.is_BB = True

    def collectPot(self, amount):
        self.bankroll += amount

    def bet(self, amount):
        self.bankroll -= amount

    def getBankroll(self):
        return self.bankroll
