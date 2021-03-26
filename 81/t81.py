with open("../tasks/output.txt", "w") as o:
    with open("../tasks/input.txt.txt", "r") as f:
        f.readline()
        M = list(map(int, f.readline().split()))
        o.write(f"{min(M)} {max(M)}")