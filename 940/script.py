with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [a, b] = list(f.readline().split())
        b = b.strip()
        o.write(f'{b[0:int(a) - 1:] + b[int(a):]}')
