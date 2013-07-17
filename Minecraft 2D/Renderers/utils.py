class Image:
    
    surface = None
    dimensions = None
    position = None
    
    def __init__(self, surface, dimensions, position):    
        self.surface = surface
        self.dimensions = dimensions
        self.position = position
        
    def getSurface(self):
        return self.surface
    
    def getDimensions(self):
        return self.dimensions
    
    def getPosition(self):
        return self.position
    
    def getWidth(self):
        return self.getDimensions()[0]
    
    def getHeight(self):
        return self.getDimensions()[1]
    
    def getX(self):
        return self.getPosition()[0]
    
    def getY(self):
        return self.getPosition()[1]
    
    def setPosition(self, position):
        self.position = position
        
    def setDimensions(self, dimensions):
        self.dimensions = dimensions
        
def average(a, b):
    return (a+b)/2
