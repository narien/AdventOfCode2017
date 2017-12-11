import sys

def dist(x1, y1):
    return max(abs(x1), abs(y1), abs(x1-y1))

x = 0
y = 0
maxDist = 0

with open(sys.argv[1], 'r') as f:
    path = f.readline().replace(" ", "").strip().split(",")

for step in path:   
    if step == "n":
        y += 1
    elif step == "ne":
        y += 1
        x += 1
    elif step == "se":
        x += 1
    elif step == "s":
        y -= 1
    elif step == "sw":
        y -= 1
        x -= 1
    elif step == "nw":
        x -= 1
    newDist = dist(x,y)
    if newDist > maxDist:
        maxDist = newDist

print("Last dist: ", dist(x, y))
print("Max dist: ", maxDist)




