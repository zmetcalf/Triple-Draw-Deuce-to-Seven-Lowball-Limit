from Player import Player

import random

class GameHandler:
    
    def __init__(self, numberOfPlayers, bankroll, isTest):
        self.raiseCount = 0

        self.players = [] 
        for i in range(0, numberOfPlayers):
            self.players.append(Player(bankroll)) 
        self.activePlayers = numberOfPlayers
        self.opponents = numberOfPlayers - 1
        self.isTest = isTest
        self.pointer = 0
        self.initDealer()
        self.betLevel = 10
        self.pot = 0
        self.activeCheck = False
        self.isInitialRound = True
        
        
    def setAction(self, action, player):
        if self.players[player].getActiveStatus():
            if self.opponents == 1 and self.isInitialRound:
                return self.headsUp1stSt(action, player)
            elif self.opponents > 1 and self.isInitialRound:
                return self.multiHand1stSt(action, player)
            
            
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
                elif action == "Fold":
                    self.activePlayers -= 1
                    self.nextActive()
            elif self.raiseCount == 4:
                if action == "CheckDraw":
                    x = 1
                elif action == "Fold":
                    self.resetAction()
        else:
            return False
        
    def initDealer(self):
        if self.isTest:
            x = 0
        else:
            x = random.randint(0, self.opponents)
        self.players[x].setDealer()
        self.pointer = x
        if self.opponents > 1:
            self.advancePointer()
        
    def setDealer(self):
        x = 0
        
        for i in self.players:
            if i.getDealerStatus():
                x = i.index()
                break
        
        self.players[x].setNonDealer()
        self.pointer = x
        self.players[self.advancePointer()].setDealer()
        if self.opponents > 1:
            self.advancePointer()
        
    def changeActionPlayer(self):
        self.players[self.pointer].setInactive()
        for i in range(0, self.activePlayers):
            self.advancePointer()
            if self.players[self.pointer].getInHand():
                self.players[self.pointer].setActive()
                return True
        return False
        
    def postBlinds(self):
        self.players[self.pointer].bet(self.betLevel / 2)
        self.players[self.advancePointer()].bet(self.betLevel)
        self.players[self.advancePointer()].setActive()
                
    def advancePointer(self):
        if self.pointer == self.opponents:
            self.pointer = 0
        else:
            self.pointer += 1
        return self.pointer
        
    def bet(self, bet):
        for i in self.players:
            if i.getActiveStatus():
                i.bet(bet)
        self.pot += bet
    
    def resetAction(self):
        self.pot = 0
        self.setDealer()
        self.postBlinds()
    
    def setForDraw(self):
        self.activeCheck = False
        self.isInitialRound = False
        x = 0
        
        for i in self.players:
            if i.getDealerStatus():
                x = i.index()
                break
        
        self.pointer = x
        self.players[self.advancePointer()].setActive()
        
    def headsUp1stSt(self, action, player):
        if self.raiseCount == 0:
            if action == "CheckDraw": # Call
                self.raiseCount = 1
                self.bet(self.betLevel / 2)
                self.activeCheck = True
            elif action == "BetRaise": # Raise
                self.raiseCount = 2
                self.bet(self.betLevel * 1.5)
                self.activeCheck = False
            elif action == "Fold":
                self.resetAction()
        elif self.players[player].getIsBB() and False: # Needs fixed
                if action == "CheckDraw":
                    self.setForDraw()
                    return "Draw"
                elif action == "BetRaise":
                    self.bet(self.betLevel)
                    self.raiseCount = 2
                    self.activeCheck = False
        elif 4 > self.raiseCount > 1:
            if action == "CheckDraw" and self.activeCheck == False:
                self.bet(self.betLevel)
                self.activeCheck = True
            elif action == "CheckDraw" and self.activeCheck == True:
                self.activeCheck == False
                self.setForDraw()
                return "Draw"
            elif action == "BetRaise":
                self.bet(self.betLevel * 2)
                self.activeCheck = False
                self.raiseCount += 1
            elif action == "Fold":
                self.resetAction()
        elif self.raiseCount == 4:
            if action == "CheckDraw":
                self.bet(self.betLevel)
                self.setForDraw()
                return "Draw"
            elif action == "Fold":
                self.resetAction()
            
        if action != "Fold":
            self.changeActionPlayer()
             
        
    def multiHand1stSt(self, action):
        return False
