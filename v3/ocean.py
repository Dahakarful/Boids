from math import *
import random
from fishAgent import FishAgent
from badZone import BadZone

class Ocean:
    
    def __init__(self, nbFishs, maxWidth, maxHeight):
        self.nbFishs = nbFishs
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.fishs = []
        self.obstacles = []
        
        for _ in range(nbFishs):
            x = self.maxWidth * random.random()
            y = self.maxHeight * random.random()
            direction = 2 * pi * random.random()
            self.addFish(x, y, direction)
    
    def addFish(self, x, y, direction):
        self.fishs.append(FishAgent(x, y, direction))

    def update(self):
        for fish in self.fishs:
            fish.update(self.fishs, self.obstacles, self.maxWidth, self.maxHeight)
        for obstacle in self.obstacles:
            obstacle.update()
            if obstacle.isDead():
                self.obstacles.remove(obstacle)
    
    def addObstacle(self, x, y):
        self.obstacles.append(BadZone(x, y))
        print(self.obstacles)
        print('ok')