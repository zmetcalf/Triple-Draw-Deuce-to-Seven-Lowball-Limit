class Player:

    def __init__(self, bankroll):
        self.hand = []
        self.is_player_view = False
        self.bankroll = bankroll
        self.bet_this_street = 0.0
        self.is_active = False
        self.is_raiser = False
        self.is_dealer = False
        self.in_hand = True
        self.is_sitting_out = False
        self.is_SB = False
        self.is_BB = False

    def getHand(self):
        return self.hand

    def getPlayerViewStatus(self):
        return self.is_player_view

    def getDealerStatus(self):
        return self.is_dealer

    def getBetThisStreet(self):
        return self.bet_this_street

    def getActiveStatus(self):
        return self.is_active

    def getRaiserStatus(self):
        return self.is_raiser

    def getInHand(self):
        return self.in_hand

    def getSittingOut(self):
        return self.is_sitting_out

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

    def setRaiser(self):
        self.is_raiser = True

    def setNonRaiser(self):
        self.is_raiser = False

    def setOutOfHand(self):
        self.in_hand = False

    def sitOut(self):
        self.is_sitting_out = True

    def sitIn(self):
        self.is_sitting_in = True

    def setIsSB(self):
        self.bet_this_street = 0.5
        self.is_SB = True

    def setIsBB(self):
        self.bet_this_street = 1
        self.is_BB = True

    def drawCard(self, card):
        self.hand.append(card)

    def discardCard(self, card):
        self.hand.remove(card)

    def foldHand(self):
        self.hand = []

    def collectPot(self, amount):
        self.bankroll += amount

    def bet(self, amount, raises):
        self.bankroll -= amount
        self.bet_this_street += (1 + raises)

    def getBankroll(self):
        return self.bankroll
