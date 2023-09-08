from dice import Dice
from ball import *

class Cell:
    def __init__(self, id, color, cellType):
        self.id = id
        # self.position = position
        self.lst = []
        self.color = color
        self.cellType = cellType
        
    def add(self, ball: Ball, dice: Dice):
        if (self.cellType == 'open'):
            if (len(self.lst) == 0) or (self.lst[0].color == ball.color) :
                self.lst.append(ball)
                dice.reroll = False
            else:
                i = 0
                while (i < len(self.lst)):
                    oldBall:Ball = self.lst[i]
                    oldBall.reset(dice)
                    i+=1
                self.lst = []
                self.lst.append(ball)
                dice.reroll = True
                
        elif (self.cellType == 'destination'):
            if (self.color == ball.color):
                self.lst.append(ball)
            dice.reroll = False

        else:
            self.lst.append(ball)
            dice.reroll = False
        ball.cell = self
    
    def remove(self, ball: Ball):
        i = 0
        while (i < len(self.lst)):
            if (self.lst[i].id == ball.id):
                self.lst.pop(i)
            i+=1
                
    def __str__(self):
        # return f"id = {self.id}, lst = {[str(ball) for ball in self.lst]}, color = {self.color}, cellType = {self.cellType} "
        return f"id = {self.id}, lst = {[str(ball) for ball in self.lst]}"
        
    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id
