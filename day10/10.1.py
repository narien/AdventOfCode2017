import sys

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

with open(sys.argv[1]) as f:
    hashCode = list(map(int, f.readline().replace(" ", "").split(",")))

    for i in hashCode:
        hash(i)

print("finished list: ", myList)
print("first two values multiplied: ", myList[0]*myList[1])

