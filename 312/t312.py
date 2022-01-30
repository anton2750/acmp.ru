with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a1, a2, d = list(map(int, f.readline().split()))
        o.write(str(a1 + (a2 - a1) * (d - 1)))
