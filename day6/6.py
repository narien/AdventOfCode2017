import sys

with open(sys.argv[1]) as f:
    mem = list(map(int, f.readline().split()))

prevMems = list()
prevMems.append(str(mem))
while True:
    index = mem.index(max(mem))
    blocks = mem[index]
    mem[index] = 0
    while blocks != 0:
        index = (index + 1) % len(mem)
        mem[index] += 1
        blocks -= 1
    if str(mem) in prevMems:
        break
    else:
        prevMems.append(str(mem))
print("iterations: ", len(prevMems))
print("loop size: ", len(prevMems) - prevMems.index(str(mem)))
