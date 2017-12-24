import sys

def findAllPaths(targetPort, ix, components):
    internalC = list(components)
    t = internalC.pop(ix)
    currStrength = t[0] + t[1]
    if t[0] == targetPort:
        targetPort = t[1]
    else:
        targetPort = t[0]

    possibleComps = []
    for i in range(len(internalC)):
        if internalC[i][0] == targetPort or internalC[i][1] == targetPort:
            possibleComps.append(i)

    results = []
    for ix in possibleComps:
        results += findAllPaths(targetPort, ix, internalC)
    results = list(map(lambda x:x+currStrength, results))

    if len(results) == 0:
        results.append(currStrength)

    return results

def findMaxStrength(targetPort, components):
    possibleComps = []
    for i in range(len(components)):
        if components[i][0] == targetPort or components[i][1] == targetPort:
            possibleComps.append(i)
    results = []
    for ix in possibleComps:
         results += findAllPaths(targetPort, ix, components)
    return max(results)

if __name__ == '__main__':
    components = []
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            pair = line.strip().split("/")
            components.append((int(pair[0]), int(pair[1])))

    strength = findMaxStrength(0, components)
    print("strenght of bridge: ", strength)









