with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [c, h, x] = list(map(int, f.readline().split()))
        o.write(str(min([c // 2, h // 6, x])))
