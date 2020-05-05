# 156 Ananagrams
# https://onlinejudge.org/external/1/156.pdf

if __name__ == "__main__":
	words = dict()
	while True:
		line = input().split()
		if line == ["#"]:
			break
		for w in line:
			a = w.lower()
			a = list(a)
			a.sort()
			a = ''.join(a)
			if a not in words:
				words[a] = [1, w]
			else:
				words[a] = [words[a][0] + 1, w]
	result = []
	for w in words:
		if words[w][0] == 1:
			result.append(words[w][1])
	result.sort()
	for w in result:
		print(w)

