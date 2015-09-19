def calculateContiguousSum(L):
        best_sum = 0
        current_sum = 0
        for ele in L:
                if current_sum + ele > 0:
                        current_sum += ele
                else:
                        current_sum = 0
                if current_sum > best_sum:
                        best_sum = current_sum
        return best_sum

def calculateNonContiguousSum(L):
        sum = 0
        for ele in L:
                if ele > 0:
                       sum += ele
        return sum

LT = []
T = int(raw_input())
while T > 0:
        n = int(raw_input())
        ar = [int(i) for i in raw_input().strip().split()]
        LT.append(list(ar))
        T -= 1

for L in LT:
        contiguousSum = calculateContiguousSum(L)
        nonContiguousSum = calculateNonContiguousSum(L)
        print contiguousSum, nonContiguousSum

