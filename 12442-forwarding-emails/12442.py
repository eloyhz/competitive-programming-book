# 12442 Forwarding Emails
# https://onlinejudge.org/external/124/12442.pdf

def bfs(data, start):
    if data[start][3] == True:     # if visited
        return 0
    data[start][3] = True       # mark as visited
    end = data[start][1]
    return bfs(data, end) + 1
    

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        mail = [0] * (n + 1)
        for _ in range(n):
            u, v = [int(x) for x in input().split()]
            mail[u] = [u, v, 0, False]
        # print(mail)
        r = 0
        for m in mail:
            if m == 0:
                continue
            s = m[0]
            m[2] = bfs(mail, s)
            if m[2] > r:
                r = m[2]
            for d in mail:
                if d == 0:
                    continue
                d[3] = False
        w = set()
        for m in mail:
            if m == 0:
                continue
            if m[2] == r:
                w.add(m[0])
        # print(mail, r, min(w))
        print("Case", i + 1, end="")
        print(":", min(w))
