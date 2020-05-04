# https://onlinejudge.org/external/115/11507.pdf

if __name__ == "__main__":
    while True:
        length = int(input())
        if length == 0:
            break
        decisions = input().split()
        current = "+x"
        for d in decisions:
            if d == "No":
                continue
            if current[1] == "x":
                if current[0] == "+":
                    current = d
                else:
                    if d == "+y":
                        current = "-y"
                    elif d == "-y":
                        current = "+y"
                    elif d == "+z":
                        current = "-z"
                    else:
                        current = "+z"
            elif current[1] == "y":
                if current[0] == "+":
                    if d == "+y":
                        current = "-x"
                    elif d == "-y":
                        current = "+x"
                    else:
                        current = "+y"            
                else:
                    if d == "+y":
                        current = "+x"
                    elif d == "-y":
                        current = "-x"
                    else:
                        current = "-y"
            elif current[1] == "z":
                if current[0] == "+":
                    if d == "+z":
                        current = "-x"
                    elif d == "-z":
                        current = "+x"
                    else:
                        current = "+z"
                else:
                    if d == "+z":
                        current = "+x"
                    elif d == "-z":
                        current = "-x"
                    else:
                        current = "-z"
        print(current)
