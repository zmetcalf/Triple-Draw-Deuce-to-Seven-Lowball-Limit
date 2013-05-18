import os, pygame, math
from pygame.locals import *

class Button:
    
    def __init__(self, textToButton):
        self.textToButton = textToButton
        self.buttonImage = pygame.Surface((50, 25), 1).convert()
        self.buttonImage.fill((255, 0, 0))
        self.textImage = pygame.font.Font("FreeSans.ttf", 18).render(
                                        self.textToButton, True, (0, 0, 0))

    def draw(self, surface, x, y):
        surface.blit(self.buttonImage, (x, y))
