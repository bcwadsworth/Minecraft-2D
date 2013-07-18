'''
Created on Jul 15, 2013

@author: python09
'''
import pygame

class storeinventory:
    slots = None
    inventoryPic = None
    inventoryRect = None
    picWidth = 0
    picHeight = 0
    screenWidth = 0
    screenHeight = 0
    
    playerRect = None
    
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
        
        '''#create the area to draw the player
        self.playerRect = pygame.Rect(width/7, height/33, (width*7/3)-(width/7), (height*78/165)-(height/33))'''
        
        #set up the slots
        for n in range(0,slots):
            self.inventoryarray.append([0,0])
            
    def draw(self, screen):
        screen.blit(self.inventoryPic, (self.inventoryRect.x, self.inventoryRect.y))
        '''if not self.playerPic == None:
            screen.blit(self.playerPic, (self.playerRect.x + (self.playerRect.width-self.playerPic.get_rect().width)/2, 
                                         self.playerRect.y + (self.playerRect.height-self.playerPic.get_rect().height)/2))'''
            
    def newSlotItem (self,slot,item,amount):
        self.inventoryarray[slot] = [item, amount]
        
    def addSlotItem (self,slot,amount):
        self.inventoryarray[slot][1] += amount
        
    def removeSlotItem (self,slot):
        self.inventoryarray[slot] == [0,0]
        
    '''def setPlayerPic(self, picture):
        temp = picture
        if picture'''
        