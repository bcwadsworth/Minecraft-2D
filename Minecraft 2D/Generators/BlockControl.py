import random
from Renderers.Block import BlocksManager

class BlockTerrainControl:
    
    name = None
    seed = None
    blocksManager = None
    chunks = None
    chunkDimensions = None
    amtchunks = None
    
    def __init__(self, pygame, name, seed):
        self.name = name
        self.seed = seed
        self.blocksManager = BlocksManager(pygame)
        self.chunkDimensions = (16, 256)
        
        self.amtchunks = 1
        self.chunks = [None] * self.amtchunks
        for i in range(len(self.chunks)):
            self.chunks[i] = BlockChunkControl(self.seed, ((i * self.chunkDimensions[0]),0), self.blocksManager, self, i)      
            self.chunks[i].generateTerrain()
        
    def getChunks(self):
        return self.chunks
    
    def getChunkDimensions(self):
        return self.chunkDimensions
    
    def getBlockDimensions(self):
        return self.blocksManager.getBlockDimensions()
    
    def convertToX(self, convert):
        return convert%self.chunkDimensions[0]
    
    def convertToY(self, convert):
        return convert/self.chunkDimensions[1]
    
    def convertToCoords(self, tile):
        return (self.convertToX(tile),self.convertToY(tile))
    
    def convertFromCoords(self, coord):
        x = self.chunkDimensions[0] - coord[0]
        y = self.chunkDimensions[0] * coord[1]
        return y+x
    
    def getChunksToRender(self, offset, width):
        
        startingChunk = -1
        
        for i in range(len(self.getChunks())-1):
            if(offset[0] >= self.getChunks()[i].getPosition()[0]*16 and offset[0] < self.getChunks()[i+1].getPosition()[0]*16):
                startingChunk = i

        if(startingChunk < 0):
            self.addChunkWest()
            startingChunk = 0
        
        endingChunk = -1
        
        for i in range(len(self.getChunks())-1):
            if(width + offset[0] >= self.getChunks()[i].getPosition()[0]*16 and width + offset[0] < self.getChunks()[i+1].getPosition()[0]*16):
                endingChunk = i
        
        if(endingChunk < 0):
            self.addChunkEast()
            endingChunk = len(self.getChunks())-1
            
        return self.getChunks()[startingChunk:endingChunk+1]
    
    def addChunkWest(self):
        self.amtchunks += 1
        newchunks = [None]
        newchunks[0] = BlockChunkControl(self.seed, ((self.chunks[0].getPosition()[0] - self.chunkDimensions[0]),0), self.blocksManager, self, 0)
        newchunks += self.chunks
        self.chunks = newchunks
        for i in range(len(self.chunks)):
            self.chunks[i].setPosInArray(i)
        self.chunks[0].generateTerrain()
    
    def addChunkEast(self):
        self.amtchunks += 1
        newchunks = [None]
        newchunks[0] = BlockChunkControl(self.seed, ((self.chunks[-1].getPosition()[0] + self.chunkDimensions[0]),0), self.blocksManager, self, len(self.chunks))
        newchunks = self.chunks + newchunks
        self.chunks = newchunks
        for i in range(len(self.chunks)):
            self.chunks[i].setPosInArray(i)
        self.chunks[-1].generateTerrain()
        
    def draw(self, screen, offset, resolution):
        width = resolution[0]
        height = resolution[1]
        
        for chunk in self.getChunksToRender(offset, width):
            currx = 0
            curry = 0
            for block in chunk.getBlocks():
                
                if(currx > chunk.getDimensions()[0]-1):
                    currx = 0
                    curry += 1   
                    
                if(not block.getId() == 0): #Air
                    location = (currx * block.getImage().getWidth() - offset[0] + (chunk.getPosition()[0]*16), curry * block.getImage().getHeight() - offset[1]) 
                    if(not (location[0] <= 0-abs(offset[0]/self.getBlockDimensions()[0])-block.getImage().getWidth()) 
                       and not (location[0] >= width + abs((offset[0]/self.getBlockDimensions()[0])+self.getBlockDimensions()[0])) 
                       and not (location[1] <= 0-abs(offset[1]/self.getBlockDimensions()[1])-block.getImage().getHeight()) 
                       and not (location[1] >= height + abs((offset[1]/self.getBlockDimensions()[1])+self.getBlockDimensions()[1]))):     
                        screen.blit(block.getImage().getSurface(), location)
                        
                currx += 1
    
