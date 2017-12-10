import sys
from functools import reduce

currIx = 0
skipSize = 0
myList = list(range(int(sys.argv[2])))

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

#Program start
hashCode = list()
with open(sys.argv[1]) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        hashCode.append(ord(c))

hashCode += [17, 31, 73, 47, 23]

for iter in range(64):
    for i in hashCode:
        hash(i)

sparseHash = list()
for i in range(0, 16):
    sparseHash.append('%02x'%reduce((lambda x, y: x ^ y), myList[i*16:i*16 + 16]))

print(''.join(sparseHash))
