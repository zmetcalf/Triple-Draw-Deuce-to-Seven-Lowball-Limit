import random

from Bankroll import Bankroll

# Change North/South to position number

class GameHandler:
    
    def __init__(self, opponents, bankroll):
        self.raiseCount = 0
        self.player = [opponents]
        self.northBankroll = Bankroll(bankroll)
        self.southBankroll = Bankroll(bankroll)
        self.dealer = self.initDealer()
        self.actionPlayer = self.dealer
        self.betLevel = 10
        self.pot = 0
        self.activeCheck = False
        
    def setAction(self, action, player):
        if self.actionPlayer == player:
            if self.pot == 15: # Handles Dealer Small Blind
                if action == "CheckDraw":
                    self.raiseCount = 1
                    self.activeCheck = True
                elif action == "BetRaise":
                    self.raiseCount = 2
                elif action == "Fold":
                    self.resetAction()
            elif self.raiseCount < 4:
                if action == "CheckDraw": 
                    if self.activeCheck:
                        self.setForDraw()
                        return "Draw"
                    else:
                        self.activeCheck = True
                        self.changeActionPlayer()
                elif action == "BetRaise":
                    self.raiseCount += 1
            elif self.raiseCount == 4:
                if action == "CheckDraw":
                    x = 1
                elif action == "Fold":
                    self.resetAction()
        else:
            return False
        
    def initDealer(self):
        if random.randint(0, 1):
            self.dealer = 'NORTH'
        else:
            self.dealer = 'SOUTH'
    
    def setDealer(self):
        if self.dealer == 'NORTH':
            self.dealer = 'SOUTH'
        else:
            self.dealer = 'NORTH'
            
    def changeActionPlayer(self):
        if self.actionPlayer == 'NORTH':
            self.actionPlayer == 'SOUTH'
        else:
            self.actionPlayer == 'NORTH'
    
    def postBlinds(self):
        if self.dealer: 
            northBankroll.decrementRoll(5)
            southBankroll.decrementRoll(10)
        else:
            northBankroll.decrementRoll(10)
            southBankroll.decrementRoll(5)
        self.pot = 15
        
    def bet(self, bet, player):
        if player == 'NORTH':
            northBankroll.decrementRoll(bet)
        else:
            southBankroll.decrementRoll(bet)
            
    def getBankroll(self, player):
        if player == 'NORTH':
            return northBankroll.getBankroll()
        else:
            return southBankroll.getBankroll()
        
    def resetAction(self):
        self.pot = 0
        self.setDealer()
        self.postBlinds()
    
    def setForDraw(self):
        self.activeCheck = False
