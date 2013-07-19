'''
Created on Jul 16, 2013

@author: python09
'''

class CraftingManager:
    
    recipes = []
    
    def __init__(self):
        # put recipes here
        pass
    
    def startCrafting(self,size):
        self.inventory = []
        for n in range(1,(size**2)):
            self.inventory.append([0,0])
            
    def newSlotItem (self,slot,item,amount):
        self.inventory[slot] = [item, amount]
        
    def addSlotItem (self,slot,amount):
        self.inventory[slot][1] += amount
        
    def removeSlotItem (self,slot):
        self.inventory[slot] == [0,0]
        
    def getRecipe(self, index):
        return self.recipes[index]
    
    
        