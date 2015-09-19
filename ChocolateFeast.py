
def getChocolatesForMoney(rs, costOfOneChocolates):
    return int(rs) / costOfOneChocolates

def getChocolatesForWrapper(numberOfWrappers, wrappersRequiredForOneChocolate):
    return numberOfWrappers / wrappersRequiredForOneChocolate

def getTotalChocolatesForWrappers(numberOfWrappers, wrappersRequiredForOneChocolate):
    chocolatesForWrapper = 0
    while numberOfWrappers >= wrappersRequiredForOneChocolate:
        exaggerateWrappers = numberOfWrappers % wrappersRequiredForOneChocolate
        exactWrappersForChocolate = numberOfWrappers - exaggerateWrappers
        chocolates = getChocolatesForWrapper(exactWrappersForChocolate, wrappersRequiredForOneChocolate)
        chocolatesForWrapper = chocolatesForWrapper + chocolates
        numberOfWrappers = chocolates + exaggerateWrappers        
    return chocolatesForWrapper

T = input()
NCM = []
while T > 0:
    NCM.append( [int(ele) for ele in raw_input().split()] )
    T -= 1

for ncm in NCM:
    chocolatesThroughMoney = getChocolatesForMoney(ncm[0], ncm[1])
    chocolatesThroughWrapper = getTotalChocolatesForWrappers(chocolatesThroughMoney, ncm[2])
    print chocolatesThroughMoney + chocolatesThroughWrapper
