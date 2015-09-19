#!/bin/python
def insertionSort(ar):
    ar = findCorrectPlace(ar, len(ar)-2, ar[len(ar)-1])
    printArray(ar)

def findCorrectPlace(ar, place, ele):
        if ar[place] <= ele or place == -1:
                ar[place+1] = ele
                return ar
        else:
                ar[place+1] = ar[place]
                printArray(ar)
                return findCorrectPlace(ar, place-1, ele)

def printArray(ar):
        for ele in ar:
                print ele,
        print
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
