class Bankroll:
    
    def __init__(self, initialRoll):
        self.bankroll = initialRoll
        
    def incrementRoll(self, amount):
        self.bankroll += amount
        
    def decrementRoll(self, amount):
        self.bankroll -= amount
        
    def getBankroll(self):
        return self.bankroll
