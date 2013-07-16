import random
from Renderers.Block import BlocksManager

class BlockTerrainControl:
    
    name = None
    seed = None
    blocksManager = None
    chunks = None
    
    def __init__(self, pygame, name, seed):
        self.name = name
        self.seed = seed
        self.blocksManager = BlocksManager(pygame)
        self.chunks = BlockChunkControl(self.seed, (0,0), self.blocksManager),
        
    def getChunks(self):
        return self.chunks
    
class BlockChunkControl:
    
    seed = None
    position = None
    blocksManager = None
    blocks = None
    dimensions = None
    
    def __init__(self, seed, position, blocksManager):
        self.seed = seed
        self.position = position
        self.blocksManager = blocksManager
        self.dimensions = (16,128)
        blocks = [None] * (self.dimensions[0]*self.dimensions[1])
        
        assert isinstance(blocksManager, BlocksManager)
        
        #GENERATION
        rand = random.Random()
        rand.seed(seed)
        for i in range(len(blocks)):
            x = i%self.dimensions[0]
            y = self.dimensions[1] - ((i)/self.dimensions[0])
            print x, y
            if(y > 64):
                blocks[i] = blocksManager.getBlockById(0)
            if(y == 64):
                blocks[i] = blocksManager.getBlockById(2)
            if(y < 64):
                blocks[i] = blocksManager.getBlockById(1)
                
        self.blocks = blocks
        
    def getBlocks(self):
        return self.blocks
    
    def getDimensions(self):
        return self.dimensions
    
    def convertToX(self, convert):
        return convert%self.dimensions[0]
    
    def convertToY(self, convert):
        return self.dimensions[1] - ((convert/self.dimensions[0])) - 1
    
    def convertToCoords(self, tile):
        return (self.convertToX(tile),self.convertToY(tile))
    
    def convertFromCoords(self, coord):
        x = self.dimensions[0] - coord[0]
        y = self.dimensions[1] * coord[1]
        return y-x