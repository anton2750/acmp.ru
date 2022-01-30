with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:

        # init:
        c = int(f.readline())
        m = list(map(int, f.readline().split()))

        timer = {1: 0, 3: 0, 5: 0}

        # student 5:
        fine = 0
        counter = 0
        for t in m:
            counter += t
            fine += counter
        timer[5] = fine

        # student 3:
        fine = 0
        counter = 0
        for t in m[::-1]:
            counter += t
            fine += counter
        timer[3] = fine

        # student 1:
        m.sort()
        fine = 0
        counter = 0
        for t in m:
            counter += t
            fine += counter
        timer[1] = fine

        # evaluation:
        n = 1
        c = timer[n]

        if timer[3] < c:
            n = 3
            c = timer[3]

        if timer[5] < c:
            n = 5
            c = timer[5]

        o.write(f"{n}")
