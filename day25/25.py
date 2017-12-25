import sys
from collections import deque
def moveRight(ix, sMachine):
    if ix == len(sMachine) - 1:
        sMachine.append(0)
    ix += 1
    return ix

def moveLeft(ix, sMachine):
    if ix == 0:
        sMachine.appendleft(0)
    else:
        ix -= 1
    return ix

def updateState(currState, ix, sMachine):
    if currState == "A":
        if sMachine[ix] == 0:
            sMachine[ix] = 1
            ix = moveRight(ix, sMachine)
        else:
            sMachine[ix] = 0
            ix = moveLeft(ix, sMachine)
        currState = "B"
    elif currState == "B":
        if sMachine[ix] == 0:
            ix = moveRight(ix, sMachine)
            currState = "C"
        else:
            ix = moveLeft(ix, sMachine)
            currState = "B"
    elif currState == "C":
        if sMachine[ix] == 0:
            sMachine[ix] = 1
            ix = moveRight(ix, sMachine)
            currState = "D"
        else:
            sMachine[ix] = 0
            ix = moveLeft(ix, sMachine)
            currState = "A"
    elif currState == "D":
        if sMachine[ix] == 0:
            sMachine[ix] = 1
            currState = "E"
        else:
            currState = "F"
        ix = moveLeft(ix, sMachine)
    elif currState == "E":
        if sMachine[ix] == 0:
            sMachine[ix] = 1
            currState = "A"
        else:
            sMachine[ix] = 0
            currState = "D"
        ix = moveLeft(ix, sMachine)
    elif currState == "F":
        if sMachine[ix] == 0:
            sMachine[ix] = 1
            ix = moveRight(ix, sMachine)
            currState = "A"
        else:
            ix = moveLeft(ix, sMachine)
            currState = "E"
    return (currState, ix)

if __name__ == '__main__':
    sMachine = deque([0])
    stateAndIx = ("A", 0)
    for _ in range(12629077):
        stateAndIx = updateState(stateAndIx[0], stateAndIx[1], sMachine)
    print("Checksum is: ", sum(sMachine))
