'''
Created on Jul 16, 2013

@author: python09
'''

class timemanager(object):


    def __init__(self,framerate):
        self.framerate = framerate
        self.counter = 0
        self.color = (0,100,200)
        