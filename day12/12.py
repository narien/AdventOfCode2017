import sys

def findGroup(currNode):
    global nodeTree
    global nodes
    nodes.add(currNode)

    for node in nodeTree[currNode]:
        if node not in nodes:
            findGroup(node)

nodeTree = dict()
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        nodeList = line.replace(",", "").strip().split()
        nodeTree[nodeList[0]] = nodeList[2:]
nodes = set()
findGroup('0')
print(len(nodes))
groups = 1

for key in nodeTree:
    old = len(nodes)
    findGroup(key)
    if len(nodes) != old:
        groups += 1

print("amount of groups: ", groups)






