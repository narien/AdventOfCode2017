import sys

def rotate(x, y, affectedNodes, direction):
    if (x, y) in affectedNodes.keys():
        if affectedNodes[(x, y)] == 0:
            return direction
        elif affectedNodes[(x, y)] == 1:
            return (direction + 1) % 4
        elif affectedNodes[(x, y)] == 2:
            return (direction + 2) % 4
    else:
        return (direction - 1) % 4

def changeState(x, y, affectedNodes):
    if (x, y) in affectedNodes.keys():
        if affectedNodes[(x, y)] == 0:
            affectedNodes[(x, y)] = 1
            return 1
        elif affectedNodes[(x, y)] == 1:
            affectedNodes[(x, y)] = 2
            return 0
        elif affectedNodes[(x, y)] == 2:
            affectedNodes.pop((x, y))
            return 0
    else:
        affectedNodes[(x, y)] = 0
        return 0

if __name__ == '__main__':
    affectedNodes = dict() # 0 = weakened, 1 = infected, 2 = flagged
    x = 0
    y = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            for c in line:
                if c == "#":
                    affectedNodes[(x, y)] = 1
                x += 1
            x = 0
            y -= 1
    x = 12
    y = -12
    direction = 0 # 0 = up, 1 = right, 2 = down, 3 = left
    newInfected = 0
    for _ in range(int(sys.argv[2])):
        direction = rotate(x, y, affectedNodes, direction)
        newInfected += changeState(x, y, affectedNodes)
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        else:
            x -= 1
    print("Nbr of newly infected: ", newInfected)