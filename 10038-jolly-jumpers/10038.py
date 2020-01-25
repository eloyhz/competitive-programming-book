# 10038 - Jolly Jumpers
# https://onlinejudge.org/external/100/10038.pdf

from sys import stdin

for line in stdin:
    jolly = [int(i) for i in line.split()]
    n = jolly.pop(0)
    if n == 1:
        print("Jolly")
        continue
    s = set(range(1, n))
    for i in range(n - 1):
        a = abs(jolly[i] - jolly[i + 1])
        if a in s:
            s.remove(a)
    if len(s) == 0:
        print("Jolly")
    else:
        print("Not jolly")
