# https://onlinejudge.org/external/101/10141.pdf

from sys import stdin

rfp = 0
while True:
    n, p = [int(x) for x in stdin.readline().split()]
    if n == 0 and p == 0:
        break
    rfp += 1
    low_proposal = ""
    max_compliance = 0
    proposals = {}
    for i in range(n):
        stdin.readline()
    for i in range(p):
        proposal = stdin.readline()
        dr = stdin.readline().split()
        d = float(dr[0])
        r = int(dr[1])
        for i in range(r):
            stdin.readline()
        compliance = r / n
        if compliance > max_compliance:
            max_compliance = compliance
            low_proposal = proposal
        if compliance not in proposals:
            proposals[compliance] = set()
        proposals[compliance].add((i, proposal, d))
    print("RFP #", rfp, sep="")
    print("--------------")
    print(len(proposals[max_compliance]))
    print(proposals[max_compliance])
    print(low_proposal)
