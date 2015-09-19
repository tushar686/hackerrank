import math

def findNumberOfPerfectSquresBetween(ab):
    a = ab[0]
    b = ab[1]
    
    a_sqrt = int(math.ceil(math.sqrt(ab[0])))
    b_sqrt = int(math.floor(math.sqrt(ab[1])))

    count_of_perfect_square = 0

    for x in range(a_sqrt, b_sqrt+1):
        x_sq = math.pow(x, 2)
        if x_sq >= a or x_sq <= b:
            count_of_perfect_square += 1
    
    return count_of_perfect_square

if __name__ == '__main__':
    T = input()
    abs = []
    while T > 0:
        ab = [int(ele) for ele in raw_input().split()]
        abs.append(ab)
        T -= 1

    for ab in abs:
        print findNumberOfPerfectSquresBetween(ab)
