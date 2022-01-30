with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        m = list(map(int, f.readline().split()))

        if any(x < 94 for x in m):
            o.write('Error')
        elif any(x > 727 for x in m):
            o.write('Error')
        else:
            o.write(f"{max(m)}")
