import pygame, sys, os, gametime, input
from Generators.BlockControl import *
from Renderers.Entity import *
from Renderers.Block import *
from Blockmanagers.Inventory import *
from Blockmanagers.Crafting import *
from Renderers.Menu import *
from Blockmanagers.steven import *


#As part of a required Enrichment Center protocol,
#the previous statement that we would not monitor
#the test area was a complete fabrication.
#We will stop enhancing the truth in three. two. *zzzt*

 
resolution = width, height = 850, 550
location = winx, winy = (width/2, height/2)
flags = 0 #pygame.NOFRAME|pygame.FULLSCREEN
gameinput = input.inputhandler()


display = pygame.display
screen = None
clock = pygame.time.Clock()
fps = 60

menu = True
showInventory = False # whether to show the inventory or not
mainMenu = None

world = BlockTerrainControl(pygame, "World", 0)
time = gametime.timemanager(fps)
offset = [0,0]

playerInventory = None
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
        gameInput()
        draw()
        clock.tick()
        
       

def spawnPlayer():
    global offset, playerPos, playerInventory
    
    chunk = world.getChunks()[0]
    assert isinstance(chunk, BlockChunkControl)
    playerInventory = storeinventory(36, width, height)
    offset = [0, (chunk.getDimensions()[1]-80)*world.getBlockDimensions()[0]]
    setscreen(screen, width)
    

def draw():
    screen.fill(time.color)
    
    if menu:
        mainMenu.draw()
    else:
        world.draw(screen, offset, resolution)
        if showInventory:
            playerInventory.draw(screen)
        
    position(250,250)
    step(0,0)
    setscreen(screen, width)    
    
    time.tick()                
    display.flip()
    

# gets the input for the game
def gameInput():
    global offset
    global menu
    global showInventory
    menuReturn = 0
    gameinput.input()
    if gameinput.quit:
        quitGame()
    if gameinput.menu:
        menu = True
    if gameinput.mouseclick:
        menuReturn = mainMenu.getReturns(gameinput.mousepos)
    if menuReturn == 1:
        quitGame()
    elif menuReturn == 2:
        menu = False
    elif menuReturn == 3:
        pass
    elif gameinput.inv:
        if showInventory:
            showInventory = False
        else:
            showInventory = True
    vdir = 0

    #moves the viewpoint
    offset[0] += gameinput.moveDir * world.getBlockDimensions()[0]
    if gameinput.jump:
        vdir = -1
    elif gameinput.crouch:
        vdir = 1
    offset[1] += vdir * world.getBlockDimensions()[0]
    
    
def quitGame():
    global playing
    playing = False
    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()
    
