'''
Created on Jul 16, 2013

@author: python09
'''

class timemanager(object):


    def __init__(self,framerate):
        self.framerate = framerate
        self.counter = 0
        self.color = (0,100,200)
        self.hour = 8
    def tick(self):
        if self.framerate == self.counter:
            self.counter = 0
            self.hour += 0.1
        if self.hour == 24:
            self.hour = 0
        self.counter += 1
        if self.hour == 0:
            self.color = (0,0,10)
        elif self.hour == 1:
            self.color = (0,0,10)
        elif self.hour == 2:
            self.color = (0,0,10)
        elif self.hour == 3:
            self.color = (0,0,25)
        elif self.hour == 4:
            self.color = (0,0,50)
        elif self.hour == 5:
            self.color = (0,0,100)
        elif self.hour == 6:
            self.color = (0,0,150)
        elif self.hour == 7:
            self.color = (0,25,175)
        elif self.hour == 8:
            self.color = (0,75,200)
        elif self.hour == 9:
            self.color = (0,100,200)
        elif self.hour == 10:
            self.color = (0,125,200)
        elif self.hour == 11:
            self.color = (0,150,200)
        elif self.hour == 12:
            self.color = (0,160,200)
        elif self.hour == 13:
            self.color = (0,150,200)
        elif self.hour == 14:
            self.color = (0,140,200)
        elif self.hour == 15:
            self.color = (0,130,200)
        elif self.hour == 16:
            self.color = (0,120,200)
        elif self.hour == 17:
            self.color = (0,100,200)
        elif self.hour == 18:
            self.color = (0,50,200)
        elif self.hour == 19:
            self.color = (0,10,150)
        elif self.hour == 20:
            self.color = (0,0,100)
        elif self.hour == 21:
            self.color = (0,0,50)
        elif self.hour == 22:
            self.color = (0,0,25)
        elif self.hour == 23:
            self.color = (0,0,10)