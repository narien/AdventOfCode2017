import sys
import string


def swapPrograms(ix1, ix2, myList):
    programA = myList[ix1]
    myList[ix1] = myList[ix2]
    myList[ix2] = programA
    return myList

def dance(sequence, myList):
    for command in sequence:
        if command[0] == 's':
            myList = myList[len(myList) - int(command[1:]):] + myList[:len(myList) - int(command[1:])]
        elif command[0] == 'x':
            currProgramIxs = list(map(int, command[1:].split("/")))
            myList = swapPrograms(currProgramIxs[0], currProgramIxs[1], myList)
        elif command[0] == 'p':
            currProgramIds = list(command[1:].split("/"))
            myList = swapPrograms(myList.index(currProgramIds[0]), myList.index(currProgramIds[1]), myList)
    return myList

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        sequence = f.readline().strip().split(",")
    myList = list(string.ascii_lowercase[:16])

    prevLists = list()
    for i in range(1000000000):
        newOrder = ''.join(myList)
        if newOrder in prevLists:
            print("order after 1B dances: ", prevLists[1000000000 % i])
            break
        prevLists.append(newOrder)
        myList = dance(sequence, myList)

    print("first dance: ", prevLists[1])




