string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

if len(string) % 2 == 0:
    print("NO")
else:
    dict = {}
    for c in string:
        try:
            dict[c] = dict[c] + 1
        except KeyError:
            dict[c] = 1
    
    unsymmetricChar = 0
    for c in dict:
        if dict[c] % 2 != 0:
            unsymmetricChar += 1
    if unsymmetricChar > 1:    
        print("NO")
    else:    
        found = True        
        print("YES")
  