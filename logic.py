from cell import *
from ball import *
from dice import *

redPath = [Br1,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,Bb2,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,C24,By3,C25,C26,C27,C28,C29,C30,C31,C32,C33,C34,C35,C36,Bg4,C37,C38,C39,C40,C41,C42,C43,C44,C45,C46,C47,Ar1,Ar2,Ar3,Ar4,Ar5,Ar6]

bluePath = [Bb2,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,C24,By3,C25,C26,C27,C28,C29,C30,C31,C32,C33,C34,C35,C36,Bg4,C37,C38,C39,C40,C41,C42,C43,C44,C45,C46,C47,C48,Br1,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,Ab1,Ab2,Ab3,Ab4,Ab5,Ab6]

yellowPath = [By3,C25,C26,C27,C28,C29,C30,C31,C32,C33,C34,C35,C36,Bg4,C37,C38,C39,C40,C41,C42,C43,C44,C45,C46,C47,C48, Br1,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,Bb2,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,Ay1,Ay2,Ay3,Ay4,Ay5,Ay6]

greenPath = [Bg4,C37,C38,C39,C40,C41,C42,C43,C44,C45,C46,C47,C48, Br1,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,Bb2,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,C24,By3,C25,C26,C27,C28,C29,C30,C31,C32,C33,C34,C35,Ag1,Ag2,Ag3,Ag4,Ag5,Ag6]

pathLst = [redPath, bluePath, yellowPath, greenPath]
colorlst = ['red', 'blue', 'yellow', 'green']
destination6Cell = [Ar6,Ab6,Ay6,Ag6]

rb1, rb2, rb3, rb4 = Ball('rb1', 'red', Dr1, Ar6), Ball('rb2', 'red', Dr2, Ar6), Ball('rb3', 'red', Dr3, Ar6), Ball('rb4', 'red', Dr4, Ar6)
bb1, bb2, bb3, bb4 = Ball('bb1', 'blue', Db1, Ab6), Ball('bb2', 'blue', Db2, Ab6), Ball('bb3', 'blue', Db3, Ab6), Ball('bb4', 'blue', Db4, Ab6)
yb1, yb2, yb3, yb4 = Ball('yb1', 'yellow', Dy1, Ay6), Ball('yb2', 'yellow', Dy2, Ay6), Ball('yb3', 'yellow', Dy3, Ay6), Ball('yb4', 'yellow', Dy4, Ay6)
gb1, gb2, gb3, gb4 = Ball("gb1", 'green', Dg1, Ag6), Ball("gb2", 'green', Dg2, Ag6), Ball('gb3', 'green', Dg3, Ag6), Ball('gb4', 'green', Dg4, Ag6)

player1 = [rb1, rb2, rb3, rb4]
player2 = [bb1, bb2, bb3, bb4]
player3 = [yb1, yb2, yb3, yb4]
player4 = [gb1, gb2, gb3, gb4]

dice = Dice()

def turn(player: list[Ball], playerLst):
    path = pathLst[playerLst.index(player)]
    ball1:Ball = player[0]
    ball2:Ball = player[1]
    ball3:Ball = player[2]
    ball4:Ball = player[3]
    return path, ball1, ball2, ball3, ball4
    
# path, ball1, ball2, ball3, ball4   = turn(player2)
# print(len(path))

def nextTurn(oldplayer: list[Ball], playerLst):
    oldIndex = playerLst.index(oldplayer)
    newIndex = (oldIndex+1)% len(playerLst)
    newPlayer = playerLst[newIndex]
    return newPlayer

# newPlayer = nextTurn(player3)

''' Remove ball from availableBallLst after reaching the goal'''
def removeBall(availableBallLst: list[Ball], ball:Ball):
    availableBallLst.remove(ball)
    return availableBallLst

def move(ball:Ball, dice:Dice, path:list[Cell]):
    print(f'ball old position : {ball.cell}')
    oldIndex = path.index(ball.cell)
    newIndex = oldIndex + dice.getRoll()
    path[oldIndex]:Ball
    if (newIndex < len(path)):
        ball.cell.remove(ball)
        ball.cell = path[newIndex]
        path[newIndex]:Cell
        path[newIndex].add(ball, dice)
        if(path[newIndex] in destination6Cell):
            print(f'{ball} reaches to the goal {path[newIndex].id}')
            removeBall(availableBallLst, ball)
            ball.atDestination = True
            dice.reroll=True            
        print(path[newIndex])      
    else:
        print("Ball can't move")

def ableToMove(path:list[Cell], ball: Ball, diceNumber: int ):
    if ball.atDestination:
        return False
    else:
        if (diceNumber in [1,6]):
            if (ball.cell == ball.defaultCell):
                return True
            if ((path.index(ball.cell)+ diceNumber)>len(path)-1):
                    return False
            else:
                return True
        else:
            if ball.defaultCell == ball.cell:
                return False
        if ((path.index(ball.cell)+ diceNumber)>len(path)-1):
            return False
        else:
            return True

