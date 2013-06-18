from Player import Player

import random

class GameHandler:
    
    def __init__(self, opponents, bankroll):
        self.raiseCount = 0

        self.players = [] 
        for i in range(0, opponents):
            self.players.append(Player(bankroll)) 
            
        self.opponents = opponents
        self.initDealer()
        self.betLevel = 10
        self.pot = 0
        self.activeCheck = False
        
    def setAction(self, action, player):
        if self.players[player].getActiveStatus():
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
        self.players[random.randint(0, self.opponents)].setDealer()
    
    def setDealer(self):
        x = 0
        
        for i in self.players:
            if i.getDealerStatus():
                x = i.index()
                break
        
        self.players[x].setNonDealer()
        if x == self.opponents:
            self.players[0].setDealer()
        else:
            self.players[x + 1].setDealer()
        
    def changeActionPlayer(self):
        x = 0
        
        for i in self.players:
            if i.getActiveStatus():
                x = i.index()
                break
                
        self.players[x].setInactive()
        if x == self.opponents:
            self.players[0].setActive()
        else:
            self.players[x + 1].setActive()
    
    def postBlinds(self):
        if self.dealer: 
            # northBankroll.decrementRoll(5)
            # southBankroll.decrementRoll(10)
            x = 1
        else:
            x = 1
            # northBankroll.decrementRoll(10)
            # southBankroll.decrementRoll(5)
        self.pot = 15
        
    def bet(self, bet):
        for i in self.players:
            if i.getActiveStatus():
                i.bet(bet)
    
    def resetAction(self):
        self.pot = 0
        self.setDealer()
        self.postBlinds()
    
    def setForDraw(self):
        self.activeCheck = False
