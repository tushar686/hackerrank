import sys

def buildList(L):
        L = sorted(L[0])
        for idx, ele in enumerate(L):
                printTopPart(L[idx:])
                printBottomPart(L, idx)


def printTopPart(L):
        topPart = [L[0]]
        topI = 1
        while topI < len(L):
                topPart.append(str(topPart[len(topPart)-1]) + L[topI])
                topI += 1
        for ele in topPart:
                print ele

def printBottomPart(L, idx):
        bottomPart = []
        dropIndexStart = 2
        
        bottomStart = idx + dropIndexStart
        bottomEnd = len(L)
        while bottomStart < bottomEnd:

                while bottomStart < bottomEnd:
                        bottomPartSubList = [L[idx]]
                        for ele in range(bottomStart, bottomEnd):
                                bottomPartSubList.append(L[ele])
                        bottomPart.append(bottomPartSubList[:])
                        bottomEnd -= 1
                        
                dropIndexStart += 1
                bottomStart = idx + dropIndexStart
                bottomEnd = len(L)
                        
                
        for ele in bottomPart:
                for subEle in ele:
                        sys.stdout.write(subEle)
                print

LT = []
T = int(raw_input())
while T > 0:
        n = int(raw_input())
        ar = [i for i in raw_input().strip().split()]
        LT.append(list(ar))
        T -= 1

for L in LT:
        buildList(L)
