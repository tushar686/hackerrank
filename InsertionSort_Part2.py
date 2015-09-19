#!/bin/python
def insert_sort(ar, end):
    if end > len(ar)-1:
        return

    ele = ar[end]
    hole = end

    pos = end
    while pos > -1:
        if ele < ar[pos]:
            ar[pos+1] = ar[pos]
            hole = pos
        pos -= 1

    ar[hole] = ele
    printArr(ar)

    insert_sort(ar, end+1)    

def printArr(ar):
    for ele in ar:
        print ele,
    print

s = int(raw_input())
ar = [ int(ele) for ele in raw_input().split()]
insert_sort(ar, 1)
