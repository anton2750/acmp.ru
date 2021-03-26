with open("../tasks/output.txt", "w") as o:
    with open("../tasks/input.txt", "r") as f:
        N = int(f.read())
        B = str(bin(N))
        print(N, B)
        S = 0
        for i in B[2:]:
            print(i)
            if int(i):
                S += 1
        print(S)
        o.write(str(N + S))