from math import sqrt
from math import ceil


def is_simple(a):
    for i in range(2, ceil(sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = int(f.readline())
        c = 0
        for i in range(a + 1, 2 * a):
            if is_simple(i):
                c += 1

        o.write(f'{c}')
