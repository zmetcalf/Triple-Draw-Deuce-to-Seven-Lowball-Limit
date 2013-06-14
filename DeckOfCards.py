"""
    Original Source Code from http://arainyday.se/projects/python/DeckOfCards/
    Card graphics are GPL and made by John K. Estell.
    Source code are GPL and made by John Eriksson.
    Source code modifications from Solitare to 2-7 Triple Draw Lowball
        are GPL and made by Zach Metcalf
"""
#/usr/bin/env python
#pygame.init() called in main loop
# started changing 1,0 to True, False before reading PEP 285 but may continue for readability.

#popsingle can go - only applicable to solitare games.

import os, pygame, math, sys # added sys to make it work better w/win & mac quit functions
from pygame.locals import * # Imports all the constants
import random

from ButtonGroup import ButtonGroup
from CardImages import CardImages
from CardGroup import CardGroup
from Card import Card
from GameHandler import GameHandler

class DeckOfCards:

    INITIAL_DEAL = 1
    FIRST_DRAW = 2
    SECOND_DRAW= 3
    THIRD_DRAW = 4
    END_OF_HAND = 5

    def dealHands(self): 
        #dealerDeck = self.cardGroup # initializes cardGroup object dealer deck
        self.cardGroup.collectAll(15,15) # puts cards face down on deal deck
        self.cardGroup.shuffle() # shuffle's cards

        self.cardIndex = 0
        x1 = 15
        y1 = 215
        x2 = 15
        y2 = 415

        self.burnDeck.append(self.cardGroup.cards[self.cardIndex])
        self.cardIndex += 1
        self.burnDeck[0].rect.x = 500
        self.burnDeck[0].rect.y = 500
        self.burnDeck[0].flip()
        for hand in range(5):
            self.northDeck.append(self.cardGroup.cards[self.cardIndex])
            self.northDeck[hand].rect.x = x1
            self.northDeck[hand].rect.y = y1
            self.northDeck[hand].flip()
            x1 += 20
            self.cardIndex += 1
            
            self.southDeck.append(self.cardGroup.cards[self.cardIndex])
            self.southDeck[hand].rect.x = x2
            self.southDeck[hand].rect.y = y2
            self.southDeck[hand].flip()
            x2 += 20
            self.cardIndex += 1
            # dealerDeck.dropCard(displayCard) # not sure I know what this does
        
        # Shows remaining deck
        x = 15
        y = 100
        for cols in range(41): #change to idx
            c = self.cardGroup.cards[self.cardIndex]
            self.cardIndex+=1
            c.flip()
            c.rect.x = x
            c.rect.y = y
            #self.cardGroup.dropCard(c)
            #cards+=1
            x+=12

    def drawCards(self):
        x = 1

    def redeal(self):
        self.selectionCards = [] # clears selection cards from list
        self.burnDeck = []
        self.northDeck = []
        self.southDeck = []
        self.cardGroup.collectAll(30,30) # moves cards to 'talon'
        self.cardGroup.shuffle() 

    def manageAction(self, action):
        if action == 'CAP':
            x = 1;
        if action == 'DRAW':
            advanceStreet()

    def advanceStreet(self):
        if self.mode == self.INITIAL_DEAL:
            self.dealHands()
            # self.buttonGroup[0].changeName("Check") # Does not work with button group
        elif self.mode >= self.FIRST_DRAW and self.mode <= self.THIRD_DRAW:
            self.drawCards()
        elif self.mode == self.END_OF_HAND:
            self.redeal()
            self.dealHands()
            self.mode = 0
        self.mode += 1

#----KEEP HISTORY FOR POSSIBLE HAND ANALYSIS---
#----History Constant a list-------------------
    MAX_HISTORY = 30
    history = []
    
    def clearHistory(self):
        self.history = []

    def pushHistory(self,desc):
        #print "Pushing: %s" % desc
        while len(self.history) > self.MAX_HISTORY:
            self.history.pop(0)
        
        # store get the z-order
        cards = self.cardGroup.cards[:]
        
        # store card info
        cardinfo = []
        for c in cards:
            info = []
            info.append(c.side)
            info.append(c.rect.topleft)
            info.append(c.child)
            info.append(c.parent)
            info.append(c.selected)
            cardinfo.append(info)
        
        if len(self.selectionCards):
            selcards = self.selectionCards[:]
        else:
            selrect = pygame.Rect((0,0,0,0))
            selcards = []  
       
        self.history.append([cards,cardinfo,selrect,selcards,desc])
