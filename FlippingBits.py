import struct

def invertBit(b):
    if b == '0':
        return 1
    else:
        return 0

def flipbits(L):
    binL = tuple(bin(L)[2:].zfill(32))
    binFlippedL = []
    for bit in binL:
        binFlippedL.append(invertBit(bit))
    return binFlippedL

def toDec(flippedL):
    binary = ""
    for bit in flippedL:
        binary = binary + str(bit)
    return int(binary, 2)

LT = []
T = int(raw_input())
while T > 0:
        LT.append(int(raw_input()))
        T-=1

for L in LT:
        flippedL = flipbits(L)
        print toDec(flippedL)
