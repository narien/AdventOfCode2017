import sys

mode = sys.argv[2]
with open(sys.argv[1]) as f:
    instr = list(map(int, f.read().splitlines()))

currPos = 0
iterations = 0
while currPos < len(instr) and currPos >= 0:
    nextJump = instr[currPos]
    if mode == '2' and nextJump >= 3:
        instr[currPos] += -1
    else:
        instr[currPos] += 1
    currPos += nextJump
    iterations += 1

print("Steps taken: ", iterations)