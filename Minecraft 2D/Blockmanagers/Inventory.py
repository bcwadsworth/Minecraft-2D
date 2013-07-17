'''
Created on Jul 15, 2013

@author: python09
'''
class storeinventory():
    def __init__ (self,slots):
        self.inventoryarray = []
        self.slots = slots
        for n in range(0,slots):
            self.inventoryarray.append([0,0])
    def newslotitem (self,slot,item,amount):
        self.inventoryarray[slot] = [item, amount]
    def addslotitem (self,slot,amount):
        self.inventoryarray[slot][1] += amount
    def removeslotitem (self,slot):
        self.inventoryarray[slot] == [0,0]
        