with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [w, h, r] = list(map(int, f.readline().split()))
        o.write("YES") if r * 2 <= min(w, h) else o.write("NO")
