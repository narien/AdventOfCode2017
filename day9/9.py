import sys

nestingScore = 0
currNesting = 0
inGarbage = False
garbageCount = 0
with open(sys.argv[1]) as f:
    while True:
        c = f.read(1)
        if not c:
            print ("total nesting score: ", nestingScore, " GarbageCount: ", garbageCount)
            break
        if c == '!' and inGarbage:
            f.read(1)
        elif c == '<':
            if inGarbage: garbageCount += 1
            inGarbage = True
        elif c == '>':
            inGarbage = False
        elif c == '{' and not inGarbage:
            currNesting += 1
            nestingScore += currNesting
        elif c == '}' and not inGarbage:
            currNesting -= 1
        elif inGarbage:
            garbageCount += 1

