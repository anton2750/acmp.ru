with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [a, b, c] = list(map(int, f.readline().split()))
        for i, j, k in [[a, b, c], [a, c, b], [c, b, a]]:
            if i + j == k:
                o.write("YES")
                quit()

        o.write("NO")
