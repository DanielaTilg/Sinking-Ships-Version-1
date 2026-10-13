# Schiffe versenken version 1 (Nur Computer platziert Schiffe)

import random
import math

WIDTH = 9
HEIGHT = 9
NUM_TILES_1 = 4 #Schiffslänge
NUM_TILES_2 = 3
ship1 = []
ship2 = []

def drawBoard(board):
    print ('  123456789')
    for y in range(HEIGHT):
        print ('%s|' % (y+1), end = '')
        for x in range(WIDTH):
            print(board[x][y], end = '')
        print ('|%s' % (y+1))
    print ('  123456789')
    print()

def getNewBoard():
    board = []
    for i in range(WIDTH):
        board.append(['~'] *9)
    return board

def getShip(numberTiles): #Computer platziert Schiffe auf dem Brett
    newShip = []
    if random.randint(0,1) == 0:   #horizontal
        a = random.randint(0, WIDTH - numberTiles)
        b = random.randint (0, HEIGHT - 1)
        for i in range(numberTiles):
            newShip.append((a + i, b))
    else:   #vertikal
        a = random.randint(0, WIDTH - 1)
        b = random.randint(0, HEIGHT - numberTiles)
        for i in range(numberTiles):
            newShip.append((a, b + i))
    return newShip

def shipsCollide(s1, s2):
    for (x,y) in s2:
        if (x,y) in s1:
            return True
    else: False

def isOnBoard(x, y):
    return x >= 0 and x <= WIDTH-1 and y >= 0 and y <= HEIGHT-1    

def getPlayerMove(board):
    while True:
        print ('Throw a bomb on a field of your choice (type coordinates xy).')
        DIGITS = '1 2 3 4 5 6 7 8 9'.split()
        move = input()
        if move[0] in DIGITS and move[1] in DIGITS:
         x = int(move[0])-1
         y = int(move[1])-1
        else:
            print ('Your move is not valid. Please choose again.')
            continue            
        if board[x][y] != '~':
            print ('You have made this move already / Your move is out of range. Please choose again.')
            continue
        elif isOnBoard(x, y) == False or len(move) != 2:
            print ('Your move is not valid. Please choose again.')
            continue
        else: return (x,y)        

def makeMove(s1,s2):
    x,y = getPlayerMove(board)
    if (x,y) in s1 or (x,y) in s2: 
        board[x][y] = 'X'
        print()
        print ('You hit a ship!!!')
        print()
        if (x, y) in s1:
            s1.remove((x, y))
        elif (x, y) in s2:
            s2.remove((x, y))
    else:
        board[x][y] = 'O'
        print()
        print ('You have not hit anything. Can you hit a ship with your next move?')
        print()

def isShipDown(s1, s2, s1_sunken, s2_sunken):
    if s1 == [] and s2 == []:
        drawBoard(board)
        print('You have won! All ships are sunken!')
        print()
        return True, s1_sunken, s2_sunken

    if s1 == [] and not s1_sunken:
        print('Great, you have sunken a ship with %s tiles!' % (NUM_TILES_1))
        print()
        s1_sunken = True  

    if s2 == [] and not s2_sunken:
        print('Great, you have sunken a ship with %s tiles!' % (NUM_TILES_2))
        print()
        s2_sunken = True  

    return False, s1_sunken, s2_sunken  


#MAIN GAME

print ('Welcome to Sinking Ships!') #Im Text Rateversuche/Schiffslänge anpassen.
print()
print ('''The Computer will place two ships on the board, which you have to find (one of 4 tiles and one of 3 tiles).
The ships can be placed vertically or horizontally.
Your move will be marked with 'X' when you hit a ship.
Your move will be marked with 'O' when you did not hit anything.
You have 20 guesses.
Press Enter to start.''')
print()
input()

while True:
    ship1 = []
    ship2 = []
    ship1_sunken = False
    ship2_sunken = False
    board = getNewBoard()
    moves = 0
    
    ship1 = getShip(NUM_TILES_1)
    while True:
        ship2 = getShip(NUM_TILES_2)
        if shipsCollide(ship1,ship2) == True:
            continue
        else: break        

    while True:
        drawBoard(board)
        print ('You have made %s moves.' % (moves))
        makeMove(ship1,ship2)
        moves += 1
        if moves >= 20:     #number of moves
            print ('You have run out of moves. You lost.')
            break

        game_over, ship1_sunken, ship2_sunken = isShipDown(ship1, ship2, ship1_sunken, ship2_sunken)
        if game_over == True:
            break

    print ('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
