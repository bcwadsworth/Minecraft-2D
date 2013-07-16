import random
from Renderers.Block import BlocksManager

class BlockTerrainControl:
    
    name = None
    seed = None
    blocksManager = None
    chunks = None
    chunkDimensions = None
    
    def __init__(self, pygame, name, seed):
        self.name = name
        self.seed = seed
        self.blocksManager = BlocksManager(pygame)
        self.chunkDimensions = (16, 256)
        
        amtchunks = 10 #Temporary, don't change
        self.chunks = [None] * amtchunks
        for i in range(amtchunks):
            self.chunks[i] = BlockChunkControl(self.seed, ((i * self.chunkDimensions[0]),0), self.blocksManager, self)      
        
    def getChunks(self):
        return self.chunks
    
    def getChunkDimensions(self):
        return self.chunkDimensions
    
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
        rand.seed(seed)
        for i in range(len(blocks)):
            x = i%self.dimensions[0]
            y = self.dimensions[1] - ((i)/self.dimensions[0])
            if(y > 64):
                blocks[i] = blocksManager.getBlockById(0)
            if(y == 64):
                blocks[i] = blocksManager.getBlockById(2)
            if(y < 64 and y >= 56):
                blocks[i] = blocksManager.getBlockById(3)
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