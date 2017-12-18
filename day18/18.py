import sys
from collections import defaultdict

lastSound = 0
register = defaultdict(lambda:0)

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def getVal(x):
    global register
    if isInt(x):
        return int(x)
    else:
        return register[x]

def run(instr):
    global lastSound
    global register
    lastSound = 0
    register = defaultdict(lambda:0)

    i = 0
    while i > -1 and i < len(instr):
        if instr[i][0] == 'snd':
            lastSound = getVal(instr[i][1])
        elif instr[i][0] == 'set':
            register[instr[i][1]] = getVal(instr[i][2])
        elif instr[i][0] == 'add':
            register[instr[i][1]] = getVal(instr[i][1]) + getVal(instr[i][2])
        elif instr[i][0] == 'mul':
            register[instr[i][1]] = getVal(instr[i][1]) * getVal(instr[i][2])
        elif instr[i][0] == 'mod':
            register[instr[i][1]] = getVal(instr[i][1]) % getVal(instr[i][2])
        elif instr[i][0] == 'rcv':
            if getVal(instr[i][1]) != 0:
                print("Last value played: ", lastSound)
                break
        elif instr[i][0] == 'jgz':
            if getVal(instr[i][1]) != 0:
                i = i + getVal(instr[i][2]) - 1
        else:
            print("SOMETHING WENT WRONG")
        i += 1


if __name__ == '__main__':
    instr = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            instr.append(line.strip().split())
    run(instr)






