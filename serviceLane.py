def maxVehicalTypeCanPassThroughEntryExit(ij, width):
    minSegmentWidth = 999
    while ij[0] <= ij[1]:
        minSegmentWidth = min(minSegmentWidth, width[ij[0]])
        ij[0] += 1

    return minSegmentWidth
    
def getMaxWidthPossible(ij):
    maxEntry = width[ ij[0] ]
    maxExit = width[ ij[1]]
    return min(maxEntry, maxExit)

_NT = [int(ele) for ele in raw_input().split()]
_width = [int(ele) for ele in raw_input().split()]

entryExit = []
while _NT[1] > 0:
    entryExit.append([int(ele) for ele in raw_input().split()])
    _NT[1] -= 1

for ij in entryExit:
    print maxVehicalTypeCanPassThroughEntryExit(ij, _width)
