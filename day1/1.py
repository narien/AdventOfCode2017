import sys

with open(sys.argv[1], 'r') as f:
    myList = list(f.readline())
myList = list(map(int, myList))

n = 1 if sys.argv[2] == '1' else int(len(myShiftedList)/2)
myShiftedList = myList[n:] + myList[:n]

total = 0
for i in range (len(myList)):
    if myList[i] == myShiftedList[i]:
        total += myList[i]

print("total: ", total)