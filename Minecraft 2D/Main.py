import pygame, sys, os, time, imput
from Generators.BlockControl import *
from Renderers.Entity import *
from Renderers.Menu import *


resolution = width, height = 850, 550
location = winx, winy = (width/2, height/2)
flags = 0 #pygame.NOFRAME|pygame.FULLSCREEN

display = pygame.display
screen = None
clock = pygame.time.Clock()
fps = 60

color = (125,206,250)
world = BlockTerrainControl(pygame, "World", 0)
offset = [0,0]

playing = False

def main():
    global screen
    
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((pygame.display.Info().current_w/2)-winx, (pygame.display.Info().current_h/2)-winy)
    pygame.display.set_caption('Minecraft 2D')
    screen = display.set_mode((resolution), flags)
    
    playing = True
    spawnPlayer()
    while playing:
        draw()
        keyCheck()
        clock.tick(fps)

def spawnPlayer():
    global offset, playerPos
    chunk = world.getChunks()[0]
    assert isinstance(chunk, BlockChunkControl)
    offset = [0, (chunk.getDimensions()[1]-80)*world.getBlockDimensions()[0]]

def draw():
    screen.fill(color)

    

    for chunk in world.getChunksToRender(offset, width):
        currx = 0
        curry = 0
        for block in chunk.getBlocks():
            if(currx > chunk.getDimensions()[0]-1):
                currx = 0
                curry += 1   
            if(not block.getId() == 0): #Air
                location = (currx * block.getImage().getWidth() - offset[0] + (chunk.getPosition()[0]*16), curry * block.getImage().getHeight() - offset[1]) 
                if(not (location[0] <= 0-(offset[0]/world.getBlockDimensions()[0])-block.getImage().getWidth()) and not (location[0] >= width + abs((offset[0]/world.getBlockDimensions()[0])+world.getBlockDimensions()[0])) and not (location[1] <= 0-(offset[1]/world.getBlockDimensions()[1])-block.getImage().getHeight()) and not (location[1] >= height + abs((offset[1]/world.getBlockDimensions()[1])+world.getBlockDimensions()[1]))):     
                    screen.blit(block.getImage().getSurface(), location)
            currx += 1
            
                # Array Entry = file, position
#     for n in range(0, len(Entity.ObjectArray)):
#         screen.blit(Entity.ObjectArray[n][0], Entity.ObjectArray[n][1])
#                 # Array Entry = file, position
#     for n in range(0, len(Menu.ObjectArray)):
#         screen.blit(Menu.ObjectArray[n][0], Menu.ObjectArray[n][1])
                # Array Entry = file, position
                
    display.flip()

def keyCheck():
    global offset
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
        elif event.type == pygame.QUIT:
            quitGame()
    
    pressed = pygame.key.get_pressed()
    
    if(pressed[pygame.K_w]):
        offset[1] -= world.getBlockDimensions()[0]
    if(pressed[pygame.K_s]):
        offset[1] += world.getBlockDimensions()[0]
    if(pressed[pygame.K_a]):
        offset[0] -= world.getBlockDimensions()[0]
    if(pressed[pygame.K_d]):
        offset[0] += world.getBlockDimensions()[0]

def quitGame():
    global playing
    playing = False
    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()
    
