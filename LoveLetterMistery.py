def findMinOperations(string):
    first = string[:len(string)/2]
    second = string[len(string)/2+1:] if len(string) % 2 != 0 else string[len(string)/2:]

    min = 0
    for zipped in zip(first, reversed(second)):
        min += howManyChangesRequiredToMakePalindrome(zipped)
    return min

def howManyChangesRequiredToMakePalindrome(zipped):
    if ord(zipped[0]) > ord(zipped[1]):
        return ord(zipped[0]) - ord(zipped[1])
    return ord(zipped[1]) - ord(zipped[0])
    
T = int( raw_input() )

LT = []
while T > 0:
    LT.append(raw_input())
    T -= 1

for string in LT:
    print findMinOperations(string)
