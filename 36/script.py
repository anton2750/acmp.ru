from math import sqrt
from math import ceil

a = int(input())
c = 0
for t in range(a + 1, 2 * a):
    c += 1
    for j in range(2, ceil(sqrt(t)) + 1):
        if t % j == 0:
            c -= 1
            break

print(c)
