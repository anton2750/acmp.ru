with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        f.readline()
        fork = list(map(int, f.readline().split()))
        o.write(f'{sum(fork) - len(fork) + 1}')
