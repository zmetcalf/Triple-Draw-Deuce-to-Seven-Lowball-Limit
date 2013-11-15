import os, pygame, math
from pygame.locals import *
                             
class CardImages:

    cardImages = []
    backImage = None

    def __init__(self):
    
        colors = ['s','c','d','h']
        values = ['a','2','3','4','5','6','7','8','9','t','j','q','k']

        for c in colors:
            for v in values:
                self.cardImages.append(pygame.image.load("./cards/%s%s.gif" % (v,c)).convert())
        self.backImage = pygame.image.load("./cards/b.gif").convert()

    def getCardNbr(self,nbr):
        return self.cardImages[nbr]

    def getBack(self):
        return self.backImage
