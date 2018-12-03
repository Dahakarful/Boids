class BadZone:

    def __init__(self, x, y, radius=10, liveTime=100):
        self.x = x
        self.y = y
        self.radius = radius
        self.liveTime = liveTime
    
    def update(self):
        self.liveTime = self.liveTime - 1
    
    def isDead(self):
        if self.liveTime < 0:
            return True
        return False
    
    