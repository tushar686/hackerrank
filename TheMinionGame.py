def evaluateSuffixes(s):
	vowles = ['A','E','I','O','U']
	vowelsSuffix = 0
	consonantsSuffix = 0
	for currentIndex in range(0, len(s)):
		if len(s[currentIndex]) > 0:
			if s[currentIndex] in vowles:
				vowelsSuffix += len(s) - currentIndex
			else:
				consonantsSuffix += len(s) - currentIndex
			
	if vowelsSuffix > consonantsSuffix:
		print 'Kevin ' +  str(vowelsSuffix)
	if consonantsSuffix > vowelsSuffix:
		print 'Stuart ' +  str(consonantsSuffix)
	if consonantsSuffix == vowelsSuffix:
		print 'Draw'
				
       

S = raw_input()
evaluateSuffixes(S)