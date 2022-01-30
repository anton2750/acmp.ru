with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [m1, m2, m3] = list(map(int, f.readline().split()))
        # 94, 727
        if not all(x >= 94 for x in [m1, m2, m3]):
            o.write('Error')
        elif not all(x <= 727 for x in [m1, m2, m3]):
            o.write('Error')
        else:
            o.write(f"{max([m1, m2, m3])}")
