import pygame
import time
#Variabels
arg = 0
arg2 = 0
stex = 0
stey = 100
armx = 0
img = 1
imcr = 1
lmg = 1
lmcr = 1
#Image
arm1 = pygame.image.load("Steve Arm1.png")
arm2 = pygame.image.load("Steve Arm2.png")
arm3 = pygame.image.load("Steve Arm3.png")
arm4 = pygame.image.load("Steve Arm4.png")
arm5 = pygame.image.load("Steve Arm5.png")
arm10 = pygame.image.load("Steve Arm10.png")
arm22 = pygame.image.load("Steve Arm-2.png")
arm23 = pygame.image.load("Steve Arm-3.png")
arm24 = pygame.image.load("Steve Arm-4.png")
arm25 = pygame.image.load("Steve Arm-5.png")
leg1 = pygame.image.load("Steve Leg1.png")
leg2 = pygame.image.load("Steve Leg2.png")
leg3 = pygame.image.load("Steve Leg3.png")
leg4 = pygame.image.load("Steve Leg4.png")
leg5 = pygame.image.load("Steve Leg5.png")
leg22 = pygame.image.load("Steve Leg-2.png")
leg23 = pygame.image.load("Steve Leg-3.png")
leg24 = pygame.image.load("Steve Leg-4.png")
leg25 = pygame.image.load("Steve Leg-5.png")
tor = pygame.image.load("Stevie Torso.png")
torr = pygame.image.load("Stevie Torso2.png")
screen = 0
def setscreen(sc,wi):
    global stex
    global armx
    global screen
    screen = sc
    #Set variables based on screen size
    stex = (wi/2)-8
    armx = stex - 17
#Functions
def position(x,y):
    global stey
    global stex
    stey = y
    stex = x
def step(d,sh):
    global arg
    global arg2
    global img
    global imcr
    global lmg
    global lmcr
    arg = 1
    arg2 = 1
    if d == 1:
        arg = img
        img = img + imcr
        arg2 = lmg
        lmg = lmg + lmcr
    if d == -1:
        arg = img
        img = img + imcr
        arg2 = lmg
        lmg = lmg + lmcr
    leg(arg2)
    walk(arg,sh)
    if img > 3:
        imcr = -1
    if img < -3:
        imcr = 1
    if lmg > 3:
        lmcr = -1
    if lmg < -3:
        lmcr = 1
def leg(lmg):
    if lmg == 0:
        screen.blit(leg1, (stex,stey))
    if lmg == 1:
        screen.blit(leg2, (stex,stey))
        screen.blit(leg22, (stex,stey))
    if lmg == 2:
        screen.blit(leg3, (stex,stey))
        screen.blit(leg23, (stex,stey))
    if lmg == 3:
        screen.blit(leg4, (stex,stey))
        screen.blit(leg24, (stex,stey))
    if lmg == 4:
        screen.blit(leg5, (stex,stey))
        screen.blit(leg25, (stex,stey))
    if lmg == -1:
        screen.blit(leg22, (stex,stey))
        screen.blit(leg2, (stex,stey))
    if lmg == -2:
        screen.blit(leg23, (stex,stey))
        screen.blit(leg3, (stex,stey))
    if lmg == -3:
        screen.blit(leg24, (stex,stey))
        screen.blit(leg4, (stex,stey))
    if lmg == -4:
        screen.blit(leg25, (stex,stey))
        screen.blit(leg5, (stex,stey))
def walk(img,d):
    if d == 1:
        screen.blit(tor,(stex,stey))
    if d == -1:
        screen.blit(torr,(stex,stey))
    if img == 0:
        screen.blit(arm1, (armx,stey-5))
    if img == 1:
        screen.blit(arm2, (armx,stey-5))
    if img == 2:
        screen.blit(arm3,(armx,stey-5))
    if img == 3:
        screen.blit(arm4,(armx+1,stey-5))
    if img == 4:
        screen.blit(arm5,(armx+1,stey-5))
    if img == -1:
        screen.blit(arm22, (armx,stey-5))
    if img == -2:
        screen.blit(arm23,(armx,stey-5))
    if img == -3:
        screen.blit(arm24,(armx-1,stey-5))
    if img == -4:
        screen.blit(arm25,(armx-1,stey-5))
