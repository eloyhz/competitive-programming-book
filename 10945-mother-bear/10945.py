# UVa 10945 - Mother Bear
# https://onlinejudge.org/external/109/10945.pdf

def is_palindrome(w):
	n = len(w)
	for i in range(n // 2):
		if w[i] != w[n - i - 1]:
			return False
	return True

if __name__ == "__main__":
	while True:
		sentence = input()
		if sentence == "DONE":
			break
		word = ""
		for c in sentence:
			if c == '.' or c == ',' or c == '!' or c == '?' or c == ' ':
				continue
			word += c.lower()
		if is_palindrome(word):
			print("You won't be eaten!")
		else:
			print("Uh oh..")

