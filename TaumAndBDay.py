def findMinimumGiftAmount(BW, XYZ):
    x  = XYZ[0]
    y  = XYZ[1]
    z  = XYZ[2]

    b = BW[0]
    w = BW[1]
    
    if z < x or z < y:
        return calculateCost(x, y, z, b, w)
    else:
        return b * x + w * y

def calculateCost(x, y, z, b, w):
    baseCost = 0
    exchangeCost = 0
    if min(x, y) == x:
        baseCost = b * x
        exchangeCost = calculateExchangeCost(w, y, x, z)
    else:
        baseCost = w * y
        exchangeCost = calculateExchangeCost(b, x, y, z)
    return baseCost + exchangeCost

def calculateExchangeCost(quantity, orignalCost, minCost, exchangeCost):
    normalCost = quantity * orignalCost
    convertedCost = (quantity * minCost) + (quantity * exchangeCost)
    if convertedCost < normalCost:
        return convertedCost
    else:
        return normalCost
    
    

T = input()

LT = []
while T > 0:
    BW = [int(ele) for ele in raw_input().split()]
    XYZ = [int(ele) for ele in raw_input().split()]
    LT.append(BW)
    LT.append(XYZ)
    T -= 1

while T < len(LT):
    print findMinimumGiftAmount(LT[T], LT[T+1])
    T += 2
