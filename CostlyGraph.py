import math
import itertools

def findCost(L):
    N = L[0]
    K = L[1]

    maxEdgesInTheGraph = calculateMaxEdgesInTheGraph(N)

    allcomb = generateCombinationsOfPossibleDeegreSequences(N)
    graphicalComb = filterValidGraphicalCombinations(allcomb)

    cost = 0
    for comb in graphicalComb:
        edgesInThisGraph = getEdges(comb)
        numberOfGraphs = numberOfGraphsCanBeFormedWithREdges(edgesInThisGraph, maxEdgesInTheGraph)
        cost += calculateCostOfTheseGraphs(numberOfGraphs, comb, K)    
    return int(cost % 1005060097)

def calculateCostOfTheseGraphs(numberOfGraphs, comb, K):
    cost = 0
    for degree in comb:
        cost += int(math.pow(degree, K))
    #print comb, cost, numberOfGraphs
    return cost * numberOfGraphs

def numberOfGraphsCanBeFormedWithREdges(R, totalEdges):
    return math.factorial(totalEdges) / (math.factorial(R) * math.factorial(totalEdges-R))

def getEdges(comb):
    sumOfDegrees = sum(comb)
    #sum of degrees of all vertices is atmost 2 times # Edges
    E = sumOfDegrees / 2
    return E
    

def calculateMaxEdgesInTheGraph(N):
    maxDegree = N-1
    sumOfDegrees = maxDegree * N
    #sum of degrees of all vertices is atmost 2 times # Edges
    E = sumOfDegrees / 2

    return E
    
    
def filterValidGraphicalCombinations(comb):
    graphicalComb = []
    for seq in comb:
        if isGivenDegreeSequnceGraphical(sorted(seq, reverse=True)):
            graphicalComb.append(seq)
    return graphicalComb
    

def isGivenDegreeSequnceGraphical(seq):
    if len(seq) == 1:
        if seq[0] == 0:
            return True
        return False
    first = seq[0]

    newSeq = []
    eleIdx = 1
    while first > 0:
        newSeq.append(seq[eleIdx]-1)
        eleIdx += 1
        first -= 1

    if eleIdx <= len(seq):
        newSeq = newSeq + seq[eleIdx:]
    return isGivenDegreeSequnceGraphical( sorted(newSeq, reverse=True) )    

def generateCombinationsOfPossibleDeegreSequences(N):
    degreeSequences = []
    maxDegree = N-1
    digits = range(0, maxDegree+1)    
    r = maxPossibleCombinations(len(digits), len(digits))
    comb = combinationsWithRepetitions(digits, len(digits))
    return comb

def maxPossibleCombinations(n, r):
    return math.factorial(n+r-1) / ( math.factorial(r) * math.factorial(n-1) )

def combinationsWithRepetitions(digits, r):
   return list(itertools.combinations_with_replacement(digits,r))


LT = []
T = int(raw_input())
while T > 0:
    LT.append([ int(ele) for ele in raw_input().split()])
    T -=1

for L in LT:
    print findCost(L)
