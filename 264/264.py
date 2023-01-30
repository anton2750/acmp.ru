with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        f.readline() # skip line
        m = 0
        t = 0
        for i in list(map(int, f.readline().split())):
            if i > 0:
                t = t + 1
            else:
                t = 0

            if t > m:
                m = t
        o.write(f'{m}')
