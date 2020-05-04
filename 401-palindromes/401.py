# 401 - Palindromes
# https://onlinejudge.org/external/4/401.pdf

from sys import stdin

def is_regular_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

def is_mirror(s):
    n = len(s)
    mirror = {
        'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J', 'M': 'M',
        'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
        'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '8': '8'
    }
    if n == 1:
        return s[0] in mirror and s[0] == mirror[s[0]]
    for i in range(n // 2):
        if s[i] not in mirror or s[n - i - 1] not in mirror:
            return False
        if mirror[s[i]] != s[n - i - 1] or s[i] != mirror[s[n - i - 1]]:
            return False
    if n % 2 != 0:
        if s[n // 2] not in mirror:
            return False
        if s[n // 2] != mirror[s[n // 2]]:
            return False
    return True


if __name__ == "__main__":
    for line in stdin:
        if line[-1] == "\n":
            word = line[:-1]
        else:
            word = line
        irp = is_regular_palindrome(word)
        im = is_mirror(word)
        if not irp and not im:
            print(word, "-- is not a palindrome.")
        elif irp and not im:
            print(word, "-- is a regular palindrome.")
        elif not irp and im:
            print(word, "-- is a mirrored string.")
        else:
            print(word, "-- is a mirrored palindrome.")
        print()