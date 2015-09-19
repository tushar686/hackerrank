import itertools

def manasaStonesSerries(nab):
    n = nab[0]
    a = nab[1]
    b = nab[2]
    cseries = combinationsWithRepetitions([a, b], n-1)
    allSeries = []
    for cseriesI in cseries:
        series = [0]
        for ele in cseriesI:
            series.append(series[len(series)-1] + ele)
        allSeries.append(series)
    
    printSeries(allSeries)

def printSeries(series):
    sortedSeries = []
    for ele in series:
        sortedSeries.append(ele[len(ele)-1])
    prevEle = -100
    for ele in sorted(sortedSeries):
        if prevEle != ele:
            print ele,
        prevEle = ele
    print

def combinationsWithRepetitions(ab, r):
   return list(itertools.combinations_with_replacement(ab,r))


if __name__ == '__main__':
    T = input()
    nabs = []
    while T > 0:
        nab = []
        nab.append(input())
        nab.append(input())
        nab.append(input())
        nabs.append(nab)
        T -= 1

    for nab in nabs:
        manasaStonesSerries(nab)
