import sys
from collections import defaultdict

mulUses = 0


def getVal(s):
    global register
    try: 
        return int(s)
    except ValueError:
        return register[s]

def run(instr):
    global mulUses
    global register
    mulUses = 0

    i = 0
    while i > -1 and i < len(instr):
        if instr[i][0] == 'set':
            register[instr[i][1]] = getVal(instr[i][2])
        elif instr[i][0] == 'sub':
            register[instr[i][1]] = getVal(instr[i][1]) - getVal(instr[i][2])
        elif instr[i][0] == 'mul':
            register[instr[i][1]] = getVal(instr[i][1]) * getVal(instr[i][2])
            mulUses += 1
        elif instr[i][0] == 'jnz':
            if getVal(instr[i][1]) != 0:
                i = i + getVal(instr[i][2]) - 1
        else:
            print("SOMETHING WENT WRONG")
        i += 1

#Not my solution
def run2():
    h = 0
    b = 65
    c = b
    b = b * 100
    b = b + 100000
    c = b + 17000

    while True:  # E
        f = 1
        d = 2
        e = 2

        while True:  # B
            if b % d == 0:
                f = 0
            d = d + 1
            if d != b:
                continue
            if f == 0:
                h = h + 1
            if b == c:
                return(h)
            b = b + 17
            break

if __name__ == '__main__':
    instr = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            instr.append(line.strip().split())
    register = defaultdict(lambda:0)
    run(instr)
    print("mul used: ", mulUses)
    print(run2())







