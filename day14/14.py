import sys

"""START OF MODIFIED DAY 10 SOLUTION"""
from functools import reduce

currIx = 0
skipSize = 0
myList = list(range(256))

def hash(length):
    global currIx
    global skipSize
    global myList

    if (currIx + length) > len(myList):
        reverseList = myList[currIx:]
        reverseList += myList[:length - len(reverseList)]
    else:
        reverseList = myList[currIx:currIx + length]

    reverseList = reverseList[::-1]

    tmpIx = currIx
    for val in reverseList:
        if tmpIx == len(myList):
            tmpIx = 0
        myList[tmpIx] = val
        tmpIx += 1

    currIx = (currIx + length + skipSize) % len(myList)
    skipSize += 1

def doHash(hashString):

    #Program start
    hashCode = list()
    for c in hashString:
        hashCode.append(ord(c))

    hashCode += [17, 31, 73, 47, 23]

    for iter in range(64):
        for i in hashCode:
            hash(i)

    sparseHash = list()
    for i in range(0, 16):
        sparseHash.append('%02x'%reduce((lambda x, y: x ^ y), myList[i*16:i*16 + 16]))
    returnString = ''.join(sparseHash)
    return returnString


"""END OF MODIFIED DAY 10 SOLUTION"""

def removeGroup(i, j):
    global matrix
    matrix[i][j] = 0
    if i > 0 and matrix [i-1][j] == 1: removeGroup(i-1, j)
    if j > 0 and matrix [i][j-1] == 1: removeGroup(i, j-1)
    if j < 127 and matrix [i][j+1] == 1: removeGroup(i, j+1)
    if i < 127 and matrix [i+1][j] == 1: removeGroup(i+1, j)




hex2bin_map = {
   "0":"0000",
   "1":"0001",
   "2":"0010",
   "3":"0011",
   "4":"0100",
   "5":"0101",
   "6":"0110",
   "7":"0111",
   "8":"1000",
   "9":"1001",
   "a":"1010",
   "b":"1011",
   "c":"1100",
   "d":"1101",
   "e":"1110",
   "f":"1111",
}

with open(sys.argv[1], 'r') as f:
    inputString = f.read()
    inputString += "-"

matrix = [[0 for x in range(128)] for y in range(128)] 
for riMatrix in range(128):
    ciMatrix = 0
    currIx = 0
    skipSize = 0
    myList = list(range(256))
    rowString = inputString + str(riMatrix)

    returnString = doHash(rowString)
    for c in returnString:
        binaryStr = hex2bin_map[c]
        for j in binaryStr:
            matrix[riMatrix][ciMatrix] = int(j)
            ciMatrix += 1

print("Used squares: ",sum(map(sum, matrix)))

groups = 0
for i in range(128):
    for j in range(128):
        if matrix[i][j] == 1:
            groups += 1
            removeGroup(i, j)

print("Total groups: ", groups)


