#!/usr/bin/py

def numberOfDigitsWhichAreFactorsOf(N):
    digitsCountDict = hashDigits(N)
    count = 0
    for ele in digitsCountDict:
        count += digitsCountDict[ele]
    return count

def hashDigits(N):
    dict = {}
    for ele in str(N):
        if ele != '0' and ele not in dict:
            if N % int(ele) == 0:
                dict[ele] = str(N).count(ele)
    return dict
        

if __name__ == '__main__':
    T = input()
    Ns = []
    while T > 0:
        Ns.append(input())
        T -= 1

    for N in Ns:
        print numberOfDigitsWhichAreFactorsOf(N)
    
