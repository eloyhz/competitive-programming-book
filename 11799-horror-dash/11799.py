# 11799 - Horror Dash
# https://onlinejudge.org/external/117/11799.pdf

t = int(input())
c = 1
while c <= t:
	a = list(map(int, input().split()))
	n = a[0]
	del a[0]
	largest = a[0]
	for i in range(1, n):
		if a[i] > largest:
			largest = a[i]
	print("Case ", c,": ", largest, sep='')
	c = c + 1


