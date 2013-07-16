from Renderers.utils import *

class BlocksManager:
    
    blocks = None
    
    def __init__(self, pygame):
        self.blocks = (
        Block(0, None, "Air"),
        Block(1, Image(pygame.image.load("assets/blocks/stone.png"), (16, 16), (0,0)), "Stone"),
        Block(2, Image(pygame.image.load("assets/blocks/grass_side.png"), (16, 16), (0,0)), "Grass"),
        Block(3, Image(pygame.image.load("assets/blocks/dirt.png"), (16, 16), (0,0)), "Dirt"),
        Block(4, Image(pygame.image.load("assets/blocks/cobblestone.png"), (16, 16), (0,0)), "Cobblestone"),
        Block(5, Image(pygame.image.load("assets/blocks/planks_oak.png"), (16, 16), (0,0)), "Oak Wood Plank"),
        Block(5.1, Image(pygame.image.load("assets/blocks/planks_spruce.png"), (16, 16), (0,0)), "Spruce Wood Plank"),
        Block(5.2, Image(pygame.image.load("assets/blocks/planks_birch.png"), (16, 16), (0,0)), "Birch Wood Plank"),
        Block(5.3, Image(pygame.image.load("assets/blocks/planks_jungle.png"), (16, 16), (0,0)), "Jungle Wood Plank"),
        Block(6, Image(pygame.image.load("assets/blocks/sapling_oak.png"), (16, 16), (0,0)), "Oak Sapling"),
        Block(6.1, Image(pygame.image.load("assets/blocks/sapling_spruce.png"), (16, 16), (0,0)), "Spruce Sapling"),
        Block(6.2, Image(pygame.image.load("assets/blocks/sapling_birch.png"), (16, 16), (0,0)), "Birch Sapling"),
        Block(6.3, Image(pygame.image.load("assets/blocks/sapling_jungle.png"), (16, 16), (0,0)), "Jungle Sapling"),
        Block(7, Image(pygame.image.load("assets/blocks/bedrock.png"), (16, 16), (0,0)), "Bedrock"),
        Block(8, Image(pygame.image.load("assets/blocks/water_flow.png"), (16, 16), (0,0)), "Water"),
        Block(9, Image(pygame.image.load("assets/blocks/water_still.png"), (16, 16), (0,0)), "Stationary Water"),
        Block(10, Image(pygame.image.load("assets/blocks/lava_flow.png"), (16, 16), (0,0)), "Lava"),
        Block(11, Image(pygame.image.load("assets/blocks/lava_still.png"), (16, 16), (0,0)), "Stationary Lava"),
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
        