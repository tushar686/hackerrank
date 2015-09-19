import math

def calculateHandShakes(persons):
        if persons < 2:
                return 0
        if persons == 2:
                return 1
        
        if persons > 2:
                return math.factorial(persons)/(math.factorial(2)*math.factorial(persons-2))

LT = []
T = int(raw_input())
while T > 0:
        LT.append(int(raw_input()))
        T -= 1

for persons in LT:
        print calculateHandShakes(persons)
