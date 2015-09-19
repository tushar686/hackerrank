import math

def calculatePossibleWays(L):
        l0 = int(L[0])
        l1 = int(L[1])

        n = l0 + l1
        r = l0
        ans = math.factorial(n) / ( math.factorial(r) * math.factorial(n-r) )
        return ans % 1000000007

LT = []
T = int(raw_input())
while T > 0:
        ar = [i for i in raw_input().strip().split()]
        LT.append(list(ar))
        T -= 1

for L in LT:
       print calculatePossibleWays(L)
