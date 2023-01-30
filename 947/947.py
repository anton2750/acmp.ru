with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = float(f.readline())
        i = 0
        s = 0
        while s < a:
            s += 1 / (i + 2)
            i += 1
        o.write(f'{i} card(s)')
