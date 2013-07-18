import pygame, sys, os, gametime, imput
from Generators.BlockControl import *
from Renderers.Entity import *
from Renderers.Block import *
from Blockmanagers.Inventory import *
from Blockmanagers.Crafting import *
from Renderers.Menu import *

#As part of a required Enrichment Center protocol,
#the previous statement that we would not monitor
#the test area was a complete fabrication.
#We will stop enhancing the truth in three. two. *zzzt*
 
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
time = gametime.timemanager(fps)
offset = [0,0]

playing = False

def main():
    global screen
    global mainMenu
    
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((pygame.display.Info().current_w/2)-winx, (pygame.display.Info().current_h/2)-winy)
    pygame.display.set_caption('Minecraft 2D')
    screen = display.set_mode((resolution), flags)
    mainMenu = Menu(screen, width, height)
    
    # the game play loop
    playing = True
    spawnPlayer()
    while playing:
        draw()
        gameinput()
        clock.tick()

def spawnPlayer():
    global offset, playerPos
    chunk = world.getChunks()[0]
    assert isinstance(chunk, BlockChunkControl)
    playerinventory = storeinventory(36)
    offset = [0, (chunk.getDimensions()[1]-80)*world.getBlockDimensions()[0]]

def draw():
    screen.fill(time.color)
    
    if menu:
        mainMenu.draw()
    else:
        world.draw(screen, offset, resolution)
        
    time.tick()                
    display.flip()

# gets the input for the game
def gameinput():
    global offset
    global menu
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
        elif event.type == pygame.QUIT:
            quitGame()    
        if menu:
            request = mainMenu.getEvents(event)
            if request == 1:
                quitGame()
            elif request == 2:
                menu = False
    
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
    