def choose(choice, dice: Dice, path:list[Cell], availableBallLst:list[Ball]):
    if (choice in range(len(availableBallLst))):
        ball:Ball = availableBallLst[choice]
        if (ball.cell == ball.defaultCell): 
            path[0]:Cell
            path[0].add(ball, dice)
            print(path[0])
        else:
            move(ball, dice, path)
        
def isWinner(ballLst:list[Ball]):
    win = True
    for ball in ballLst:
        if (win == False):
            break
        if (not(ball.atDestination)):
            win = False
    return win
    
playerLst = [player1, player2, player3, player4]
currentPlayer = player1

while(True):
    print(f'\n******** player color {currentPlayer[0].color} ********')
    if (len(playerLst) == 1):
        print('Game over!!')
        break
    path, ball1, ball2, ball3, ball4 = turn(currentPlayer, playerLst)
    print(path[0].id, ball1.id)
    ballLst = [ball1, ball2, ball3, ball4]
    
    availableBallLst = []
    ''' 
    check if there is a winner
    '''
    if (len(availableBallLst) == 0):
        win = isWinner(ballLst)
        if (win == True):
            print(f'"{ballLst[0].color} is the winner"')
            want_to_continue = input('Do you want to continue playing (y/n): ')
            
            if (want_to_continue == 'y'):
                dice.isSpent == True
                oldCurrentPlayer = currentPlayer
                currentPlayer = nextTurn(currentPlayer, playerLst)
                pathLst.remove(pathLst[playerLst.index(oldCurrentPlayer)])
                playerLst.remove(oldCurrentPlayer)
                continue
            else:
                print('Game over!!')
                break
    '''
    If dice is spent, dice can be rolled 
    '''
    if (dice.isSpent == True):
        dice.roll()
        print(f'diceNumber : {dice.getRoll()}')
        # diceNumber = int(input('Dice rolls to : '))
        # dice.fakeRoll(diceNumber)
        
    for ball in ballLst:
        if ableToMove(path, ball, dice.getRoll()):
            availableBallLst.append(ball)            
    
    ''' 
    ball_in_default_or_destination_cell = True means that all balls are in their default cell or in destination cell
    '''
    ball_in_default_or_destination_cell = True
    for ball in ballLst:
        if (ball_in_default_or_destination_cell == False):
            break
        if (not(ball.defaultCell == ball.cell or ball.atDestination)):
            ball_in_default_or_destination_cell = False
    
    if ((dice.getRoll() in [1, 6])):        
        if (ball_in_default_or_destination_cell == True):
            print('pop---------------------')
            path[0].add(availableBallLst[0], dice)
            print(path[0])
            dice.isSpent = True
        else:
            ''' 
            choose (pop from default cell or move)
            '''
            choice = int(input(f'choices: ball {[f"{i}:{availableBallLst[i].id}" for i in range(len(availableBallLst))]}: '))
            if choice < len(availableBallLst):
                if( ableToMove(path,availableBallLst[choice],dice.getRoll()) == False):
                    print(f'\nPlease choose from the available balls\n')
                    dice.isSpent = False
                else:
                    choose(choice, dice, path, availableBallLst)
                    dice.isSpent = True
            else:
                print(f'\nPlease choose from the available balls\n')
                dice.isSpent = False
    else:
        if (ball_in_default_or_destination_cell == True):
            currentPlayer = nextTurn(currentPlayer, playerLst)
            print('current player changed (no balls to move all in home) -> ', colorlst[playerLst.index(currentPlayer)] )
        else:
            if len(availableBallLst) == 1:
                if(ableToMove(path,availableBallLst[0],dice.getRoll()) == False):
                    print("Ball can't move")
                    currentPlayer = nextTurn(currentPlayer,playerLst)
                    print('current player changed (mandatory move only one ball) -> ', colorlst[playerLst.index(currentPlayer)])
                else:
                    choose(0, dice, path, availableBallLst)
                    if (dice.reroll == True):
                        print('\nyou can reroll the dice')
                    else:
                        currentPlayer = nextTurn(currentPlayer,playerLst)
                        print('current player changed (mandatory move only one ball) -> ', colorlst[playerLst.index(currentPlayer)] )                        
                dice.isSpent = True
                
            else:
                choice = int(input(f'choices: ball {[f"{i}:{availableBallLst[i].id}" for i in range(len(availableBallLst))]}: '))
                if choice < len(availableBallLst):
                    if( ableToMove(path,availableBallLst[choice],dice.getRoll()) == False):
                        print(f'\nPlease choose number from {[i for i in range(len(availableBallLst))]}!')
                        dice.isSpent = False
                    else:
                        choose(choice, dice, path, availableBallLst)    
                        if (dice.reroll == True):
                            print('\nyou can reroll the dice')                        
                        else:
                            currentPlayer = nextTurn(currentPlayer,playerLst)
                            print('current player changed (dice used) -> ', colorlst[playerLst.index(currentPlayer)] )
                        dice.isSpent = True
                else:
                    print(f'\nPlease choose number from {[i for i in range(len(availableBallLst))]}!')
                    dice.isSpent = False
    print(f'\nb1 cell: {ball1.cell}\nb2 cell: {ball2.cell}\nb3 cell: {ball3.cell}\nb4 cell: {ball4.cell}')
    
    