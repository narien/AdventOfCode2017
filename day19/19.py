import sys

def traverse(diagram):
    lettersPassed = list()
    currRow = 1
    currCol = diagram[0].index("|")
    direction = "down"
    oldRow = 0
    oldCol = currCol
    steps = 0
    while True:
        steps += 1
        selectionMade = False
        #print(currRow, " ", currCol, " ", diagram[currRow][currCol])
        if diagram[currRow][currCol] == "+":
            if currCol > 0 and not selectionMade:
                #print("checking left")
                if diagram[currRow][currCol - 1] == "-" and oldCol != currCol - 1:
                    #print(direction)
                    direction = "left"
                    selectionMade = True
                    #print(direction)
            if currCol < (len(diagram[currRow]) - 1) and not selectionMade:
                #print("here")
                if diagram[currRow][currCol + 1] == "-" and oldCol != currCol + 1:
                    #print(direction)
                    direction = "right"
                    selectionMade = True
                    #print(direction)
            if currRow < (len(diagram) - 1) and not selectionMade:
                #print("checking down")
                if diagram[currRow + 1][currCol] == "|"  and oldRow != currRow + 1:
                    #print(direction)
                    direction = "down"
                    selectionMade = True
                    #print(direction)
            if currRow > 0 and not selectionMade:
                if diagram[currRow - 1][currCol] == "|"  and oldRow != currRow - 1:
                #print(direction)
                    direction = "up"
                    selectionMade = True
                #print(direction)

        elif diagram[currRow][currCol] not in "|-":
            lettersPassed.append(diagram[currRow][currCol])
            print("".join(lettersPassed))
            print(steps)

        oldRow = currRow
        oldCol = currCol
        if direction == "down":
            currRow += 1
        elif direction == "right":
            currCol += 1
        elif direction == "up":
            currRow -= 1
        elif direction == "left":
            currCol -= 1
        if diagram[currRow][currCol].isspace():
            break
    return lettersPassed





if __name__ == '__main__':
    diagram = list()
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            lineList = list()
            for c in line:
                lineList.append(c)
            diagram.append(lineList)
    print(str(traverse(diagram)))






