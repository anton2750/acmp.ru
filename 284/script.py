with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        n = int(f.readline())
        e = list(map(int, f.readline().split()))
        c = int(f.readline())
        for i in range(c):
            l, r = list(map(int, f.readline().split()))
            o.write(" ".join(list(map(str, e[l - 1:r]))) + '\n')
