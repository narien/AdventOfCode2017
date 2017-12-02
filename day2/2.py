import sys
import itertools

checkSum = 0
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        currRow = list(map(int, list(line.split())))
        if(sys.argv[2] == 1):
            checkSum += max(currRow) - min(currRow)
        else:
            for i, j in itertools.permutations(currRow, 2):
                if i % j == 0: checkSum += i/j
print ("CheckSum: ", checkSum)
