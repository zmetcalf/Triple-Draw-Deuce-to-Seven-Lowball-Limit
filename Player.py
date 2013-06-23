class Player:
    
    def __init__(self, initialRoll):
        self.bankroll = initialRoll
        self.isActive = False
        self.isDealer = False
        self.inHand = True
        self.isSB = False
        self.isBB = False
        
    def getDealerStatus(self):
        return self.isDealer
        
    def getActiveStatus(self):
        return self.isActive
    
    def getInHand(self):
        return self.inHand
        
    def getIsSB(self):
        return self.isSB
    
    def getIsBB(self):
        return self.isBB
        
    def setActive(self):
        self.isActive = True
    
    def setDealer(self):
        self.isDealer = True
        
    def setInactive(self):
        self.isActive = False
        
    def setNonDealer(self):
        self.isDealer = False
        
    def setOutOfHand(self):
        self.inHand = False
        
    def setIsSB(self):
        self.isSB = True
        
    def setIsBB(self):
        self.isBB = True
        
    def collectPot(self, amount):
        self.bankroll += amount
        
    def bet(self, amount):
        self.bankroll -= amount
        
    def getBankroll(self):
        return self.bankroll
