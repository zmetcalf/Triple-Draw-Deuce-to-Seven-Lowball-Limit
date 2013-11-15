import os, pygame, math
from pygame.locals import *
                             
class Card:

    def __init__(self,frontImage,backImage,x=0,y=0, v=0):
        self.bimg = backImage
        self.fimg = frontImage
        self.img = backImage
        self.side = False # Changed from int to Boolean
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.child = None
        self.parent = None
        self.selected = 0
        self.value = v

    def flip(self):
        if self.side==True:
            self.side = False
            self.img = self.bimg
        else:
            self.side = True
            self.img = self.fimg

    def backSide(self):
        self.side = False
        self.img = self.bimg

    def frontSide(self):
        self.side = True
        self.img = self.fimg

    def setSide(self,side):
        if side:
            self.img = self.fimg
        else:
            self.img = self.bimg
        self.side = side
       
    def move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        if self.child:
            self.child.move(dx,dy)

    def draw(self,surface):
        surface.blit(self.img,self.rect.topleft)
    
    def getSuit(self):
        suit = int(self.value / 13)
        
        if suit == 0:
            return "SPADE"
        elif suit == 1:
            return "CLUB"
        elif suit == 2:
            return "DIAMOND"
        elif suit == 3:
            return "HEART"
    
    def getRank(self):
        rank = (self.value - (int(self.value / 13) * 13))
        
        if rank == 0:
            return "ACE"
        elif rank == 1:
            return "DUECE"
        elif rank == 2:
            return "THREE"
        elif rank == 3:
            return "FOUR"
        elif rank == 4:
            return "FIVE"
        elif rank == 5:
            return "SIX"
        elif rank == 6:
            return "SEVEN"
        elif rank == 7:
            return "EIGHT"
        elif rank == 8:
            return "NINE"
        elif rank == 9:
            return "TEN"
        elif rank == 10:
            return "JACK"
        elif rank == 11:
            return "QUEEN"
        elif rank == 12:
            return "KING"

