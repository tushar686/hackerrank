#!/usr/bin/py

def isClassCancelled(arrival, K):
    studentsArrivedBeforeClassStarts = sum(ele <= 0 for ele in arrival)
    if studentsArrivedBeforeClassStarts < K:
        return 'YES'
    return 'NO'
    
if __name__ == '__main__':
    T = input()
    nk = []
    arrival = []
    while T > 0:
        nk.append(map(int, raw_input().strip().split(" ")))
        arrival.append(map(int, raw_input().strip().split(" ")))
        T -= 1

    for idx, ele in enumerate(nk):
        print isClassCancelled(arrival[idx] , ele[1])
    
