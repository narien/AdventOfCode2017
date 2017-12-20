import sys

def updateVelocity(particleBuffer):
    for particle in particleBuffer:
        particle[5] += particle[9]
        particle[6] += particle[10]
        particle[7] += particle[11]

def updatePosition(particleBuffer):
    for particle in particleBuffer:
        particle[1] += particle[5]
        particle[2] += particle[6]
        particle[3] += particle[7]

def updateBuffer(particleBuffer):
    updateVelocity(particleBuffer)
    updatePosition(particleBuffer)

def findClosestparticle(particleBuffer):
    minIncrease = sys.maxsize
    particleId = -1
    for i in range(len(particleBuffer)):
        change = abs(particleBuffer[i][9]) + abs(particleBuffer[i][10]) + abs(particleBuffer[i][11])
        if change < minIncrease:
            particleId = i
            minIncrease = change
    return particleId

def compareparticle(particleA, particleB):
    return particleA[1:4] == particleB[1:4]

def findCollisions(particleBuffer):
    collisionIndexes = list()

    for i in range(len(particleBuffer)):
        for j in range(len(particleBuffer)):
            if i not in collisionIndexes and i != j and compareparticle(particleBuffer[i], particleBuffer[j]):
                collisionIndexes.append(i) #Only add one of the destroyed particles, the other one will be added later
    return sorted(collisionIndexes)

def removeCollisions(particleBuffer, collisions):
    while len(collisions) > 0:
        particleBuffer.pop(collisions.pop())

if __name__ == '__main__':
    particleBuffer = list()
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            particleBuffer.append(line.replace("=<", ",").replace(">, ",",").replace(">", "").strip().split(","))

        for particle in particleBuffer:
            particle[1] = int(particle[1])
            particle[2] = int(particle[2])
            particle[3] = int(particle[3])
            particle[5] = int(particle[5])
            particle[6] = int(particle[6])
            particle[7] = int(particle[7])
            particle[9] = int(particle[9])
            particle[10] = int(particle[10])
            particle[11] = int(particle[11])

    print("closest particle is: ", findClosestparticle(particleBuffer))

    for _ in range(100):
        collisions = findCollisions(particleBuffer)
        removeCollisions(particleBuffer, collisions)
        updateBuffer(particleBuffer)
    print("Particles still alive: ", len(particleBuffer))







