# 11507 Bender B. Rodríguez Problem
# https://onlinejudge.org/external/115/11507.pdf

if __name__ == "__main__":
    movements = {
        "+x": {
            "+y": "+y",
            "-y": "-y",
            "+z": "+z",
            "-z": "-z"
        },
        "-x": {
            "+y": "-y",
            "-y": "+y",
            "+z": "-z",
            "-z": "+z"
        },
        "+y": {
            "+y": "-x",
            "-y": "+x",
            "+z": "+y",
            "-z": "+y"
        },
        "-y": {
            "+y": "+x",
            "-y": "-x",
            "+z": "-y",
            "-z": "-y"
        },
        "+z": {
            "+y": "+z",
            "-y": "+z",
            "+z": "-x",
            "-z": "+x"
        },
        "-z": {
            "+y": "-z",
            "-y": "-z",
            "+z": "+x",
            "-z": "-x"
        }
    }
    while True:
        length = int(input())
        if length == 0:
            break
        decisions = input().split()
        current = "+x"
        for d in decisions:
            if d == "No":
                continue
            current = movements[current][d]
        print(current)
