class BlocksManager:
    
    blocks = None
    
    def __init__(self):
        self.blocks = (
        Block(0, None, "Stone"),
        Block(1, None, "Grass")
        )

class Block:
    id = None
    image = None
    name = None
    
    def __init__(self, id, image, name):
        self.id = id
        self.image = image
        self.name = name
    
    def getId(self):
        return self.id
    
    def getImage(self):
        return self.image
    
    def getName(self):
        return self.name
        