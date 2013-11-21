class Player:

    def __init__(self, bankroll):
        self.is_player_view = False
        self.bankroll = bankroll
        self.bet_this_hand = 0.0
        self.is_active = False
        self.is_dealer = False
        self.in_hand = True
        self.is_SB = False
        self.is_BB = False

    def getPlayerViewStatus(self):
        return self.is_player_view

    def getDealerStatus(self):
        return self.is_dealer

    def getBetThisHand(self):
        return self.bet_this_hand

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
        self.bet_this_hand = 0.5
        self.is_SB = True

    def setIsBB(self):
        self.bet_this_hand = 1
        self.is_BB = True

    def collectPot(self, amount):
        self.bankroll += amount

    def bet(self, amount, raises):
        self.bankroll -= amount
        self.bet_this_hand += (1 + raises)

    def getBankroll(self):
        return self.bankroll
