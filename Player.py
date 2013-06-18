class Player:
    
    def __init__(self, initialRoll):
        self.bankroll = initialRoll
        self.isActive = False
        self.isDealer = False
        
    def getDealerStatus(self):
        return self.isDealer
        
    def getActiveStatus(self):
        return self.isActive
        
    def setActive(self):
        self.isActive = True
    
    def setDealer(self):
        self.isDealer = True
        
    def setInactive(self):
        self.isActive = False
        
    def setNonDealer(self):
        self.isDealer = False
        
    def collectPot(self, amount):
        self.bankroll += amount
        
    def bet(self, amount):
        self.bankroll -= amount
        
    def getBankroll(self):
        return self.bankroll
    
