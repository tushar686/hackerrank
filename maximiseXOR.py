def maxXOR(L, R):
    l = L
    mx = 0
    while l <= R:
        r = L
        while r <= R:
            mx  = max(mx, l ^ r)    
            r += 1
        l += 1
    
    return mx
       
L = int(raw_input())
R = int(raw_input())
print maxXOR(L, R)
