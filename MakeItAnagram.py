def howManyDeletionsRequiredToMakeTheseAnagram(s1, s2):
	s1Dict = getDictOfCharOccurrences(s1)
	s2Dict = getDictOfCharOccurrences(s2)
	if len(s1Dict) > len(s2Dict):
		return calculateDeletions(s1Dict, s2Dict)
	else:
		return calculateDeletions(s2Dict, s1Dict)
		
def calculateDeletions(big, small):
	numberOfDeletions = 0
	for c in big:
		if c not in small:
			numberOfDeletions += big[c]
		elif big[c] != small[c]:
			numberOfDeletions += abs(big[c] - small[c])
			
	for c in small:
		if c not in big:
			numberOfDeletions += small[c]
			
	return numberOfDeletions;		
	
def getDictOfCharOccurrences(s):
    dict = {}
    for c in s:
        if c in dict:
            dict[c] = dict[c] + 1
        else:
            dict[c] = 1
    return dict	

s1 = raw_input()
s2 =raw_input()

print howManyDeletionsRequiredToMakeTheseAnagram(s1, s2)