class BlockChunkControl:
    
    seed = None
    position = None
    blocksManager = None
    blocks = None
    dimensions = None
    terrainControl = None
    posInArray = None
    noise = None

    
    def __init__(self, seed, position, blocksManager, terrainControl, posInArray):
        self.seed = seed+position[0]/16
        self.position = position
        self.blocksManager = blocksManager
        self.terrainControl = terrainControl
        self.dimensions = terrainControl.getChunkDimensions()
        self.posInArray = posInArray
        
        assert isinstance(blocksManager, BlocksManager)
        
    def generateTerrain(self):
        
        self.blocks = [None] * (self.dimensions[0]*self.dimensions[1])
        
        rand = random.Random()
        rand.seed(self.seed)
        
        #---------------NOISE---------------
        
        self.generateNoise (rand,1)
        noisea = self.noisea
        
        rand = random.Random()
        rand.seed(self.seed + 5)
        self.generateNoise (rand,2)
        noiseb = self.noiseb

        for i in range(len(self.blocks)):
            x = i%self.dimensions[0]
            y = i/self.dimensions[0]
            if(noiseb[x] >= self.getDimensions()[1]-y-56):
                if random.randrange(1,11) == 1 and y > 256-11:
                        self.blocks[i] = self.blocksManager.getBlockById(12)
                elif random.randrange(1,151) == 1 and y > 256-16:
                    self.blocks[i] = self.blocksManager.getBlockById(18)
                elif random.randrange(1,151) == 1 and y > 256-16:
                    self.blocks[i] = self.blocksManager.getBlockById(17)
                elif random.randrange(1,176) == 1 and y > 256-16:
                    self.blocks[i] = self.blocksManager.getBlockById(19)
                elif random.randrange(1,201) == 1 and y > 256-26:
                    self.blocks[i] = self.blocksManager.getBlockById(14)
                elif random.randrange(1,151) == 1 and y > 256-26:
                    self.blocks[i] = self.blocksManager.getBlockById(20)
                elif random.randrange(1,76) == 1:
                    if y > 256-26 and random.randrange(1, 11) == 1:
                        self.blocks[i] = self.blocksManager.getBlockById(15)
                    else:
                        self.blocks[i] = self.blocksManager.getBlockById(15)
                elif random.randrange(1,51) == 1:
                    if y > 256-26 and random.randrange(1, 16) == 1:
                        self.blocks[i] = self.blocksManager.getBlockById(16)
                    else:
                        self.blocks[i] = self.blocksManager.getBlockById(16)
                else:
                    self.blocks[i] = self.blocksManager.getBlockById(1)
            elif(noisea[x] == self.getDimensions()[1]-y-64):
                self.blocks[i] = self.blocksManager.getBlockById(2)
            elif(noisea[x] > self.getDimensions()[1]-y-64 and noiseb[x] < 256-y-56):
                self.blocks[i] = self.blocksManager.getBlockById(3)
            elif(noiseb[x] < self.getDimensions()[1]-y-2):
                self.blocks[i] = self.blocksManager.getBlockById(0)
            if(y == self.dimensions[1]-2):
                r = rand.randint(0,10)
                if(r > 3):
                    self.blocks[i] = self.blocksManager.getBlockById(7)
            if(y == self.dimensions[1]-1):
                self.blocks[i] = self.blocksManager.getBlockById(7)
                
        #--------------------DIGGERS (MINE GENERATION)----------------
        
        digArray = []
        digArray += Digger((self.getBlocks()[self.convertFromCoords((self.getDimensions()[0]/2,self.getDimensions()[1]-1-32))], self, self.convertFromCoords((self.getDimensions()[0]/2,self.getDimensions()[1]-1-32))), rand, digArray, 0),
        
        someoneIsAlive = True
        
        while(someoneIsAlive):
            someoneIsAlive = False
            for i in range(len(digArray)):
                if(digArray[i].isActive()):
                    someoneIsAlive = True
                    digArray[i].dig()
                            
                
        #--------------------SMOOTHING----------------------
                
        for i in range(len(self.blocks)):
            x = i%self.dimensions[0]
            y = i/self.dimensions[0]
            if(self.blocks[i].getId() == 2): #Grass
                if(not self.getNeighborBlock(i, 1) == None and not self.getNeighborBlock(i, 3) == None):
                    eastAir = False
                    westAir = False
                    if(self.getNeighborBlock(i, 1)[1] == 1):
                        if(self.getNeighborChunk(0).getBlocks()[self.getNeighborBlock(i, 1)[0]].getId() == 0):
                            eastAir = True
                    else:
                        if(self.blocks[self.getNeighborBlock(i, 1)[0]].getId() == 0):
                            eastAir = True
                        
                    if(self.getNeighborBlock(i, 3)[1] == 1):
                        if(self.getNeighborChunk(1).getBlocks()[self.getNeighborBlock(i, 3)[0]].getId() == 0):
                            westAir = True
                    else:
                        if(self.blocks[self.getNeighborBlock(i, 3)[0]].getId() == 0):
                            westAir = True
                    if(eastAir == True and westAir == True):
                        self.blocks[i] = self.blocksManager.getBlockById(0)
                        self.blocks[self.getNeighborBlock(i, 2)[0]] = self.blocksManager.getBlockById(2)
                
    def generateNoise(self, rand, id):
        array = [0] * self.getDimensions()[0]
        direction = 0
        inOtherChunk = False
        prob = 75
        
        if(self.getNeighborChunk(1) == None and self.getNeighborChunk(0) == None): #None
            direction = 1
        elif(self.getNeighborChunk(1) == None and not self.getNeighborChunk(0) == None): #West
            direction = -1
            inOtherChunk = True
        elif(self.getNeighborChunk(0) == None and not self.getNeighborChunk(1) == None): #East
            direction = 1
            inOtherChunk = True
        
        for i in range(len(array)):
            if(direction == 1):
                if(inOtherChunk and i == 0):
                    if(self.getNeighborChunk(1).getNoise(id)[-2] < self.getNeighborChunk(1).getNoise(id)[-1]):
                        #Going up
                        array[i] = self.getNeighborChunk(1).getNoise(id)[-1]+rand.randint(-2, 1)
                    elif(self.getNeighborChunk(1).getNoise(id)[-2] > self.getNeighborChunk(1).getNoise(id)[-1]):
                        #Going down
                        array[i] = self.getNeighborChunk(1).getNoise(id)[-1]+rand.randint(-1, 2)
                    elif(self.getNeighborChunk(1).getNoise(id)[-2] == self.getNeighborChunk(1).getNoise(id)[-1]):
                        #Flat
                        array[i] = self.getNeighborChunk(1).getNoise(id)[-1]+rand.randint(-1, 1)
                elif(inOtherChunk and i == 1):
                    if(self.getNeighborChunk(1).getNoise(id)[-1] < array[0]):
                        #Going up
                        array[i] = array[0]+rand.randint(-2, 1)
                    elif(self.getNeighborChunk(1).getNoise(id)[-1] > array[0]):
                        #Going down
                        array[i] = array[0]+rand.randint(-1, 2)
                    elif(self.getNeighborChunk(1).getNoise(id)[-1] == array[0]):
                        #Flat
                        array[i] = array[0]+rand.randint(-1, 1)
                else:
                    if(array[i-2] < array[i-1]):
                        #Going up
                        array[i] = array[i-1]+rand.randint(-2, 1)
                    elif(array[i-2] > array[i-1]):
                        #Going down
                        array[i] = array[i-1]+rand.randint(-1, 2)
                    elif(array[i-2] == array[i-1]):
                        #Flat
                        array[i] = array[i-1]+rand.randint(-1, 1)
            else:
                if(inOtherChunk and i == 0):
                    if(self.getNeighborChunk(0).getNoise(id)[1] < self.getNeighborChunk(0).getNoise(id)[0]):
                        #Going up
                        array[-1-i] = self.getNeighborChunk(0).getNoise(id)[0]+rand.randint(-2, 1)
                    elif(self.getNeighborChunk(0).getNoise(id)[1] > self.getNeighborChunk(0).getNoise(id)[0]):
                        #Going down
                        array[-1-i] = self.getNeighborChunk(0).getNoise(id)[0]+rand.randint(-1, 2)
                    elif(self.getNeighborChunk(0).getNoise(id)[1] == self.getNeighborChunk(0).getNoise(id)[0]):
                        #Flat
                        array[-1-i] = self.getNeighborChunk(0).getNoise(id)[0]+rand.randint(-1, 1)
                elif(inOtherChunk and i == 1):
                    if(self.getNeighborChunk(0).getNoise(id)[0] < array[-1-0]):
                        #Going up
                        array[-1-i] = array[-1]+rand.randint(-2, 1)
                    elif(self.getNeighborChunk(0).getNoise(id)[0] > array[-1-0]):
                        #Going down
                        array[-1-i] = array[-1]+rand.randint(-1, 2)
                    elif(self.getNeighborChunk(0).getNoise(id)[0] == array[-1-0]):
                        #Flat
                        array[-1-i] = array[-1]+rand.randint(-1, 1)
                else:
                    if(array[-1-i+2] < array[-1-i+1]):
                        #Going up
                        array[-1-i] = array[-1-i+1]+rand.randint(-2, 1)
                    elif(array[-1-i+2] > array[-1-i+1]):
                        #Going down
                        array[-1-i] = array[-1-i+1]+rand.randint(-1, 2)
                    elif(array[-1-i+2] == array[-1-i+1]):
                        #Flat
                        array[-1-i] = array[-1-i+1]+rand.randint(-1, 1)
        if id == 1:
            self.noisea = array
        elif id == 2:
            self.noiseb = array

    def getNoise(self, id):
        if id == 1:
            return self.noisea
        elif id == 2:
            return self.noiseb
        
    def setPosInArray(self, pos):
        self.posInArray = pos
                
    def getBlocks(self):
        return self.blocks
    
    def getAbsBlock(self, blockArray):
        if(blockArray[1] == 1): #In another chunk
            if(blockArray[2] == 1): #East direction
                return self.getNeighborChunk(0).getBlocks()[blockArray[0]], self.getNeighborChunk(0), blockArray[0]
            elif(blockArray[2] == 3): #West direction
                return self.getNeighborChunk(1).getBlocks()[blockArray[0]], self.getNeighborChunk(1), blockArray[0]
        elif(blockArray[1] == 0): #In same chunk
            return self.getBlocks()[blockArray[0]], self, blockArray[0]
    
    def getDimensions(self):
        return self.dimensions
    
    def getPosition(self):
        return self.position
    
    def convertToX(self, convert):
        return convert%self.dimensions[0]
    
    def convertToY(self, convert):
        return convert/self.dimensions[0]
    
    def convertToCoords(self, tile):
        return (self.convertToX(tile),self.convertToY(tile))
    
    def convertFromCoords(self, coord):
        x = self.dimensions[0] - coord[0]
        y = self.dimensions[0] * coord[1]
        return y+x
    
    def getNeighborBlock(self, block, direction):
        if(direction == 0): #North
            if (block - self.getDimensions()[0]) < (self.getDimensions()[0]*self.getDimensions()[1])-1:
                return None
            return block - self.getDimensions()[0], 0, direction
        if(direction == 1): #East
            if((block + 1) % self.getDimensions()[1] > block % self.getDimensions()[1]):
                return block + 1, 0, direction
            else:
                neighborChunk = self.getNeighborChunk(0)
                if(not neighborChunk == None):
                    return block - (block % self.getDimensions()[1]), 1, direction
                else:
                    return None
        if(direction == 2): #South
            if (block + self.getDimensions()[0]) > (self.getDimensions()[0]*self.getDimensions()[1])-1:
                return None
            return block + self.getDimensions()[0], 0, direction
        if(direction == 3): #West
            if((block - 1) % self.getDimensions()[1] < block % self.getDimensions()[1]):
                return block - 1, 0, direction
            else:
                neighborChunk = self.getNeighborChunk(1)
                if(not neighborChunk == None):
                    return block + (self.getDimensions()[0] - (block % self.getDimensions()[0])), 1, direction
                else:
                    return None
                    
    def getNeighborChunk(self, direction):
        if(direction == 0): #East
            if(self.posInArray + 1 > len(self.terrainControl.getChunks())-1):
                return None
            else:
                return self.terrainControl.getChunks()[self.posInArray + 1]
        if(direction == 1): #West
            if(self.posInArray - 1 < 0):
                return None
            else:
                return self.terrainControl.getChunks()[self.posInArray - 1]
        
    def getBlockManager(self):
        return self.blocksManager
        
