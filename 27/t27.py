def map_print():
    for i in my_map:
        for g in i:
            print(g, end=" ")
        print()
    pass


def m_c():
    global my_map, w, h
    c = 0
    for i in my_map:
        g = 0
        while g < h:
            if i[g] > 0:
                g += i[g]
            else:
                c += 1
                g += 1
    return c


def add_points(p):
    global my_map
    x1, y1, x2, y2 = p

    # ?????µ?? ????-???‚?????‡????:
    for i in range(x1, x2):
        for g in range(y1 + my_map[i][y1], y2):
            my_map[i][g] = max(y2 - g, my_map[i][g])

    # ?????µ?? ????-???‚?????‡????:
    # for i in range(x1, x2):
    #     my_map[i][y1] = max(y2 - y1, my_map[i][y1])

    pass


with open("../tasks/output.txt", "w") as g:
    with open("../tasks/input.txt", "r") as f:
        w, h = list(map(int, f.readline().split()))
        n = int(f.readline())
        total = w * h

        my_map = [[0 for i in range(h)] for g in range(w)]
        for _ in range(n):
            add_points(map(int, f.readline().split()))
        map_print()
        g.write(str(m_c()))