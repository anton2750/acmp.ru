with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        f.readline()
        bridges = list(map(int, f.readline().split()))

        c = 0
        for i in bridges:
            c += 1
            if i <= 437:
                o.write(f'Crash {c}')
                quit()

        o.write('No crash')
