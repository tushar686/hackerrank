def buildSuffixTries(s):
	suffixTries = [[],[]]
	for currentIndex in range(0, len(s)):
		for currentSubIndex in range(currentIndex, len(s)+1):	
			suffix = s[currentIndex: currentSubIndex]
			if len(suffix) > 0:
				if suffix in suffixTries[0]:
					suffixTries[1][suffixTries[0].index(suffix)] += 1
				else:
					suffixTries[0].append(suffix)
					suffixTries[1].append(1)

	return suffixTries
       

S = raw_input()
suffixTries = buildSuffixTries(S)

print suffixTries