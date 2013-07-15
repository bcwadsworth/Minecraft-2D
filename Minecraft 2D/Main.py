'''
Created on Jul 15, 2013

@author: python10
'''
import pygame

color = (0,0,0)

def draw():
    screen.fill(color)
    for n in range(0, len(Block.ObjectArray)):
        screen.blit(Block.ObjectArray[n][0], Block.gameObjectArray[n][1])
                # Array Entry = file, position
    for n in range(0, len(Entity.ObjectArray)):
        screen.blit(Entity.ObjectArray[n][0], Entity.gameObjectArray[n][1])
                # Array Entry = file, position
        for n in range(0, len(Entity.ObjectArray)):
        screen.blit(Entity.ObjectArray[n][0], Entity.gameObjectArray[n][1])
                # Array Entry = file, position
        pygame.display.flip()

if __name__ == '__main__':
    pygame.display.set_caption('Minecraft 2D')
    screen = pygame.display.set_mode((0,0), pygame.NOFRAME|pygame.FULLSCREEN)