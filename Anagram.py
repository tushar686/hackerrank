def numberOfChangeRequiredToMakeAnagram(test):
    if isOddLengthStringWhichCannotBeMadeAnagram(test):
        return -1
    else:
        return howManyChangesRequired(test)

def howManyChangesRequired(test):
    s1 = test[0:len(test)/2]
    s2 = test[len(test)/2:]
    s1CharOccurrences = getDictOfCharOccurrences(s1)
    s2CharOccurrences = getDictOfCharOccurrences(s2)

    numberOfChangesRequired = 0
    for c in s2CharOccurrences:
        if c not in s1:
            numberOfChangesRequired += s2CharOccurrences[c]
        else:
            if (s2CharOccurrences[c] - s1.count(c)) > 0:
                numberOfChangesRequired += s2CharOccurrences[c] - s1.count(c)
            
    return numberOfChangesRequired

def getDictOfCharOccurrences(s):
    dict = {}
    for c in s:
        if c in dict:
            dict[c] = dict[c] + 1
        else:
            dict[c] = 1
    return dict    


def isOddLengthStringWhichCannotBeMadeAnagram(test):
    if len(test) % 2 != 0:
        return True
    return False

t = int(raw_input())
tests = []
while t > 0:
    tests.append(raw_input())
    t-=1
for test in tests:
    print numberOfChangeRequiredToMakeAnagram(test)
