'''
Created on Jul 15, 2013

@author: python09
'''

'''creeper = 0
spider = 1
skeleton = 2
zombie = 3
pig = 4
cow = 5
sheep = 6
chicken = 7
dog = 8
horse = 9
arrow = 10'''

class entityManager:
    def __init__(self):
        self.creeper = []
        self.spider = []
        self.skeleton = []
        self.zombie = []
        self.pig = []
        self.cow = []
        self.sheep = []
        self.chicken = []
        self.dog = []
        self.horse = []
        self.arrow = []
        self.allentitys = []
    def newentity(self, entityID):
        'sa'
    def killentity(self, entityID, number):
        'as'
    def moveentity(self, entityID, number, x, y):
        'sa'
    def updateentitys(self):
        's'