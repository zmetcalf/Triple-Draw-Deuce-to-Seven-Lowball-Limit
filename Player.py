class Player:
    
    def __init__(self, initialRoll):
        self.bankroll = initialRoll
        self.isActive = False
        self.isDealer = False
        self.inHand = True
        self.isSB = False
        
    def getDealerStatus(self):
        return self.isDealer
        
    def getActiveStatus(self):
        return self.isActive
    
    def getInHand(self):
        return self.inHand
        
    def getIsSB(self):
        return self.isSB
        
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
        
    def collectPot(self, amount):
        self.bankroll += amount
        
    def bet(self, amount):
        self.bankroll -= amount
        
    def getBankroll(self):
        return self.bankroll
