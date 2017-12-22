import sys

def rotate(x, y, infectedNodes, direction):
    if (x, y) in infectedNodes.keys():
        #print("found infected")
        direction = (direction + 1) % 4
    else:
        #print("uninfected")
        direction = (direction - 1) % 4
    return direction

def tryInfect(x, y, infectedNodes):
    if (x, y) in infectedNodes.keys():
        infectedNodes.pop((x, y))
        return 0
    else:
        infectedNodes[(x, y)] = True
        return 1


if __name__ == '__main__':
    infectedNodes = dict()
    x = 0
    y = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            for c in line:
                if c == "#":
                    infectedNodes[(x, y)] = True
                x += 1
            x = 0
            y -= 1
    x = 12
    y = -12
    direction = 0 # 0 = up, 1 = right, 2 = down, 3 = left
    newInfected = 0
    for _ in range(int(sys.argv[2])):
        direction = rotate(x, y, infectedNodes, direction)
        newInfected += tryInfect(x, y, infectedNodes)
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        else:
            x -= 1
    print("Nbr of newly infected: ", newInfected)







