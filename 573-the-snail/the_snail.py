# https://onlinejudge.org/external/5/573.pdf

while True:
	H, U, D, F = [ int(x) for x in input().split() ]
	if H == 0:
		break
	day = 0
	height = 0
	distance_climbed = U
	factor = round(F / 100 * U, 2)
	while True:
		day += 1
		height_after_climbing = height + distance_climbed
		height_after_sliding = height_after_climbing - D
		# print(day, round(height,2),  round(distance_climbed,2), round(height_after_climbing,2), round(height_after_sliding,2))
		distance_climbed -= factor
		if distance_climbed < 0:
			distance_climbed = 0
		height = height_after_sliding
		if height_after_climbing > H:
			print("success on day", day)
			break
		elif height_after_sliding < 0:
			print("failure on day", day)
			break
