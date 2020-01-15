t = int(input())
while t > 0:
	t = t - 1
	ab = input().split(' ')
	a = int(ab[0])
	b = int(ab[1])
	if a < b:
		print("<")
	elif a > b:
		print(">")
	else:
		print("=")

