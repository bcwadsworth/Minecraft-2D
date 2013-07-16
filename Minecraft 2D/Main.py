import pygame, sys, os
from Generators.BlockControl import *
from Renderers.Entity import *
from Renderers.Menu import *

resolution = width, height = 850, 550
location = winx, winy = (width/2, height/2)
flags = 0 #pygame.NOFRAME|pygame.FULLSCREEN

display = pygame.display
screen = None
clock = pygame.time.Clock()
fps = 120

color = (0,0,0)
world = BlockTerrainControl(pygame, "World", 0)
offset = [0, (128*16)]

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
    global offset
    chunk = world.getChunks()[0]
    assert isinstance(chunk, BlockChunkControl)
    offset = [-((width/2/16)*16 - ((chunk.getDimensions()[0]/2) * 16)), (chunk.getDimensions()[1]-80)*16]

def draw():
    screen.fill(color)
    currx = 0
    curry = 0
    for chunk in world.getChunks():
        for block in chunk.getBlocks():
            if(currx > chunk.getDimensions()[0]-1):
                currx = 0
                curry += 1   
            if(block.getId() == 0): #Air
                pass
            else:
                location = (currx*block.getImage().getWidth() - offset[0], curry*block.getImage().getHeight() - offset[1]) 
                if((location[0] <= 0-offset[0]-block.getImage().getWidth()) or (location[0] >= width+abs(offset[0])) or (location[1] <= 0-offset[1]-block.getImage().getHeight()) or (location[1] >= height+abs(offset[1]))):
                    pass
                else:     
                    screen.blit(block.getImage().getSurface(), location)
            currx += 1
                # Array Entry = file, position
#     for n in range(0, len(Entity.ObjectArray)):
#         screen.blit(Entity.ObjectArray[n][0], Entity.ObjectArray[n][1])
#                 # Array Entry = file, position
#     for n in range(0, len(Menu.ObjectArray)):
#         screen.blit(Menu.ObjectArray[n][0], Menu.ObjectArray[n][1])
                # Array Entry = file, position
        pygame.display.flip()

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
        offset[1] -= 16
    if(pressed[pygame.K_s]):
        offset[1] += 16
    if(pressed[pygame.K_a]):
        offset[0] -= 16
    if(pressed[pygame.K_d]):
        offset[0] += 16

def quitGame():
    global playing
    playing = False
    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()
    