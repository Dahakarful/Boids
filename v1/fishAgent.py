from math import *
from worldObject import WorldObject

class FishAgent:

    STEP = 2.0 # pas de déplacement
    DISTANCE_MIN = 10.0
    DISTANCE_MAX = 30.0
    SQUARE_DISTANCE_MIN = 100.0
    SQUARE_DISTANCE_MAX = 900.0
    WALL_AVOID = 0.3

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.vx = cos(direction)
        self.vy = sin(direction)
    
    def updatePosition(self):
        self.x = self.x + self.vx * FishAgent.STEP
        self.y = self.y + self.vy * FishAgent.STEP

    def normalise(self):
        norm = sqrt(pow(self.vx, 2) + pow(self.vy, 2))
        self.vx = self.vx / norm
        self.vy = self.vy / norm 
    
    def near(self, fishAgent):
        x1 = fishAgent.x - self.x
        y1 = fishAgent.y - self.y
        squareDistance = pow(x1,2) + pow(y1,2)
        if squareDistance >= FishAgent.SQUARE_DISTANCE_MIN and squareDistance <= FishAgent.SQUARE_DISTANCE_MAX:
            return True
        return False

    def update(self, fish, obstacles, maxWidth, maxHeight):
        self.updatePosition()