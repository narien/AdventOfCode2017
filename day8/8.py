import sys

varList = dict()
highestVal = 0
with open(sys.argv[1]) as f:
    for line in f:
        command = list(line.split())
        if command[0] not in varList:
            varList[command[0]] = 0
        if command[4] not in varList:
            varList[command[4]] = 0
        
        increase = True if command[1] == "inc" else False
        validOp = False
        if command[5] == '>':
            if varList[command[4]] > int(command[6]):
                validOp = True
        elif command[5] == '<':
            if varList[command[4]] < int(command[6]):
                validOp = True
        elif command[5] == '>=':
            if varList[command[4]] >= int(command[6]):
                validOp = True
        elif command[5] == '<=':
            if varList[command[4]] <= int(command[6]):
                validOp = True
        elif command[5] == '==':
            if varList[command[4]] == int(command[6]):
                validOp = True
        elif command[5] == '!=':
            if varList[command[4]] != int(command[6]):
                validOp = True
        
        if increase and validOp:
            varList[command[0]] += int(command[2])
        elif validOp:
            varList[command[0]] -= int(command[2])
        if varList[command[0]] > highestVal:
            highestVal = varList[command[0]]

print("Largest value at end: ", max(varList.values()))
print("Largest value during execution: ", highestVal)

