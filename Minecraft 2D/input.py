'''
Created on Jul 16, 2013

@author: python09
'''
import pygame
import sys
class inputhandler:
    def __init__(self):
        self.moveDir = 0
        self.invDir = 0
        self.jump = False
        self.crouch = False
        self.inv = False
        self.drop = False
        self.menu = False
        self.mouseclickright = False
        self.mouseclickleft = False
        self.mousepos = (0,0)
    def input(self):
        self.moveDir = 0
        self.invDir = 0
        self.jump = False
        self.crouch = False
        self.inv = False
        self.drop = False
        self.menu = False
        self.mouseclickright = False
        self.mouseclickleft = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.jump = True
                if event.key == pygame.K_ESCAPE:
                    self.menu = True
                if event.key == pygame.K_q:
                    self.drop = True
                if event.key == pygame.K_e:
                    self.inv = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEMOTION:
                self.mousepos = event.pos
        self.pressed = pygame.key.get_pressed()
        if(self.pressed[pygame.K_a]):
            self.moveDir = -1
        elif(self.pressed[pygame.K_d]):
            self.moveDir = 1
        if not self.jump == True and (self.pressed[pygame.K_d]):
            self.crouch = True
        if(self.pressed[pygame.K_d]):
            self.crouch = True
        if(self.pressed[pygame.K_z]):#inv dir- if possible mouse wheel?
            self.invDir = -1
        elif(self.pressed[pygame.K_c]):
            self.invDir = 1
