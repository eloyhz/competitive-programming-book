# 10689 - Yet another Number Sequence
# https://onlinejudge.org/external/106/10689.pdf

def fibonacci(a, b, n):
	if n == 0:
		return a
	if n == 1:
		return b
	prev = a
	curr = b
	for _ in range(n - 1):
		tmp = prev
		prev = curr
		curr = curr + tmp
	return curr


def pisano(a, b, m):
	prev = a
	curr = b
	period_length = 0
	while period_length < m * m:
		tmp = prev
		prev = curr
		curr = (curr + tmp) % m
		period_length += 1
		if prev == 0 and curr == 1:
			break
	return period_length


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		a, b, n, m = map(int, input().split())
		p = pisano(a, b, 10 ** m)
		n = n % p
		f = fibonacci(a, b, n)
		f = f % (10 ** m)
		print(f)

