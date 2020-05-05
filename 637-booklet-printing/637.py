# 637 Booklet Printing
# https://onlinejudge.org/external/6/637.pdf

import math

if __name__ == "__main__":
	while True:
		n = int(input())	# pages
		if n == 0:
			break
		print("Printing order for", n, "pages:")
		if n == 1:
			print("Sheet 1, front: Blank, 1")
			continue
		total_sheets = math.ceil(n / 4)
		total_blank = 4 - n % 4
		sheets = [[0 for _ in range(4)] for _ in range(total_sheets)]
		page = 1
		for i in range(total_sheets):
			sheets[i][1] = page
			sheets[i][2] = page + 1
			page += 2
		fill = [0] * total_sheets * 2
		i = 0
		for p in range(total_sheets * 2 + 1, n + 1):
			fill[i] = p
			i += 1
		for p in range(n + 1, total_sheets * 4 + 1):
			fill[i] = "Blank"
			i += 1
		p = total_sheets * 2 - 1
		for i in range(total_sheets):
			sheets[i][0] = fill[p]
			sheets[i][3] = fill[p - 1]
			p -= 2
		for i in range(total_sheets):
			print("Sheet ", i + 1, ", front: ", sheets[i][0], ", ", sheets[i][1], sep="") 
			print("Sheet ", i + 1, ", back : ", sheets[i][2], ", ", sheets[i][3], sep="") 

			
