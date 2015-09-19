import sys

def printCavity(map, N):
    row = 1
    col = 1
    while col < N:
        cavityValue = map[row][col]
        if cavityValue > map[row-1][col] and cavityValue > map[row+1][col] and cavityValue > map[row][col-1] and cavityValue > map[row][col+1]:
            map[row][col] = 'X'
        row += 1
        if row == N:
            row = 1
            col += 1
        if col == N:
            return

if __name__ == '__main__':
    N = input()
    map = []
    T = N
    while T > 0:
        row = raw_input()
        rowL = []
        for ele in str(row):
            rowL.append(ele)    
        map.append(rowL)
        T -= 1

    printCavity(map, N-1)
    for row in range(0, N):
        for col in range(0, N):
            sys.stdout.write(map[row][col])
        print
    
