import sys


def GenerateA(x):
    return Generate(x, 16807)

def GenerateB(x):
    return Generate(x, 48271)

def GeneratePartTwoA(x):
    x = Generate(x, 16807)
    while x % 4 != 0:
        x = Generate(x, 16807)
    return x

def GeneratePartTwoB(x):
    x = Generate(x, 48271)
    while x % 8 != 0:
        x = Generate(x, 48271)
    return x

def Generate(x, factor):
    return (x * factor) % 2147483647

def compareBinary(x, y):
    xBin = "{0:b}".format(x)[-16:]
    yBin = "{0:b}".format(y)[-16:]
    return xBin == yBin

def countMatchesPartOne(x, a, b):
    matches = 0
    for _ in range(x):
        a = GenerateA(a)
        b = GenerateB(b)
        if compareBinary(a, b):
            matches += 1
    return matches

def countMatchesPartTwo(x, a, b):
    matches = 0
    for _ in range(x):
        a = GeneratePartTwoA(a)
        b = GeneratePartTwoB(b)
        if compareBinary(a, b):
            matches += 1
    return matches




if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        a = int(f.readline().split()[4])
        b = int(f.readline().split()[4])
        if(sys.argv[3] == 1):
            print(countMatchesPartOne(int(sys.argv[2]), a, b))
        else:
            print(countMatchesPartTwo(int(sys.argv[2]), a, b))



