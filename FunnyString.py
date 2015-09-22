accumulateDiff = 0

def formTheDifferentialString(s):
	differentialString = [];
	for c in s:
		differentialString.append(abs(currentMinusLastChar(c, s)))
	return differentialString	

def currentMinusLastChar(c, s):
	diff = ord(c) - asciiOfLastChar(s)
	accumulateDifference(diff)
	return diff

def accumulateDifference(diff):
	global accumulateDiff
	accumulateDiff += diff

def asciiOfLastChar(s):
	return ord(s[0]) + accumulateDiff

N = int(raw_input())
S = []
while N > 0:
	S.append(raw_input())
	N -= 1

for s in S:
	sDifferential = formTheDifferentialString(s)[1:]
	rDifferential = formTheDifferentialString(s[::-1])[1:]
	print 'Funny' if sDifferential == rDifferential else 'Not Funny'
