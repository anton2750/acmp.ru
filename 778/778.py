with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        o.write(f'{round(sum(list(map(int, f.readline().split()))) / 27)}')
