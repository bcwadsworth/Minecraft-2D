import pygame
pygame.init()

class pywindow:
    def __init__ (self, width = 500, length = 500, string = 'None', icon = 'None', backColor = (0,0,0)):
        self.width = width
        self.length = length
        self.resolution = (self.width, self.length)
        self.windowString = string
        self.windowIcon = icon
        self.fullscreen = False
        self.resizable = False
        self.frame = True
        self.backColor = backColor
    
    def updateRes(self):
        self.resolution = (width, length)
        
    def updateScreen(self):
        if not self.fullscreen and not self.resizable and not self.frame:
            self.screen = pygame.display.set_mode(self.resolution, pygame.NOFRAME)
        if not self.fullscreen and not self.resizable and self.frame:
            self.screen = pygame.display.set_mode(self.resolution)
        if not self.fullscreen and self.resizable and not self.frame:
            self.screen = pygame.display.set_mode(self.resolution, pygame.NOFRAME|pygame.RESIZABLE)
        if not self.fullscreen and self.resizable and self.frame:
            self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE)
        if self.fullscreen and not self.resizable and not self.frame:
            self.screen = pygame.display.set_mode(self.resolution, pygame.NOFRAME|pygame.FULLSCREEN)
        if self.fullscreen and not self.resizable and self.frame:
            self.screen = pygame.display.set_mode(self.resolution|pygame.FULLSCREEN)
        if self.fullscreen and self.resizable and not self.frame:
            self.screen = pygame.display.set_mode(self.resolution, pygame.NOFRAME|pygame.RESIZABLE|pygame.FULLSCREEN)
        if self.fullscreen and self.resizable and self.frame:
            self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE|pygame.FULLSCREEN)

    def updateSysstat(self):
        if self.windowString != 'None':
            pygame.display.set_caption(self.windowString)
        if self.windowIcon != 'None':
            pygame.display.set_icon(self.windowIcon)

    def update(self):
        self.screen.fill(self.backColor)
        for n in range(0, gameObject.gameObjects):
            if gameObject.gameObjectArray[n][0]:
                self.screen.blit(gameObject.gameObjectArray[n][1], gameObject.gameObjectArray[n][2])
                # Array Entry = True, file, position
            else:
                if gameObject.gameObjectArray[n][1]:
                    pygame.draw.Rect(self.screen, gameObject.gameObjectArray[n][3],gameObject.gameObjectArray[n][2])
                    # Array Entry = False, True, Rect, Color
                else:
                    pygame.draw.circle(self.screen, gameObject.gameObjectArray[n][4], gameObject.gameObjectArray[n][2], gameObject.gameObjectArray[n][3])
                    # Array Entry = False, False, Coordinates, Radius, Color
        pygame.display.flip()


class gameObject:
     gameObjects = 0
     gameObjectArray = []
     def __init__(self, blit, shape, x, y, lengthradius, width, filename, color):
         if blit:
              self.active = True
              self.blit = True
              self.file = pygame.image.load(filename)
              self.x = x
              self.y = y
              self.array = -1
              
         elif shape:
              self.active = True
              self.blit = True
              self.shape = True
              self.x = x
              self.y = y
              self.length = lengthradius
              self.width = width
              self.color = color
              self.array = -1
              
         else:
              self.active = True
              self.blit = True
              self.shape = False
              self.x = x
              self.y = y
              self.radius = lengthradius
              self.color = color
              self.array = -1
          
         self.update()
         print str(self) +" Initialized'
          
     def update(self):
          if self.active and self.blit:
               if self.array == -1:
                    self.position = (self.x,self.y)
                    gameObject.gameObjectArray.append([True, self.file, self.position])
                    self.array = len(gameObject.gameObjectArray) - 1
                    gameObject.gameObjects += 1
               else:
                    self.position = (self.x,self.y)
                    gameObject.gameObjectArray[self.array] = [True, str(self.filename), self.position]
          elif self.active and self.shape:
               if self.array == -1:
                    self.rect = pygame.Rect(self.x, self.y, self.length, self.width)
                    gameObject.gameObjectArray.append([False, True, self.rect, self.color])
                    self.array = len(gameObject.gameObjectArray) - 1
                    gameObject.gameObjects += 1
               else:
                    self.rect = pygame.Rect(self.x, self.y, self.length, self.width)
                    gameObject.gameObjectArray.append([False, True, self.rect, self.color])
          elif self.active and not self.shape:
               if self.array == -1:
                    self.position = (self.x,self.y)
                    gameObject.gameObjectArray.append([False, False, self.position, self.radius, self.color])
                    self.array = len(gameObject.gameObjectArray) - 1
                    gameObject.gameObjects += 1
               else:
                    gameObject.gameObjectArray.append([False, False, self.position, self.radius, self.color])
          else:
               if self.array == -1:
                    pass
               else:
                    gameObject.gameObjectArray.remove(self.array)
                    self.array = -1
                    gameObject.gameObjects += -1
                    
               

