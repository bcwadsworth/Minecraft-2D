'''
Created on Jul 15, 2013

@author: python09
'''
import pygame

class Menu:
    # the images for the buttons
    playButton = None
    optionsButton = None
    quitButton = None
    # the screen to draw on
    screen = None
    
    def __init__(self, surface):
        self.playButton = pygame.image.load('assets/GUI/playButton.png')
        self.optionsButton = pygame.image.load('assets/GUI/optionsButton.png')
        self.quitButton = pygame.image.load('assets/GUI/quitButton.png')
        self.screen = surface
        
    def draw(self):
        self.screen.blit(self.quitButton, (0, 0))
    
    #the event handler
    def getEvents(self):
        print("GetEvents working")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quitButton.get_rect().contains(event.pos):
                    return 0
                    