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
            self.chunks[i] = BlockChunkControl(self.seed, ((i * self.chunkDimensions[0]),0), self.blocksManager, self)      
        
    def getChunks(self):
        return self.chunks
    
    def getChunkDimensions(self):
        return self.chunkDimensions
    
    def getBlockDimensions(self):
        return self.blocksManager.getBlockDimensions()
    
    def convertToX(self, convert):
        return convert%self.chunkDimensions[0]
    
    def convertToY(self, convert):
        return self.chunkDimensions[1] - ((convert/self.chunkDimensions[0]))
    
    def convertToCoords(self, tile):
        return (self.convertToX(tile),self.convertToY(tile))
    
    def convertFromCoords(self, coord):
        x = self.chunkDimensions[0] - coord[0]
        y = self.chunkDimensions[1] * coord[1]
        return y-x
    
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
        print "Adding Chunk West"
        self.amtchunks += 1
        newchunks = [None]
        newchunks[0] = BlockChunkControl(self.seed, ((self.chunks[0].getPosition()[0] - self.chunkDimensions[0]),0), self.blocksManager, self)
        newchunks += self.chunks
        self.chunks = newchunks
    
    def addChunkEast(self):
        print "Adding Chunk East"
        self.amtchunks += 1
        newchunks = [None]
        newchunks[0] = BlockChunkControl(self.seed, ((self.chunks[-1].getPosition()[0] + self.chunkDimensions[0]),0), self.blocksManager, self)
        newchunks = self.chunks + newchunks
        self.chunks = newchunks
        
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
    
    def __init__(self, seed, position, blocksManager, terrainControl):
        self.seed = seed
        self.position = position
        self.blocksManager = blocksManager
        self.dimensions = terrainControl.getChunkDimensions()
        blocks = [None] * (self.dimensions[0]*self.dimensions[1])
        
        assert isinstance(blocksManager, BlocksManager)
        
        #GENERATION
        rand = random.Random()
        rand.seed(seed+self.position[0]/16)
        for i in range(len(blocks)):
            x = i%self.dimensions[0]
            y = self.dimensions[1] - ((i)/self.dimensions[0])
            if(y > 64):
                blocks[i] = blocksManager.getBlockById(0)
            if(y == 64):
                blocks[i] = blocksManager.getBlockById(2)
            if(y < 64 and y >= 56):
                blocks[i] = blocksManager.getBlockById(rand.randint(1, 7))
            if(y < 56):
                blocks[i] = blocksManager.getBlockById(1)
                
        self.blocks = blocks
        
    def getBlocks(self):
        return self.blocks
    
    def getDimensions(self):
        return self.dimensions
    
    def getPosition(self):
        return self.position
    
    def convertToX(self, convert):
        return convert%self.dimensions[0]
    
    def convertToY(self, convert):
        return self.dimensions[1] - ((convert/self.dimensions[0]))
    
    def convertToCoords(self, tile):
        return (self.convertToX(tile),self.convertToY(tile))
    
    def convertFromCoords(self, coord):
        x = self.dimensions[0] - coord[0]
        y = self.dimensions[1] * coord[1]
        return y-x