#---------Undo last action--------------------------------------------- 
    def popHistory(self):
        if not len(self.history):
            return
    
        hi = self.history.pop()
        
        cards = hi[0]
        
        i = 0
        for ci in hi[1]:
            cards[i].setSide(ci[0])
            cards[i].rect.topleft = ci[1]
            cards[i].child = ci[2]
            cards[i].parent = ci[3]
            cards[i].selected = ci[4]            
            i+=1
            
        self.cardGroup.cards = cards    
        self.selectionCards = hi[3]        
                

#-------------Help file text----------------------------- 
    text = [
        "Triple Draw 2-7 Lowball Limit Pre-Alpha",
        "-----------------------",
        "F1 - Display this help text.",
        "F2 - Collect cards and shuffle deck.",
        "F3 - Setup for Klondike solitaire.",
        "Ctrl+T - Toggle sticky cards.",
        "Ctrl+S - Shuffle selected cards.",
        "Ctrl+Z - Undo latest action.",
        "-----------------------",
        "press any key to continue"]
#---------------------------------------------------------

    def mainLoop(self):    
        pygame.init() # required for pygame

        self.screen = pygame.display.set_mode((640, 480),HWSURFACE|RESIZABLE) # intializes screen
        pygame.display.set_caption('Triple Draw Deuce to Seven Lowball Limit') # sets caption of window
                              
        self.selectedCard = None # argument of selectedCard defined
    
        self.selectionRect = pygame.Rect((0,0,0,0)) # not sure if this creates pygame object, but should select a rectangle of pixels?
        self.selectionCards = []  # initialize list of seclectionCards
               
        ci = CardImages() # ci creates a deck of cards
 
        cards = [] # initialize list of cards
        
        # loop through 52 cards - cards.append adds card to list -
        # Card() Creates object with the variables from ci which is list cardImages to pull from
        # the remaining parts in Card() 30, 30  places the top left of card at 30 right 30 down
        for i in range(0,52):
            cards.append(Card(ci.getCardNbr(i),ci.getBack(), 30, 30, i)) 
                   
        self.cardGroup = CardGroup(cards) # creates cardGroup object from card list
        self.cardGroup.shuffle() # uses shuffle function on cardGroup
         
        self.burnDeck = []
        self.northDeck = []
        self.southDeck = []

        self.gameHandler = GameHandler(1, 1000)
                
        self.mode = self.INITIAL_DEAL
                        
