#!/usr/bin/py
from sets import Set

def howManyMaxPeices(k):
    return (k-k/2) * (k/2)

if __name__ == '__main__':
    T = input()
    k = []
    while T > 0:
        k.append(input())
        T -= 1

    for cut in k:
        print howManyMaxPeices(cut)
    
