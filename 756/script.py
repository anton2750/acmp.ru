with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [a, b] = list(map(int, f.readline().split()))
        o.write(f'{(a - 1) * (b - 1)}')
