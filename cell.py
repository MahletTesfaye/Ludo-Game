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

C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,C24,C25,C26,C27,C28,C29,C30,C31,C32,C33,C34,C35,C36,C37,C38,C39,C40,C41,C42,C43,C44,C45,C46,C47,C48,C49,C50,C51,C52 = Cell('C1', 'gray', 'open'),Cell('C2', 'gray', 'open'),Cell('C3', 'gray', 'open'),Cell('C4', 'gray', 'open'),Cell('C5', 'gray', 'open'),Cell('C6', 'gray', 'open'),Cell('C7', 'gray', 'open'),Cell('C8', 'gray', 'open'),Cell('C9', 'gray', 'open'),Cell('C10', 'gray', 'open'),Cell('C11', 'gray', 'open'),Cell('C12', 'gray', 'open'),Cell('C13', 'gray', 'open'),Cell('C14', 'gray', 'open'),Cell('C15', 'gray', 'open'),Cell('C16', 'gray', 'open'),Cell('C17', 'gray', 'open'),Cell('C18', 'gray', 'open'),Cell('C19', 'gray', 'open'),Cell('C20', 'gray', 'open'),Cell('C21', 'gray', 'open'),Cell('C22', 'gray', 'open'),Cell('C23', 'gray', 'open'),Cell('C24', 'gray', 'open'),Cell('C25', 'gray', 'open'),Cell('C26', 'gray', 'open'),Cell('C27', 'gray', 'open'),Cell('C28', 'gray', 'open'),Cell('C29', 'gray', 'open'),Cell('C30', 'gray', 'open'),Cell('C31', 'gray', 'open'),Cell('C32', 'gray', 'open'),Cell('C33', 'gray', 'open'),Cell('C34', 'gray', 'open'),Cell('C35', 'gray', 'open'),Cell('C36', 'gray', 'open'),Cell('C37', 'gray', 'open'),Cell('C38', 'gray', 'open'),Cell('C39', 'gray', 'open'),Cell('C40', 'gray', 'open'),Cell('C41', 'gray', 'open'),Cell('C42', 'gray', 'open'),Cell('C43', 'gray', 'open'),Cell('C44', 'gray', 'open'),Cell('C45', 'gray', 'open'),Cell('C46', 'gray', 'open'),Cell('C47', 'gray', 'open'),Cell('C48', 'gray', 'open'),Cell('C49', 'gray', 'open'),Cell('C50', 'gray', 'open'),Cell('C51', 'gray', 'open'),Cell('C52', 'gray', 'open')

Ar1,Ar2,Ar3,Ar4,Ar5,Ar6 = Cell('Ar1', 'red', 'destination'),Cell('Ar2', 'red', 'destination'),Cell('Ar3', 'red', 'destination'),Cell('Ar4', 'red', 'destination'),Cell('Ar5', 'red', 'destination'),Cell('Ar6', 'red', 'destination')

Ab1,Ab2,Ab3,Ab4,Ab5,Ab6 = Cell('Ab1', 'blue', 'destination'),Cell('Ab2', 'blue', 'destination'),Cell('Ab3', 'blue', 'destination'),Cell('Ab4', 'blue', 'destination'),Cell('Ab5', 'blue', 'destination'),Cell('Ab6', 'blue', 'destination')

Ay1,Ay2,Ay3,Ay4,Ay5,Ay6 = Cell('Ay1', 'yellow', 'destination'),Cell('Ay2', 'yellow', 'destination'),Cell('Ay3', 'yellow', 'destination'),Cell('Ay4', 'yellow', 'destination'),Cell('Ay5', 'yellow', 'destination'),Cell('Ay6', 'yellow', 'destination')

Ag1,Ag2,Ag3,Ag4,Ag5,Ag6 = Cell('Ag1', 'green', 'destination'),Cell('Ag2', 'green', 'destination'),Cell('Ag3', 'green', 'destination'), Cell('Ag4', 'green', 'destination'),Cell('Ag5', 'green', 'destination'),Cell('Ag6', 'green', 'destination')

Br1 = Cell('Br1', 'red', 'home')
Bb2 = Cell('Bb2', 'blue', 'home')
By3 = Cell('By3', 'yellow', 'home')
Bg4 = Cell('Bg4', 'green', 'home')

Dg1, Dg2, Dg3, Dg4 = Cell('Dg1', 'green', 'default'), Cell('Dg2', 'green', 'default'), Cell('Dg3', 'green', 'default'), Cell('Dg4', 'green', 'default')
Dr1, Dr2, Dr3, Dr4 = Cell('Dr1', 'red', 'default'), Cell('Dr2', 'red', 'default'), Cell('Dr3', 'red', 'default'), Cell('Dr4', 'red', 'default')
Dy1, Dy2, Dy3, Dy4 = Cell('Dy1', 'yellow', 'default'), Cell('Dy2', 'yellow', 'default'), Cell('Dy3', 'yellow', 'default'), Cell('Dy4', 'yellow', 'default')
Db1, Db2, Db3, Db4 = Cell('Db1', 'blue', 'default'), Cell('Db2', 'blue', 'default'), Cell('Db3', 'blue', 'default'), Cell('Db4', 'blue', 'default')
