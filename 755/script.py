with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [first, second, lost] = list(map(int, f.readline().split()))
        o.write(f"{first + second - lost}") if first + second - lost >= 0 else o.write('Impossible')
