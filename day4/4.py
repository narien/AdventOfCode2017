import sys
from collections import Counter

def is_anagram(w1, w2):
    w1, w2 = list(w1), list(w2)
    w1.sort()
    w2.sort()
    return w1 == w2


file = open(sys.argv[1])
goodPasswords = 0
for line in file:
    containsAnagram = False
    myList = line.split()
    if sys.argv[2] == 1:
        c = Counter(myList)
        if max(c.values()) <= 1:
            goodPasswords += 1
    else:
        for i in range(len(myList)):
            for j in range(len(myList)):
                if i != j and is_anagram(myList[i], myList[j]):
                    containsAnagram = True
                    print("current word: ", myList[i], myList[j], containsAnagram)
    if not containsAnagram:
        goodPasswords += 1 

print("good passwords: ", goodPasswords)
