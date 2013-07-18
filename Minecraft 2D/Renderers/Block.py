from Renderers.utils import *

class BlocksManager:
    
    blocks = None
    blocksDimensions = None
    
    def __init__(self, pygame):
        self.blocksDimensions = (16,16)
        self.blocks = (
        Block(0, None, "Air"),
        Block(1, Image(pygame.image.load("assets/blocks/stone.png"), self.blocksDimensions, (0,0)), "Stone"),
        Block(2, Image(pygame.image.load("assets/blocks/grass_side.png"), self.blocksDimensions, (0,0)), "Grass"),
        Block(3, Image(pygame.image.load("assets/blocks/dirt.png"), self.blocksDimensions, (0,0)), "Dirt"),
        Block(4, Image(pygame.image.load("assets/blocks/cobblestone.png"), self.blocksDimensions, (0,0)), "Cobblestone"),
        Block(5, Image(pygame.image.load("assets/blocks/planks_oak.png"), self.blocksDimensions, (0,0)), "Oak Wood Plank"),
        Block(5.1, Image(pygame.image.load("assets/blocks/planks_spruce.png"), self.blocksDimensions, (0,0)), "Spruce Wood Plank"),
        Block(5.2, Image(pygame.image.load("assets/blocks/planks_birch.png"), self.blocksDimensions, (0,0)), "Birch Wood Plank"),
        Block(5.3, Image(pygame.image.load("assets/blocks/planks_jungle.png"), self.blocksDimensions, (0,0)), "Jungle Wood Plank"),
        Block(6, Image(pygame.image.load("assets/blocks/sapling_oak.png"), self.blocksDimensions, (0,0)), "Oak Sapling"),
        Block(6.1, Image(pygame.image.load("assets/blocks/sapling_spruce.png"), self.blocksDimensions, (0,0)), "Spruce Sapling"),
        Block(6.2, Image(pygame.image.load("assets/blocks/sapling_birch.png"), self.blocksDimensions, (0,0)), "Birch Sapling"),
        Block(6.3, Image(pygame.image.load("assets/blocks/sapling_jungle.png"), self.blocksDimensions, (0,0)), "Jungle Sapling"),
        Block(7, Image(pygame.image.load("assets/blocks/bedrock.png"), self.blocksDimensions, (0,0)), "Bedrock"),
        Block(8, Image(pygame.image.load("assets/blocks/water_flow.png"), self.blocksDimensions, (0,0)), "Water"),
        Block(9, Image(pygame.image.load("assets/blocks/water_still.png"), self.blocksDimensions, (0,0)), "Stationary Water"),
        Block(10, Image(pygame.image.load("assets/blocks/lava_flow.png"), self.blocksDimensions, (0,0)), "Lava"),
        Block(11, Image(pygame.image.load("assets/blocks/lava_still.png"), self.blocksDimensions, (0,0)), "Stationary Lava"),
        Block(12, Image(pygame.image.load("assets/blocks/obsidian.png"), self.blocksDimensions, (0,0)), "Obsidian"),
        Block(14, Image(pygame.image.load("assets/blocks/gold_ore.png"), self.blocksDimensions, (0,0)), "Gold Ore"),
        Block(15, Image(pygame.image.load("assets/blocks/iron_ore.png"), self.blocksDimensions, (0,0)), "Iron Ore"),
        Block(16, Image(pygame.image.load("assets/blocks/coal_ore.png"), self.blocksDimensions, (0,0)), "Coal Ore"),
        Block(17, Image(pygame.image.load("assets/blocks/lapis_ore.png"), self.blocksDimensions, (0,0)), "Lapis Lazuli Ore"),
        Block(18, Image(pygame.image.load("assets/blocks/diamond_ore.png"), self.blocksDimensions, (0,0)), "Diamond Ore"),
        Block(19, Image(pygame.image.load("assets/blocks/emerald_ore.png"), self.blocksDimensions, (0,0)), "Emerald Ore"),
        Block(20, Image(pygame.image.load("assets/blocks/redstone_ore.png"), self.blocksDimensions, (0,0)), "Redstone Ore")
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
    
    def getBlockDimensions(self):
        return self.blocksDimensions

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
        