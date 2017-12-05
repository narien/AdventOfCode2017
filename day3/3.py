import sys
from itertools import product
import math
import numpy

def fillMatrix(fillMode):
    global direction
    global x
    global y
    count = 1
    mem[x][y] = count
    while count < input:
        count += 1
        tryChangeDir()
        nextEle()
        if fillMode == 1:
            mem[x][y] = count
        else:
            mem[x][y] = mSum(neighbours((x, y)))
            if mem[x][y] > input:
                print("first larger value: ", int(mem[x][y]))
                print(mem)
                sys.exit()

def tryChangeDir():
    global direction
    global x
    global y
    if direction == 0: 
        if mem[x + 1][y] == 0: direction = 1
    elif direction == 1:
        if mem[x][y + 1] == 0: direction = 2
    elif direction == 2:
        if mem[x - 1][y] == 0: direction = 3
    else:
        if mem[x][y - 1] == 0: direction = 0

def nextEle():
    global direction
    global x
    global y

    if direction == 0: y -= 1
    elif direction == 1: x += 1
    elif direction == 2: y += 1
    else: x -= 1

#return list of adjacent elements
def neighbours(cell):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < side for n in c):
            yield c

#sum adjacent elements
def mSum(aList):
    global mem
    total = 0
    for t in aList:
        total += mem[t[0]][t[1]]
    return total

input = int(sys.argv[1])
side = math.ceil(math.sqrt(input)) if math.ceil(math.sqrt(input)) % 2 != 0 else math.ceil(math.sqrt(input)) + 1
middleCoord = math.ceil(side/2) - 1
x = middleCoord
y = middleCoord
direction = 0 # 0 = down, 1 = right, 2 = up, 3 = left

mem = numpy.zeros(shape=(side, side))
fillMatrix(int(sys.argv[2]))
print("Distance: ", abs(x - middleCoord) + abs(y - middleCoord))
