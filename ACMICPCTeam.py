def findMaxNumberOfTeamAndTopics(LT):
    N = len(LT)
    totalTeamsKnowMaxTopics = 0
    maxKnownTopics = 0

    me = 0
    while me < N:
        he = me+1
        while he < N:
            if me != he:
                maxTopicsWeKnow = howManyMaxTopicsWeKnow(LT[me], LT[he])
                if maxTopicsWeKnow == maxKnownTopics:
                    totalTeamsKnowMaxTopics += 1
                elif maxTopicsWeKnow > maxKnownTopics:
                    totalTeamsKnowMaxTopics = 1
                    maxKnownTopics = maxTopicsWeKnow
            he += 1
        me += 1

    print maxKnownTopics
    print totalTeamsKnowMaxTopics

def howManyMaxTopicsWeKnow(myTopics, hisTopics):
    maxTopicsWeKnow = myTopics | hisTopics
    return str(bin(maxTopicsWeKnow)[2:]).count('1')
    
    
NM = [int(ele) for ele in raw_input().split()]
N = NM[0]
M = NM[1]

LT = []
while N > 0:
    LT.append(int(raw_input(), 2))
    N -= 1
findMaxNumberOfTeamAndTopics(LT)
