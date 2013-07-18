'''
Created on Jul 15, 2013

@author: python09
'''
import pygame
import random

class Menu:
    # the images for the buttons
    playButton = None
    playRect = None    
    optionsButton = None
    optionsRect = None    
    quitButton = None
    quitRect = None
    logo = None
    logoRect = None
    rotatedText = None
    
    # the screen to draw on
    screen = None
    font = None
    pygameControl = None
    
    buttonGap = 10 # the vertical space between buttons
    width = None # the width of the screen
    height = None # height of the screen
    snippit = None # the phrase to display on the menu
    rotateAngle = 30
    snippitX = None
    snippitY = None
    
    def loadSnippit(self):
        loadFile = open('assets/snippets.txt')
        text = loadFile.read()
        snippits = text.split('-')
        rand = random.Random()
        i = rand.randint(0, len(snippits)-1)
        return snippits[i]
    
    def __init__(self, surface, width, height):
        #load the images
        self.playButton = pygame.image.load('assets/GUI/playButton.png')
        self.optionsButton = pygame.image.load('assets/GUI/optionsButton.png')
        self.quitButton = pygame.image.load('assets/GUI/quitButton.png')
        self.logo = pygame.image.load('assets/GUI/logo.png')
        
        #set up the screen  
        self.screen = surface
        self.width = width
        self.height = height
        
        # set up the picture rectangles
        self.quitRect = pygame.Rect((self.width - self.quitButton.get_rect().width)/2, self.height - self.quitButton.get_rect().height - self.buttonGap, self.quitButton.get_rect().width,
                               self.quitButton.get_rect().height)
        self.optionsRect = pygame.Rect(self.quitRect.x, self.quitRect.y - self.optionsButton.get_rect().height - self.buttonGap, self.optionsButton.get_rect().width, 
                                      self.optionsButton.get_rect().height)
        self.playRect = pygame.Rect(self.optionsRect.x, self.optionsRect.y - self.playButton.get_rect().height - self.buttonGap, self.playButton.get_rect().width,
                                    self.playButton.get_rect().height)        
        #scale logo
        temp = self.logo
        self.logo = pygame.transform.scale(temp, (width * 4/5, height/4))
        self.logoRect = pygame.Rect((width - self.logo.get_rect().width)/2, (height - self.logo.get_rect().height)/4, self.logo.get_rect().width, self.logo.get_rect().height)
        
        # set up the snippit
        self.font = pygame.font.SysFont('Arial', 32)        
        self.snippit = self.loadSnippit()     
        self.snippitX = width*2/3
        self.snippitY = height/6
        self.rotate()
        
    def rotate(self):
        pic1 = self.font.render(self.snippit, 1, (255, 255, 0)) # save the text as an image
        self.rotatedText = pygame.transform.rotate(pic1, self.rotateAngle) # rotate the image        
               
    def draw(self):
        self.screen.blit(self.quitButton, (self.quitRect.x, self.quitRect.y))
        self.screen.blit(self.optionsButton, (self.optionsRect.x, self.optionsRect.y))
        self.screen.blit(self.playButton, (self.playRect.x, self.playRect.y))
        self.screen.blit(self.logo, (self.logoRect.x, self.logoRect.y))
        self.screen.blit(self.rotatedText, (self.snippitX, self.snippitY)) #show the image        
    
    #the menu return handler
    def getReturns(self, pos):     
        if self.quitRect.collidepoint(pos): # see if the quit button was clicked
            return 1 # send back the code to quit
        elif self.playRect.collidepoint(pos):
            return 2 #send back the code to play the game
        elif self.optionsRect.collidepoint(pos):
            return 3
            
                    