class Digger:
    
    block = None
    active = None
    rand = None
    digArray = None
    did = None
    
    def __init__(self, block, rand, array, did):
        self.block = block
        self.active = True
        self.rand = rand
        self.digArray = array
        self.did = did
    
    def getId(self):
        return self.did
    
    def dig(self):
        chunk = self.block[1]
        assert isinstance(chunk, BlockChunkControl)
        available = []
        chosen = None
        
        print chunk.convertToCoords(self.block[2])
        
        if(not chunk.getNeighborBlock(self.block[2], 0) == None):
            if(not chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], 0))[0].getId() == 0):
                available += chunk.getNeighborBlock(self.block[2], 0),
        if(not chunk.getNeighborBlock(self.block[2], 1) == None):
            if(not chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], 1))[0].getId() == 0):
                available += chunk.getNeighborBlock(self.block[2], 1),
        if(not chunk.getNeighborBlock(self.block[2], 2) == None):
            if(not chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], 2))[0].getId() == 0):
                available += chunk.getNeighborBlock(self.block[2], 2),
        if(not chunk.getNeighborBlock(self.block[2], 3) == None):
            print chunk.getNeighborBlock(self.block[2], 3), self.block[2]
            if(not chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], 3))[0].getId() == 0):
                available += chunk.getNeighborBlock(self.block[2], 3),
            
        if(len(available) > 0):
            chosen = available[self.rand.randint(0, len(available)-1)]
        else:
