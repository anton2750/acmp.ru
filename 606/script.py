with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [a, b, c] = sorted(list(map(int, f.readline().split())))
        o.write('YES') if a + b > c else o.write('NO')
