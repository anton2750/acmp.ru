with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [t1, t2] = list(map(int, f.readline().split()))
        w = f.readline().strip()

        if w == 'auto':
            o.write(f'{t2}')
        elif w == 'freeze':
            o.write(f'{t2}') if t1 > t2 else o.write(f'{t1}')
        elif w == 'heat':
            o.write(f'{t2}') if t1 < t2 else o.write(f'{t1}')
        else:
            o.write(f'{t1}')
