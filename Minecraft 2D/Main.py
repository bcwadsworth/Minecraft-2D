import pygame, sys, os, gametime, imput
from Generators.BlockControl import *
from Renderers.Entity import *
from Renderers.Block import *
from blockmanagers.Inventory import *
from blockmanagers.Crafting import *

#As part of a required Enrichment Center protocol,
#the previous statement that we would not monitor
#the test area was a complete fabrication.
#We will stop enhancing the truth in three. two. *zzzt*
 
resolution = width, height = 850, 550
location = winx, winy = (width/2, height/2)
flags = pygame.NOFRAME|pygame.FULLSCREEN
imput = imput.imputhandler

display = pygame.display
screen = None
clock = pygame.time.Clock()
fps = 60

<<<<<<< HEAD
menu = True
mainMenu = None

color = (125,206,250)
=======
>>>>>>> refs/remotes/origin/master
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
<<<<<<< HEAD
    screen.fill(color)
    
    if menu:
        mainMenu.draw()
    else:
        world.draw(screen, offset, resolution)    
=======
    time.tick()
    screen.fill(time.color)

    world.draw(screen, offset, resolution)
>>>>>>> refs/remotes/origin/master
            
                # Array Entry = file, position
#    for n in range(0, len(entityMangager.ObjectArray)):
#        screen.blit(entityMangagerObjectArray[n][0], entityMangager.ObjectArray[n][1])
#                 # Array Entry = file, position
#     for n in range(0, len(Menu.ObjectArray)):
#         screen.blit(Menu.ObjectArray[n][0], Menu.ObjectArray[n][1])
                # Array Entry = file, position
                
    display.flip()

<<<<<<< HEAD
#gets the key pressed events [for during the game?]
def keyCheck():
    global menu
    
=======
def gameinput():
>>>>>>> refs/remotes/origin/master
    global offset
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
    
