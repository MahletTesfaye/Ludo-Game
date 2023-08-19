
class Ball:
    def __init__(self, id , color, defaultCell, destCell):
        self.id = id
        # self.position = position
        self.color = color
        self.cell = defaultCell
        self.defaultCell = defaultCell
        self.atDestination = False
        self.destCell = destCell;
    def reset(self, dice):
        self.cell = self.defaultCell
        self.defaultCell.add(self, dice)
        
    def __str__(self):
        # return f"\nid = {self.id},  color = {self.color}, defaultCell : [{self.defaultCell}] "
        return self.id
    
    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id

