# https://onlinejudge.org/external/117/11727.pdf

t = int(input())
for i in range(t):
	salaries = [int(s) for s in input().split()]
	salaries.sort()
	print("Case", i + 1, end="")
	print(":", salaries[1])
