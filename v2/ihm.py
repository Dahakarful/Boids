from tkinter import *
import random
from math import *
from ocean import Ocean

class Ihm:
    AGENT_LENGTH = 10

    def __init__(self, environment):
        self.environment = environment # l’océan dans notre cas
        fen = Tk()
        self.canvas = Canvas(fen, width=self.environment.maxWidth,height=self.environment.maxHeight, bg='white', bd=0)
        self.canvas.pack()
        self.fen = fen
        self.canvas.bind_all("a", self.addFish) #attacher une touche
        self.canvas.bind("<Button-3>", self.addFish) # attacher la souris
        self.fen.after(1000, self.update) # lancer la boucle principale
        self.fen.mainloop()
    
    def addFish(self, event):
        self.environment.addFish(event.x, event.y, random.random() * 2 * pi)
    
    def drawFish(self, fishAgent):
        self.canvas.create_line(fishAgent.x, fishAgent.y, fishAgent.x - Ihm.AGENT_LENGTH * fishAgent.vx, fishAgent.y - Ihm.AGENT_LENGTH * fishAgent.vy, fill='blue')
    
    def draw(self):
        self.canvas.delete(ALL)
        for fish in self.environment.fishs:
            self.drawFish(fish)
    
    def update(self):
        self.environment.update()
        self.draw()
        self.fen.after(25, self.update)

ocean = Ocean(100, 1000, 1000)
ihm = Ihm(ocean)
