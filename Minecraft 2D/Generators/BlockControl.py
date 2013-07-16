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
        
        self.amtchunks = 2
        self.chunks = [None] * self.amtchunks
        for i in range(self.amtchunks):
            self.chunks[i] = BlockChunkControl(self.seed, ((i * self.chunkDimensions[0]),0), self.blocksManager, self, i)      
        
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
            if(i > 0):
                self.chunks[i].setPosInArray(i)
    
    def addChunkEast(self):
        self.amtchunks += 1
        newchunks = [None]
        newchunks[0] = BlockChunkControl(self.seed, ((self.chunks[-1].getPosition()[0] + self.chunkDimensions[0]),0), self.blocksManager, self, len(self.chunks))
        newchunks = self.chunks + newchunks
        self.chunks = newchunks
        for i in range(len(self.chunks)):
            if(i < len(self.chunks)):
                self.chunks[i].setPosInArray(i)
        
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

    
    def __init__(self, seed, position, blocksManager, terrainControl, posInArray):
        self.seed = seed+position[0]/16
        self.position = position
        self.blocksManager = blocksManager
        self.terrainControl = terrainControl
        self.dimensions = terrainControl.getChunkDimensions()
        self.posInArray = posInArray
        
        assert isinstance(blocksManager, BlocksManager)
        
        self.generateTerrain()
        
    def generateTerrain(self):
        
        blocks = [None] * (self.dimensions[0]*self.dimensions[1])
        
        rand = random.Random()
        rand.seed(self.seed)
        
        noise = self.generateNoise(rand)
        
        for i in range(len(blocks)):
            x = i%self.dimensions[0]
            y = i/self.dimensions[0]
            print x,y
            if(noise[x] == 256-y-64):
                blocks[i] = self.blocksManager.getBlockById(2)
            elif(noise[x] > 256-y-64):
                blocks[i] = self.blocksManager.getBlockById(3)
            else:
                blocks[i] = self.blocksManager.getBlockById(0)
            if(256-y < 64):
                blocks[i] = self.blocksManager.getBlockById(1)
                
        self.blocks = blocks
                
    def generateNoise(self, rand):
        array = [0] * self.getDimensions()[0]
        
        currNumerator = 16
        amtTimes = 1
        moveFactor = 0.8
        
        while currNumerator > 1:
            lastBlock = 0
            for i in range(amtTimes):
                pass
                
            currNumerator /= 2
            amtTimes = len(array)/currNumerator
            moveFactor -= 0.2
            
        return array
        
    def setPosInArray(self, pos):
        self.posInArray = pos
                
    def getBlocks(self):
        return self.blocks
    
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
            return block - self.getDimensions()[1]
        if(direction == 1): #East
            if((block + 1) % self.getDimensions()[1] > block % self.getDimensions()[1]):
                return block + 1
            else:
                neighborChunk = self.getNeighborChunk(0)
                return neighborChunk.getBlocks()[block - (block % self.getDimensions()[1])]
        if(direction == 2): #South
            return block + self.getDimensions()[1]
        if(direction == 3): #West
            if((block - 1) % self.getDimensions()[1] < block % self.getDimensions()[1]):
                return block - 1
            else:
                neighborChunk = self.getNeighborChunk(0)
                return neighborChunk.getBlocks()[block + (self.getDimensions()[1] - (block % self.getDimensions()[1]))]
        
    def getNeighborChunk(self, direction):
        if(direction == 0): #East
            return self.terrainControl.getChunks()[self.posInArray + 1]
        if(direction == 1): #West
            return self.terrainControl.getChunks()[self.posInArray - 1]
        
        