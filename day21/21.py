import sys
from numpy import *

def addAllVariantsToRules(rules, rule):
    m = list(map(list, rule[0].split("/")))
    for i in range(4):
        m = list(zip(*m[::-1]))
        s = ""
        for l in m:
            s += "".join(l)
        rules[s] = rule[1]
        m2 = list(m)
        for i in range(len(m2)):
            m2[i] = m2[i][::-1]
        s = ""
        for l in m2:
            s += "".join(l)
        rules[s] = rule[1]

def generate(oldArt, rules):
    subSize = 2 if len(oldArt) % 2 == 0 else 3
    newSubSize = subSize + 1

    sideSubM = int(len(oldArt) / subSize)
    result = empty(shape=[newSubSize*sideSubM, newSubSize*sideSubM], dtype='S1')
    for i in range(sideSubM):
        for j in range(sideSubM):
            subM = oldArt[i*subSize:subSize + i*subSize, j*subSize:subSize + j*subSize]
            s = ""
            for l in subM:
                for c in l:
                    s += c.decode('UTF-8')
            substitute = rules[s]
            substitute = substitute.split("/")
            newM = empty(shape=[newSubSize, newSubSize], dtype='S1')
            for i2 in range(len(substitute)):
                for j2 in range(len(substitute)):
                    newM[i2][j2] = substitute[i2][j2]
            result[i*newSubSize:(i+1)*newSubSize, j*newSubSize:(j+1)*newSubSize] = newM

    return result


if __name__ == '__main__':
    rules = dict()
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            rule = line.replace("=> ", "").strip().split()
            addAllVariantsToRules(rules, rule)
    currArt = array([[".", "#", "."],[".", ".", "#"],["#", "#", "#"]],dtype='S1')
    for _ in range(int(sys.argv[2])):
        currArt = generate(currArt, rules)

    pixelsOn = 0
    for i in range(len(currArt)):
        for j in range(len(currArt)):
            if currArt[i][j] == b'#': pixelsOn += 1
    print(pixelsOn)






