import sys
from collections import defaultdict

registerA = defaultdict(lambda:0)
registerB = defaultdict(lambda:0)
deadLockA = False
deadLockB = False
sndCounterB = 0
mailboxA = list()
mailboxB = list()


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def getVal(x, register):
    if isInt(x):
        return int(x)
    else:
        return register[x]

def runA(instr, pc):
    global registerA
    global deadLockA
    global mailboxA
    global mailboxB

    if deadLockA and len(mailboxA) > 0:
        deadLockA = False

    while not deadLockA and pc > -1 and pc < len(instr):
        if instr[pc][0] == 'snd':
            mailboxB.append(getVal(instr[pc][1], registerA))
        elif instr[pc][0] == 'set':
            registerA[instr[pc][1]] = getVal(instr[pc][2], registerA)
        elif instr[pc][0] == 'add':
            registerA[instr[pc][1]] = getVal(instr[pc][1], registerA) + getVal(instr[pc][2], registerA)
        elif instr[pc][0] == 'mul':
            registerA[instr[pc][1]] = getVal(instr[pc][1], registerA) * getVal(instr[pc][2], registerA)
        elif instr[pc][0] == 'mod':
            registerA[instr[pc][1]] = getVal(instr[pc][1], registerA) % getVal(instr[pc][2], registerA)
        elif instr[pc][0] == 'rcv':
            if len(mailboxA) == 0:
                deadLockA = True
                break
            else:
                registerA[instr[pc][1]] = mailboxA.pop(0)
        elif instr[pc][0] == 'jgz':
            if getVal(instr[pc][1], registerA) > 0:
                pc = pc + getVal(instr[pc][2], registerA) - 1
        else:
            print("SOMETHING WENT WRONG")
        pc += 1
    return pc

def runB(instr, pc):
    global registerB
    global deadLockB
    global mailboxA
    global mailboxB
    global sndCounterB

    if deadLockB and len(mailboxB) > 0:
        deadLockB = False

    while not deadLockB and pc > -1 and pc < len(instr):
        if instr[pc][0] == 'snd':
            sndCounterB += 1
            mailboxA.append(getVal(instr[pc][1], registerB))
        elif instr[pc][0] == 'set':
            registerB[instr[pc][1]] = getVal(instr[pc][2], registerB)
        elif instr[pc][0] == 'add':
            registerB[instr[pc][1]] = getVal(instr[pc][1], registerB) + getVal(instr[pc][2], registerB)
        elif instr[pc][0] == 'mul':
            registerB[instr[pc][1]] = getVal(instr[pc][1], registerB) * getVal(instr[pc][2], registerB)
        elif instr[pc][0] == 'mod':
            registerB[instr[pc][1]] = getVal(instr[pc][1], registerB) % getVal(instr[pc][2], registerB)
        elif instr[pc][0] == 'rcv':
            if len(mailboxB) == 0:
                deadLockB = True
                break
            else:
                registerB[instr[pc][1]] = mailboxB.pop(0)
        elif instr[pc][0] == 'jgz':
            if getVal(instr[pc][1], registerB) > 0:
                pc = pc + getVal(instr[pc][2], registerB) - 1
        else:
            print("SOMETHING WENT WRONG")
        pc += 1
    return pc


if __name__ == '__main__':
    instr = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            instr.append(line.strip().split())

    registerB['p'] = 1

    pcA = 0
    pcB = 0
    while not deadLockA or not deadLockB or len(mailboxA) > 0 or len(mailboxB) > 0:
        pcA = runA(instr, pcA)
        pcB = runB(instr, pcB)
    print("sndCounterB = ", sndCounterB)










