import sys
import re

def treeWeight(node):
    global treeData
    index = -1

    for i in range(len(treeData)):
        if treeData[i][0] == node:
            index = i
            break
    totalWeight = treeData[index][1]
    childWeights = list()
    for subNode in treeData[index][2]:
        childWeights.append(treeWeight(subNode))
    if not (len(set(childWeights)) <= 1):
        print(node, str(childWeights), totalWeight)
    childSum = sum(childWeights)
    totalWeight += childSum
    return totalWeight



progList = list()
with open(sys.argv[1]) as f:
    for line in f:
        progList.append(list(line.strip().replace(",", "").split()))


mainProgFinder = [x[0] for x in progList]

for lineList in progList:
    if len(lineList) > 3:
        for ix in range (3, len(lineList)):
            try:
                mainProgFinder.remove(lineList[ix])
            except ValueError:
                """print("Failed to remove: ", lineList[ix])"""
            else:
                """print("Remove: ", lineList[ix])"""

print(str(mainProgFinder))
treeData = list()

for l in progList:
    if len(l) > 3:
        treeData.append((l[0], int(re.search(r'\d+', l[1]).group()), l[3:]))
    else:
        treeData.append((l[0], int(re.search(r'\d+', l[1]).group()), list()))

print(treeWeight(str(mainProgFinder[0])))