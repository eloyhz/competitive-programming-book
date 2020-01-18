# 11498 - Division of Nlogonia
# https://onlinejudge.org/external/114/11498.pdf

while True:
	k = int(input())
	if k == 0:
		break
	nm = input().split(' ')
	n = int(nm[0])
	m = int(nm[1])
	while k > 0:
		k = k - 1
		xy = input().split(' ')
		x = int(xy[0])
		y = int(xy[1])
		dx = x - n
		dy = y - m
		if dx == 0 or dy == 0:
			print("divisa")
		elif dx > 0 and dy > 0:
			print("NE")
		elif dx > 0 and dy < 0:
			print("SE")
		elif dx < 0 and dy < 0:
			print("SO")
		elif dx < 0 and dy > 0:
			print("NO")

