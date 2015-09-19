#!/usr/bin/py
def lonelyinteger(a):
    a.sort()
    idx = 0
    for ele in a[::2]:
        if idx + 1 > len(a)-1 or ele != a[idx + 1]:
            return ele
        idx += 2

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
