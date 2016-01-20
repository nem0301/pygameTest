from BasicObject import BasicObject
import numpy
import math
from numpy import sqrt

gravity_constant = 1

class Star(BasicObject):
    def __init__(self, x, y, deltaX, deltaY, mass, name, color, fixed=False):
        BasicObject.__init__(self, x, y)
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.mass = mass
        self.fixed = fixed
        self.name = name
        self.color = color
        
    def getMass(self):
        return self.mass
        
    def update(self):
        if not self.fixed:
            self.x += self.deltaX
            self.y += self.deltaY
            if self.x > 2800:
                self.x = 0
            if self.x < -1000:
                self.x = 1799
            if self.y > 2000:
                self.y = -1000
            if self.y < 0:
                self.y = 999
    
    def delta_update(self, list):
        for each in list:
            if each == self:
                continue

            vector = ( ( each.x - self.x ) , ( each.y - self.y ) )
            r = math.hypot(vector[0], vector[1])
            
            if r <= int(sqrt(self.mass)):
                if self.getMass() > each.getMass():
                    self.deltaX -= self.deltaX * each.getMass() / self.mass
                    self.deltaY -= self.deltaY * each.getMass() / self.mass
                    self.mass += each.getMass()                    
                    list.remove(each)
                    each.__del__()
                    continue                    
                else:
                    each.deltaX -= each.deltaX * self.mass / each.getMass()
                    each.deltaY -= each.deltaY * self.mass / each.getMass()
                    each.mass += self.getMass()                                        
                    list.remove(self)
                    self.__del__()
            
            
            rsqaure = numpy.power(r, 2)                         
#             force = (each.mass * self.mass) / rsqaure
            force = (each.mass) / rsqaure
            force *= gravity_constant                        
            unitV = (vector[0]/r, vector[1]/r)
            unitV = (unitV[0] * force, unitV[1] * force)
            self.deltaX += unitV[0]
            self.deltaY += unitV[1]
            
            
        
