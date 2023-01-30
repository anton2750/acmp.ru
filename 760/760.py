with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [a, s, l] = list(map(int, f.readline().split()))
        inspectors = list(map(int, f.readline().split()))
        final = l / s * 60
        for d in range(0, len(inspectors), 2):
            final += inspectors[d - 1]
        o.write(f'{"%.2f" % final}')
