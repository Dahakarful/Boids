from math import *

class WorldObject:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distanceTo(self, worldObject):
        x1 = worldObject.x - self.x
        y1 = worldObject.y - self.y
        return sqrt(pow(x1,2) + pow(y1,2))
    
    def squareDistance(self, worldObject):
        x1 = worldObject.x - self.x
        y1 = worldObject.y - self.y
        return pow(x1,2) + pow(y1,2)