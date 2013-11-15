import os, pygame, math
from pygame.locals import *

class Button:
    
    def __init__(self, textToButton, x, y):
        self.textToButton = textToButton
        self.x = x
        self.y = y
        self.buttonImage = pygame.Surface((100, 50), 1).convert()
        self.buttonImage.fill((255, 0, 0))
        self.textImage = pygame.font.Font("FreeSans.ttf", 18).render(
                                        self.textToButton, True, (0, 0, 0))

    def draw(self, surface):
        surface.blit(self.buttonImage, (self.x, self.y))
        surface.blit(self.textImage, (self.x + 30, self.y + 15))
        
    def pressed(self, x, y): 
        if self.x < x and self.x + 100 > x and self.y < y and self.y + 50 > y:
            return True
    
    def changeName(self, newName):
        self.textImage = pygame.font.Font("FreeSans.ttf", 18).render(
                                        newName, True, (0, 0, 0))

