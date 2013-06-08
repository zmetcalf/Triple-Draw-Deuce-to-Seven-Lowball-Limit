import random

from Bankroll import Bankroll

class GameHandler:
    
    def __init__(self):
        self.raiseCount = 0
        self.northBankroll = Bankroll(1000)
        self.southBankroll = Bankroll(1000)
        self.dealer = random.randint(0, 1) # 1 = north is dealer
        self.actionPlayer = self.dealer
        self.pot = 0
        
    def setAction(self, action):
        if self.pot == 15:
            if action == "CheckDraw":
                x = 1
        if self.raiseCount < 4:
            x = 1
        return True
        
    def setDealer(self):
        if self.dealer:
            self.dealer == False
        else:
            self.dealer == True
    
    def postBlinds(self):
        if self.dealer: 
            northBankroll.decrementRoll(5)
            southBankroll.decrementRoll(10)
        else:
            northBankroll.decrementRoll(10)
            southBankroll.decrementRoll(5)
        self.pot = 15
        
    def resetAction(self):
        self.pot = 0
        self.setDealer()
        self.postBlinds()
