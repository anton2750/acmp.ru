with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [a, b, c] = list(map(int, f.readline().split()))
        o.write(f'{a * b * 2 + b * c * 2 + a * c * 2} {a * b * c}')
