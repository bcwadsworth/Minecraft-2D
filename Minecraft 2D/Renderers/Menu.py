'''
Created on Jul 15, 2013

@author: python09
'''
import pygame

class Menu:
    # the images for the buttons
    playButton = None
    playRect = None    
    optionsButton = None
    optionsRect = None    
    quitButton = None
    quitRect = None
    # the screen to draw on
    screen = None
    pygameControl = None
    
    buttonGap = 10 # the vertical space between buttons
    width = None # the width of the screen
    height = None # height of the screen
    
    def __init__(self, surface, width, height):
        pygame.init()
        self.playButton = pygame.image.load('assets/GUI/playButton.png')
        self.optionsButton = pygame.image.load('assets/GUI/optionsButton.png')
        self.quitButton = pygame.image.load('assets/GUI/quitButton.png')        
        self.screen = surface
        self.width = width
        self.height = height
        self.quitRect = pygame.Rect((self.width - self.quitButton.get_rect().width)/2, self.height - self.quitButton.get_rect().height - self.buttonGap, self.quitButton.get_rect().width,
                               self.quitButton.get_rect().height)
        self.optionsRect = pygame.Rect(self.quitRect.x, self.quitRect.y - self.optionsButton.get_rect().height - self.buttonGap, self.optionsButton.get_rect().width, 
                                      self.optionsButton.get_rect().height)
        self.playRect = pygame.Rect(self.optionsRect.x, self.optionsRect.y - self.playButton.get_rect().height - self.buttonGap, self.playButton.get_rect().width,
                                    self.playButton.get_rect().height)
        
    def draw(self):
        self.screen.blit(self.quitButton, (self.quitRect.x, self.quitRect.y))
        self.screen.blit(self.optionsButton, (self.optionsRect.x, self.optionsRect.y))
        self.screen.blit(self.playButton, (self.playRect.x, self.playRect.y))
    
    #the event handler
    def getEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:     
            if self.quitRect.collidepoint(event.pos): # see if the quit button was clicked
                return 1 # send back the code to quit
            elif self.playRect.collidepoint(event.pos):
                return 2 #send back the code to play the game
            elif self.optionsRect.collidepoint(event.pos):
                return 3
                    