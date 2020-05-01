# https://onlinejudge.org/external/115/11559.pdf

import sys

for data in sys.stdin:
    [N, B, H, W] = [int(x) for x in data.split()]
    minimum_cost = sys.maxsize
    for _ in range(H):
        price = int(input())
        avail = [int(x) for x in input().split()]
        if price * N <= B:
            for a in avail:
                if a >= N:
                    minimum_cost = min(minimum_cost, price * N)
                    break
    if minimum_cost < sys.maxsize:
        print(minimum_cost)
    else:
        print("stay home")

