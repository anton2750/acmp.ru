with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [s, t] = list(map(int, f.readline().split()))

        c = 0
        while s != t:
            s = 1 if s == 12 else s + 1
            c += 1

        o.write(f'{c}')
