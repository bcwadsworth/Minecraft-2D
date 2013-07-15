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
    
    def __init__(self, seed, position, blocksManager):
        self.seed = seed
        self.position = position
        self.blocksManager = blocksManager
        blocks = [None] * (256*16)
        
        assert isinstance(blocksManager, BlocksManager)
        
        #GENERATION
        rand = random(seed)
        for i in range(len(blocks)):
            x = i%16
            y = 256 - ((i-1)/16)
            if(y > 64):
                blocks[i] = blocksManager.getBlockById(0)
            if(y == 64):
                blocks[i] = blocksManager.getBlockById(2)
            if(y < 64):
                blocks[i] = blocksManager.getBlockById(1)
        
    def getBlocks(self):
        return self.blocks
    
    def convertToX(self, convert):
        return convert%16
    
    def convertToY(self, convert):
        return 256 - ((convert-1/16))