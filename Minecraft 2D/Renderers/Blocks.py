from Base.utils import *

class BlocksManager:
    
    blocks = None
    
    def __init__(self, pygame):
        self.blocks = (
        Block(0, Image(pygame.image.load("assets/blocks/stone.png"), (16, 16), (0,0)), "Stone"),
        Block(1, Image(pygame.image.load("assets/blocks/grass.png"), (16, 16), (0,0)), "Grass")
        )
        
    def getBlockByName(self, name):
        for b in self.blocks:
            if(b.getName() == name):
                return b
        return None
    
    def getBlockById(self, bid):
        for b in self.blocks:
            if(b.getId() == bid):
                return b
        return None

class Block:
    bid = None
    image = None
    name = None
    
    def __init__(self, bid, image, name):
        self.bid = bid
        self.image = image
        self.name = name
    
    def getId(self):
        return self.bid
    
    def getImage(self):
        return self.image
    
    def getName(self):
        return self.name
        