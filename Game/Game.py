from Constant import * #@UnusedWildImport
from Planet.Star import * #@UnusedWildImport
import pygame
import numpy
from threading import Thread
from numpy import sqrt

class Game():
    def __init__(self, window_name, background, width, height):
        pygame.init() 
        
        self.num = 0
               
        self.background = background
        self.window_width = width
        self.window_height = height
        
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.window_name = window_name
        self.screen.fill(self.background)
        
        self.clock = pygame.time.Clock()        
        self.done = False
        
        obj = Star(900, 500, 0, 0, 100, str(self.num), const_red, True)
        self.starList = [obj,]
                
        self.run()

        
    def input_key(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.done = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    mass = numpy.random.randint(50)
                    x = numpy.random.randint(self.window_width)
                    y = numpy.random.randint(self.window_height)
                    deltaX, deltaY = numpy.random.rand(2)
                    if numpy.random.rand(1) > 0.5:
                        deltaX = -deltaX                        
                    if numpy.random.rand(1) > 0.5:
                        deltaY = -deltaY
                         
                    self.num += 1
                     
#                     deltaX *= 10
#                     deltaY *= 10
                    color = (numpy.random.randint(256), numpy.random.randint(256), numpy.random.randint(256))
                    obj = Star(x, y, deltaX, deltaY, mass, str(self.num), color)
                    self.starList.append(obj)
                                    
                
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE]:
#             pass
#         if keys[pygame.K_UP]:
#             self.obj.setY(self.obj.getY() - 1)
#         if keys[pygame.K_DOWN]:
#             self.obj.setY(self.obj.getY() + 1)
#         if keys[pygame.K_LEFT]:
#             self.obj.setX(self.obj.getX() - 1)
#         if keys[pygame.K_RIGHT]:
#             self.obj.setX(self.obj.getX() + 1)
            
    def update(self):
        self.input_key()        
        for each in self.starList:
            each.update()
            x = each.getX()
            y = each.getY()
            if x < -1000 or x > self.window_width + 1000 or y < - 1000 or y > self.window_height + 1000:
                self.starList.remove(each)
                each.__del__()
                
        print (len(self.starList))

        for each in self.starList:
            th = Thread(target=each.delta_update, args=(self.starList, ))            
            th.start()
        if len(self.starList) != 0:
            th.join()
        
        pygame.display.update()
        self.clock.tick(60)
        
    def draw(self, test=True):
        if test:  
            self.screen.fill(const_black)
            for each in self.starList:        
                pygame.draw.circle(self.screen, each.color, each.getXY(), int(sqrt(each.getMass())))
        
    def run(self):        
        while not self.done:            
            self.update()
            self.draw()
            
        self.close()
        
    def close(self):
        pygame.quit()
        
    
        
if __name__ == '__main__':
    game = Game('test', const_black, 1800, 1000)
    quit()
    