def heightAfterCycles(cycles):
    height = 1
    prev = 'summer'
    while cycles > 0:
        if prev == 'summer':
            height = height * 2
            prev = 'spring'
        else:
            height += 1
            prev = 'summer'
        cycles -= 1
    return height
        
T = int(raw_input())
cyclesList = []
while T > 0:
    cyclesList.append(int(raw_input()))
    T -= 1

for cycles in cyclesList:
    print heightAfterCycles(cycles)
