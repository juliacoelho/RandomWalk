from tkinter import *
import random

class Window(Frame):
    
    def __init__(self):
        self.tk = Tk()
        self.tk.geometry("1000x1000+100+100")     
        self.tk.title("Random Walk")
        self.canvas = Canvas(self.tk,width=1000,height=1000,bg = "White")
        self.canvas.pack()
        self.positionX = 500
        self.positionY = 500
        self.walk()
        
    def getNextPoint(self):
        possiblePoints = [[self.positionX + 1, self.positionY], [self.positionX - 1, self.positionY], [self.positionX, self.positionY + 1], [self.positionX, self.positionY - 1]]
        return random.choice(possiblePoints)
    
    def walk(self):
        for i in range(1000000):
            nextPoints = self.getNextPoint()
            self.canvas.create_line(self.positionX, self.positionY, nextPoints[0], nextPoints[1])
            self.positionX, self.positionY = nextPoints[0], nextPoints[1]
            
randomWalk = Window()
mainloop()
