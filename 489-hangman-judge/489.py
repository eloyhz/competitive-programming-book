# 489 - Hangman Judge
# https://onlinejudge.org/external/4/489.pdf

while True:
    # round
    r = int(input())
    if r == -1:
        break
    # solution
    s = set(input())
    # guesses
    g = input()
    checked = set()
    strokes = 0
    for c in g:
        if c in checked:
            continue
        else:
            checked.add(c)
        if c in s:
            s.remove(c)
            if len(s) == 0:
                break
        else:
            strokes += 1
    print("Round", r)
    if len(s) == 0 and strokes < 7:
        print("You win.")
    elif strokes >= 7:
        print("You lose.")
    else:
        print('You chickened out.')
