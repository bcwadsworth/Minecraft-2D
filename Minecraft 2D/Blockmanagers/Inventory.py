'''
Created on Jul 15, 2013

@author: python09
'''
import pygame
import pdb

class storeinventory:
    slots = None
    inventoryPic = None
    inventoryRect = None
    picWidth = 0
    picHeight = 0
    screenWidth = 0
    screenHeight = 0
    
    playerRect = None
    playerPic = None
    playerX = 0
    playerY = 0
    
    def __init__ (self,slots, width=500, height=500):
        self.inventoryarray = []
        self.slots = slots
        
        # set up the screen dimensions
        self.screenWidth = width
        self.screenHeight = height
        self.picWidth = self.screenWidth/2
        self.picHeight = self.screenHeight * 4/5
        
        #create the images
        tempPic = pygame.image.load('assets/mcgui/container/inventoryEdit.png')
        self.inventoryPic = pygame.transform.scale(tempPic, (self.picWidth, self.picHeight))
        self.inventoryRect = self.inventoryPic.get_rect()
        self.inventoryRect.x = (width - self.picWidth)/2
        self.inventoryRect.y = (height - self.picHeight)/2
        
        #create the area to draw the player
        self.playerRect = pygame.Rect(self.inventoryRect.width/7 + self.inventoryRect.x, self.inventoryRect.height/33 + self.inventoryRect.y, (self.inventoryRect.width*80/175)-(self.inventoryRect.width/7), 
                                      (self.inventoryRect.height*78/165)-(self.inventoryRect.height/33))
        
        #set up the slots
        for n in range(0,slots):
            self.inventoryarray.append([0,0])
            
    def draw(self, screen):        
        screen.blit(self.inventoryPic, (self.inventoryRect.x, self.inventoryRect.y))
        if not self.playerPic == None:         
            screen.blit(self.playerPic, (self.playerX, self.playerY))
            
    def newSlotItem (self,slot,item,amount):
        self.inventoryarray[slot] = [item, amount]
        
    def addSlotItem (self,slot,amount):
        self.inventoryarray[slot][1] += amount
        
    def removeSlotItem (self,slot):
        self.inventoryarray[slot] == [0,0]
        
    # set the picture to display of the player
    def setPlayerPic(self, picture):
        newWidth = picture.get_rect().width
        newHeight = picture.get_rect().height
        if picture.get_rect().width > self.playerRect.width:
            newWidth = self.playerRect.width
        if picture.get_rect().height > self.playerRect.height:
            newHeight = self.playerRect.height
        self.playerPic = pygame.transform.scale(picture, (newWidth, newHeight))
        self.playerX = self.playerRect.x + ((self.playerRect.width-newWidth)/2)
        self.playerY = self.playerRect.y + ((self.playerRect.height-newHeight)/2)
        print(self.playerX)
        print(self.playerY)
        