import sys

def findAllPaths(targetPort, ix, components):
    internalC = list(components)
    t = internalC.pop(ix)
    currStrength = sum(t)
    targetPort = t[1] if t[0] == targetPort else t[0]

    results = []
    for ix in range(len(internalC)):
        if internalC[ix][0] == targetPort or internalC[ix][1] == targetPort:
            results += findAllPaths(targetPort, ix, internalC)

    for l in results:
        l.append(currStrength)
    results.append([currStrength])

    return results

def findMaxStrength(targetPort, components):
    results = []
    for ix in range(len(components)):
        if components[ix][0] == targetPort or components[ix][1] == targetPort:
            results += findAllPaths(targetPort, ix, components)

    maxStrength = 0
    maxLength = 0
    for l in results:
        if len(l) > maxLength:
            maxLength = len(l)
            maxStrength = sum(l)
        elif len(l) == maxLength:
            maxStrength = max(sum(l), maxStrength)

    return maxStrength

if __name__ == '__main__':
    components = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            pair = line.strip().split("/")
            components.append((int(pair[0]), int(pair[1])))

    strength = findMaxStrength(0, components)
    print("strenght of bridge: ", strength)
