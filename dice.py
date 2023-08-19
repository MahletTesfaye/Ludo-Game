from random import randint

class Dice:
    def __init__(self):
        self.initialPosition = (0, 0)
        self.isSpent = True
        self.reroll = False
        self.__value = 1

    def roll(self):
        diceNumber = randint(1, 6)
        self.isSpent = True
        self.reroll = True if diceNumber in [1,6] else False
        self.__value = diceNumber
        # return self.__value
    
    def fakeRoll(self, diceNumber):
        self.isSpent = True
        self.reroll = True if diceNumber in [1,6] else False
        self.__value = diceNumber
        # return self.__value
    
    def getRoll(self)->int:
        return self.__value
    


    
