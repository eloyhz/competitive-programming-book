# UVA 161 - Traffic Lights
# https://onlinejudge.org/external/1/161.pdf

from sys import stdin

def to_display(num):
	result = ""
	if num < 10:
		result = "0"
	return result + str(num)


if __name__ == "__main__":
	# s = [19, 20]
	# s = [30, 25, 35]
	# st = ['g', 'g']
	# st = ['g', 'g', 'g']
	# d = [0, 0]
	# d = [0, 0, 0]
	data = []
	for line in stdin:
		data += [int(x) for x in line.split()]
	
	data = data[:-3]
	# print(data)
	s = []
	for d in data:
		# print(d)
		if d != 0:
			s.append(d)
		else:
			# s = list(scenario)
			# scenario = []
			# print(s)
			st = ['g'] * len(s)
			d = [0] * len(s)
			found = False
			t = 0
			while not found and t <= 18000:
				t += 1
				for i in range(len(s)):
					d[i] = d[i] + 1
					if st[i] == 'g' and d[i] > s[i] - 5:
						st[i] = 'o'
					elif st[i] == 'o' and d[i] > s[i]:
						st[i] = 'r'
						d[i] = 1
					elif st[i] == 'r' and d[i] > s[i]:
						st[i] = 'g'
						d[i] = 1
				# print(t, st)
				a = True
				for b in st:
					if b != 'g':
						a = False
						break
				if a and t > min(s):
					found = True
			s = []
			if found:
				secs = t - 1
				mins = secs // 60
				secs = secs % 60
				hours = mins // 60
				mins = mins % 60
				print(to_display(hours), ":", to_display(mins), ":", to_display(secs), sep="")
			else:
				print("Signals fail to synchronise in 5 hours")

