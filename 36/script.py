from math import sqrt
from math import ceil

with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = int(f.readline())
        c = 0
        for t in range(a + 1, 2 * a):
            c += 1
            for j in range(2, ceil(sqrt(t)) + 1):
                if t % j == 0:
                    c -= 1
                    break

        o.write(f'{c}')
