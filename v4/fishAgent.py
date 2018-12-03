from math import *
from worldObject import WorldObject
import random

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
        color = ['blue', 'green', 'orange', 'black', 'red', 'grey', 'purple']
        i = random.randint(0, 6)
        self.color = color[i]
    
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
        self.computeAverageDirection(fish)
        self.avoidWall(0, maxWidth, 0, maxHeight)
        self.avoidFishs(fish)
        self.avoidObstacle(obstacles)
    
    def avoidWall(self, wallXMin, wallXMax, wallYMin, wallYMax):
        if self.x > wallXMax - 10:
            self.vx = self.vx - FishAgent.WALL_AVOID
        if self.x < wallXMin + 10:
            self.vx = self.vx + FishAgent.WALL_AVOID
        if self.y > wallYMax - 10:
            self.vy = self.vy - FishAgent.WALL_AVOID
        if self.y < wallYMin + 10:
            self.vy = self.vy + FishAgent.WALL_AVOID
        self.normalise()
    
    def avoidFishs(self, fishs):
        for fish in fishs:
            if fish != self:
                x1 = fish.x - self.x
                y1 = fish.y - self.y
                squareDistance = pow(x1,2) + pow(y1,2)
                if squareDistance < FishAgent.SQUARE_DISTANCE_MIN:
                    self.vx = self.vx - x1
                    self.vy = self.vy - y1
                    self.normalise()
    
    def computeAverageDirection(self, fishs):
        vxAverage = 0
        vyAverage = 0
        countFish = 0
        for fish in fishs:
            if fish != self:
                x1 = fish.x - self.x
                y1 = fish.y - self.y
                squareDistance = pow(x1,2) + pow(y1,2)
                if squareDistance > FishAgent.SQUARE_DISTANCE_MIN and squareDistance < FishAgent.SQUARE_DISTANCE_MAX:
                    vxAverage += fish.vx
                    vyAverage +=fish.vy
                    countFish += 1
        if countFish > 0:
            vxAverage = vxAverage / countFish
            vyAverage = vyAverage / countFish
            self.vx += vxAverage
            self.vy += vyAverage
            self.normalise()

    def avoidObstacle(self, obstacles):
        for obstacle in obstacles:
            x1 = obstacle.x - self.x
            y1 = obstacle.y - self.y
            squareDistance = pow(x1,2) + pow(y1,2)
            if squareDistance < FishAgent.SQUARE_DISTANCE_MIN:
                self.vx = self.vx - x1
                self.vy = self.vy - y1
                self.normalise()