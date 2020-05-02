# https://onlinejudge.org/external/101/10114.pdf

while True:
	data = input().split()
	duration = int(data[0])
	if duration < 0:
		break
	payment = float(data[1])
	loan = float(data[2])
	records = int(data[3])
	depr = dict()
	for i in range(records):
		data = input().split()
		month = int(data[0])
		perc = float(data[1])
		depr[month] = perc
	# print(duration, payment, loan, depr)
	month = 0
	car_worth = (loan + payment) - (loan + payment) * depr[0]
	payment = loan / duration
	borrower_owe = loan
	# print(month, car_worth)
	current_depr  = depr[0]
	# print(month, car_worth, borrower_owe, current_depr)
	while borrower_owe >= car_worth:
		month += 1
		if month == 100:
			break
		if month in depr:
			current_depr = depr[month]
		car_worth -= car_worth * current_depr
		borrower_owe -= payment
		# print(month, car_worth, borrower_owe, current_depr)
	if month == 1:
		print(month, "month")
	else:
		print(month, "months")
	# print()

