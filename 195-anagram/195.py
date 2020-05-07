# UVa 195 - Anagram
# https://onlinejudge.org/external/1/195.pdf

from itertools import permutations

words = set()

def permute(w, left, right):
	if left == right:	# base case
		words.add(''.join(w))
	else:
		for i in range(left, right + 1):
			w[left], w[i] = w[i], w[left]	# swap
			permute(word, left + 1, right)
			w[left], w[i] = w[i], w[left]	# swap back


if __name__ == "__main__":
	n = int(input())
	for _ in range(n):
#		word = list(input())
#		permute(word, 0, len(word) - 1)
#		for w in sorted(words):
#			print(w)
#		words.clear()
		word = input()
		p = permutations(word)
		for w in list(p):
			print(''.join(w))
