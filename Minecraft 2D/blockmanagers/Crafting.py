'''
Created on Jul 16, 2013

@author: python09
'''

class CraftingManager:
    def startcrafting(self,size):
        self.inventory = []
        for n in range(1,(size**)):
            self.inventory.append([0,0])
    def newslotitem (self,slot,item,amount):
        self.inventory[slot] = [item, amount]
    def addslotitem (self,slot,amount):
        self.inventory[slot][1] += amount
    def removeslotitem (self,slot):
        self.inventory[slot] == [0,0]
        
        