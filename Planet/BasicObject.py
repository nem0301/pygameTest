import pygame

class BasicObject():
    def __init__(self, x, y):
        self.x = x
        self.y = y        
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getXY(self):
        return (int(self.getX()), int(self.getY()))
    
    def __del__(self):
        pass