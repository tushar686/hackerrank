import math

def findPos(v, ar, start, end):
	mid = int(math.floor((end-start)/2))
	if v == ar[start + mid]:
        	return start + mid
        else:
                if v < ar[start + mid]:
			firstHalf = ar[start:start+mid]
			return findPos(v, ar, start, mid)
		else:
			secondHalf = ar[start+mid:]
			return findPos(v, ar, start + mid, end)

v = int(raw_input())
n = int(raw_input())
numbers = raw_input()
ar = map(int, numbers.split())
print findPos(v, ar, 0, n)