#             someoneIsAlive = False
#             for i in self.digArray:
#                 if(i.isActive() and not i.getId() == self.did):
#                     someoneIsAlive = True
#                     print "Someone is alive!"
            self.active = False
            return
#             if(someoneIsAlive):
#                 self.active = False
#                 return
#             else:
#                 print "Nobody is alive. Searching.."
#                 while(len(available) == 0):
#                     print "Still 0..."
#                     
#                     for i in range(4):
#                         if(not chunk.getNeighborBlock(self.block[2], i) == None):
#                             print "Current location: "+str(chunk.convertToCoords(self.block[2]))
#                             if(not chunk.getNeighborBlock(self.block[2], i) == None):
#                                 if(not chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], i))[0].getId() == 0):
#                                     available += chunk.getNeighborBlock(self.block[2], i),
#                                 
#                     r = self.rand.randint(0,3)
#                     print r
#                     while(chunk.getNeighborBlock(self.block[2], r) == None):
#                         r = self.rand.randint(0,3)
#                     self.block = chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], r))
#                 print "Done searching. Validating..."
#                 while(chunk.getNeighborBlock(self.block[2], r) == None):
#                     r = self.rand.randint(0,3)
#                 self.block = chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], r))
#                 chosen = available[self.rand.randint(0, len(available)-1)]
#                 print "Validated"
        
        availableS = []
        
        spawn = self.rand.randint(1, 100)
        if(spawn <= 8):
            if(not chunk.getNeighborBlock(self.block[2], 0) == None):
                if(chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], 0))[0].getId() == 0):
                    availableS += chunk.getNeighborBlock(self.block[2], 0),
            if(not chunk.getNeighborBlock(self.block[2], 1) == None):
                if(chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], 1))[0].getId() == 0):
                    availableS += chunk.getNeighborBlock(self.block[2], 1),
            if(not chunk.getNeighborBlock(self.block[2], 2) == None):
                if(chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], 2))[0].getId() == 0):
                    availableS += chunk.getNeighborBlock(self.block[2], 2),
            if(not chunk.getNeighborBlock(self.block[2], 3) == None):
                if(chunk.getAbsBlock(chunk.getNeighborBlock(self.block[2], 3))[0].getId() == 0):
                    availableS += chunk.getNeighborBlock(self.block[2], 3),
                
        if(len(availableS) > 0):
            spawnDig = availableS[self.rand.randint(0, len(availableS)-1)]
            self.digArray += Digger(chunk.getAbsBlock(spawnDig), self.rand, self.digArray, len(self.digArray)),
               
        self.block = chunk.getAbsBlock(chosen)
        otherChunk = chunk.getAbsBlock(chosen)[1]
        otherChunk.getBlocks()[chunk.getAbsBlock(chosen)[2]-1] = chunk.getBlockManager().getBlockById(0)
            
    def isActive(self):
        return self.active
            
