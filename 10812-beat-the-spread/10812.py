# 10812 - Beat the Spread!
# https://onlinejudge.org/external/108/10812.pdf

if __name__ == "__main__":
	t = int(input())
	for _ in range(t):
		s, d = [int(x) for x in input().split()]
		y = s - d
		if y < 0 or y % 2 != 0:
			print("impossible")
			continue
		y //= 2
		x = s - y
		if x < 0:
			print("impossible")
			continue
		if x > y:
			print(x, y)
		else:
			print(y, x)

