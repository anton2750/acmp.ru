with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [a, b, c, t] = list(map(int, f.readline().split()))
        o.write(f'{t * b}') if t < a else o.write(f'{a * b + (t - a) * c}')
