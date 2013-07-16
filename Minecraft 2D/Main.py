import pygame, sys, os, time, imput
from Generators.BlockControl import *
from Renderers.Entity import *
from Renderers.Menu import *


resolution = width, height = 850, 550
location = winx, winy = (width/2, height/2)
flags = 0 #pygame.NOFRAME|pygame.FULLSCREEN
imput = imput.imputhandler

display = pygame.display
screen = None
clock = pygame.time.Clock()
fps = 60

menu = True
mainMenu = None

color = (125,206,250)
world = BlockTerrainControl(pygame, "World", 0)
offset = [0,0]

playing = False

def main():
    global screen
    global mainMenu
    
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((pygame.display.Info().current_w/2)-winx, (pygame.display.Info().current_h/2)-winy)
    pygame.display.set_caption('Minecraft 2D')
    screen = display.set_mode((resolution), flags)
    mainMenu = Menu(screen)
    
    # the game play loop
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
    '''
    if menu:
        mainMenu.draw()
    else:
        world.draw(screen, offset, resolution)'''
    world.draw(screen, offset, resolution)
            
                # Array Entry = file, position
#     for n in range(0, len(Entity.ObjectArray)):
#         screen.blit(Entity.ObjectArray[n][0], Entity.ObjectArray[n][1])
#                 # Array Entry = file, position
#     for n in range(0, len(Menu.ObjectArray)):
#         screen.blit(Menu.ObjectArray[n][0], Menu.ObjectArray[n][1])
                # Array Entry = file, position
                
    display.flip()

#gets the key pressed events [for during the game?]
def keyCheck():
    global offset
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
        elif event.type == pygame.QUIT:
            quitGame()
    '''
    if menu:
        if mainMenu.getEvents() == 0:
            quitGame()'''
    
    pressed = pygame.key.get_pressed()
    
    #moves the viewpoint
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
    
