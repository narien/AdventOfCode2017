import sys

if __name__ == '__main__':
    steps = 312
    spinlockBuffer = [0]
    currPos = 0
    for i in range(1, 2018):
        spinlockBuffer.insert((currPos + steps + 1) % len(spinlockBuffer), i)
        currPos = spinlockBuffer.index(i)

    print("Value after value 2017: ", spinlockBuffer[(spinlockBuffer.index(2017) + 1) % len(spinlockBuffer)])

    valAfterZero = 0
    currPos = 0
    for i in range(1, 50000001):
        currPos = (currPos + steps) % i
        if  currPos == 0:
            valAfterZero = i
        currPos = (currPos + 1) % i

    print("Value to stop spinlock: ", valAfterZero)