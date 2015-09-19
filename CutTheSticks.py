#!/usr/bin/py
def findNumberofAticksInACut(sticks):
    print len(sticks)
    minLength = min(sticks)
    newSticks = []
    for length in sticks:
        if length - minLength != 0:
            newSticks.append(length - minLength)
    if len(newSticks) != 0:
        findNumberofAticksInACut(newSticks)
    
if __name__ == '__main__':
    N = input()
    sticks = map(int, raw_input().strip().split(" "))
    findNumberofAticksInACut(sticks)