#-------------------Prints menu on screen--------------------
        self.helptext = pygame.Surface((380,420),1).convert()
        self.helptext.fill((0x0, 0x0, 0x0))
        self.helptext.set_alpha(200);
        self.helptextRect = self.helptext.get_rect()
                
        font = pygame.font.Font("FreeSans.ttf", 18)
        ty = 8
        for t in self.text:
            img = font.render(t, 1, (0xff, 0xff, 0))
            r = img.get_rect()
            r.top = ty
            r.centerx = self.helptextRect.centerx
            ty += 25
            self.helptext.blit(img,r.topleft)
        
        viewhelp = True # changed this and all references to boolean
        sr = self.screen.get_rect()
        self.helptextRect.centerx = sr.centerx #autocenter help on screen
        self.helptextRect.centery = sr.centery #autocenter help on screen       

        self.buttonGroup = ButtonGroup()

        lctrlDown = False
        rctrlDown = False
        lshiftDown = False
        rshiftDown = False
                                            
        while True:                                                                      
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit(); sys.exit(); # used this instead of return for better compatability
                    #return # uses return to break infinite loop
                # performs resize of screen and help box
                elif event.type == VIDEORESIZE:
                    self.screen = pygame.display.set_mode(event.size,HWSURFACE|RESIZABLE)
                    if viewhelp:
                        sr = self.screen.get_rect()
                        self.helptextRect.centerx = sr.centerx
                        self.helptextRect.centery = sr.centery
                # waits for keystroke to preform action        
                elif event.type == KEYDOWN:          
                    #print "key = %s" % str(event.key) #looks like author's old test code
                    #print "keyname = %s" % pygame.key.name(event.key) #same here
                    if viewhelp:
                        if event.key == K_ESCAPE:
                            pygame.quit(); sys.exit(); # used this instead of return
                            # return # uses return to break infinite loop               
                        viewhelp=False # press any key and screen goes away
                        self.advanceStreet()
                        continue # continue restarts loop so it does not execute any keystroke                                                 
                    if event.key == K_ESCAPE:
                        pygame.quit(); sys.exit(); # used this instead of return
                        # return # uses return to break infinite loop                   
                    elif event.key == K_LCTRL: # code to show ctrl key pushed
                        lctrlDown = True        
                    elif event.key == K_RCTRL: # code to show ctrl key pushed
                        rctrlDown = True        
                    elif event.key == K_LSHIFT: # code to show shift key pushed
                        lshiftDown = True        
                    elif event.key == K_RSHIFT: # code to show shift key pushed
                        rshiftDown = True        
                    elif event.key == K_z and (lctrlDown or rctrlDown): # Changed from keynumber 122 to K_z http://www.pygame.org/docs/ref/key.html Did this to create continuity and readability                
                            self.popHistory() # triggers undo function
                    elif event.key == K_t and (lctrlDown or rctrlDown): # Changed from keynumber 116 to K_t                       
                        if popsingle: #toggles 'sticky'
                            popsingle = False
                        else:
                            popsingle = True
                    elif event.key == K_s and (lctrlDown or rctrlDown):    # Changed from keynumber 115 to K_s                   
                        self.pushHistory("Selection shuffle") # Adds item to history for undo
                        self.shuffleSelection() # Shuffles selected cards - testing mechinism, but may be useful in large 2-7 Triple Draw game
                    elif event.key == K_F1: # display's help file
                        if self.mode == self.END_OF_HAND:
                            sr = self.screen.get_rect() # if you comment out this and the next two lines, it does not center on reload
                            self.helptextRect.centerx = sr.centerx
                            self.helptextRect.centery = sr.centery                            
                            viewhelp = True
                    elif event.key == K_F2: # collects cards and shuffle's deck
                        self.pushHistory("F2") # adds item to undo
                        self.selectionCards = [] # clears selection cards from list
                        self.burnDeck = []
                        self.northDeck = []
                        self.southDeck = []
                        self.cardGroup.collectAll(30,30) # moves cards to 'talon'
                        self.cardGroup.shuffle() # shuffle's cards
                    elif event.key == K_F3: # deals hands
                        self.pushHistory("Setup Klondike") # adds item to undo
                        self.dealHands() # deals hand
                          
                elif event.type == KEYUP: #These log the CTRL/SHIFT key going up          
                    if event.key == K_LCTRL:
                        lctrlDown = False        
                    elif event.key == K_RCTRL:
                        rctrlDown = False        
                    elif event.key == K_LSHIFT:
                        lshiftDown = False        
                    elif event.key == K_RSHIFT:
                        rshiftDown = False        
                        
                elif event.type == MOUSEBUTTONDOWN and viewhelp == False: #starts mouseclick code if help is not showing
                    if event.button == 1:
                        self.selectedCard = self.cardGroup.getOneCard(
                            event.pos[0],event.pos[1]) # code to select a card
                        if self.selectedCard:
                            if  any(self.selectedCard == val for val in
                                self.selectionCards) == False and any(
                                self.selectedCard == val for val in
                                self.southDeck):
                                tempY = self.selectedCard.rect.y
                                self.selectedCard.rect.y = tempY - 20
                                self.selectionCards.append(self.selectedCard)
                        self.buttonReturn = self.buttonGroup.pressed(
                                            event.pos[0], event.pos[1])
                        if self.buttonReturn:
                            self.manageAction(self.gameHandler.setAction(self.buttonReturn, "NORTH"))
                            print self.buttonReturn
                            self.buttonGroup.hideButton(self.buttonReturn)
                            
            # DRAWING - Code good for now.
            self.screen.fill((0x00, 0xb0, 0x00))

            self.cardGroup.draw(self.screen)
            self.buttonGroup.draw(self.screen)
            if viewhelp:
                self.screen.blit(self.helptext,self.helptextRect.topleft)

            pygame.display.flip()

def main():
    g = DeckOfCards()
    g.mainLoop()

#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
