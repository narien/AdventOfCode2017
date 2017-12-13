import sys
import time

def moveScanner(firewall):
    for layer in firewall:
        if len(layer) > 0:
            pos = layer.index('S')
            layer[pos] = ''
            pos = (pos + 1) % len(layer)
            layer[pos] = 'S'

def resetScanner(firewall):
    for layer in firewall:
        if len(layer) > 0:
            for i in range(len(layer)):
                if i == 0:
                    layer[i] = 'S'
                else:
                    layer[i] = ''

firewall = list()
severity = 0
depth = 0
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        depthAndRange = line.replace(" ", "").strip().split(':')

        while len(firewall) < int(depthAndRange[0]):
            firewall.append(list())


        firewall.append([''] * (int(depthAndRange[1])*2 - 2))
        firewall[int(depthAndRange[0])][0] = 'S'
while depth < len(firewall):
    if len(firewall[depth]) > 0 and firewall[depth][0] == 'S':
        severity += depth*(len(firewall[depth]) - int((len(firewall[depth]) - 2)/2))
    moveScanner(firewall)
    depth += 1

print("severity: ", severity)
delay = 0
ok = False

while not ok:
    ok = True
    depth = 0
    delay += 1
    for layer in firewall:
        if len(layer) > 0:
            if (delay + depth)%len(layer)==0:
                ok = False
                break
        depth += 1

print("delay: ", delay)
