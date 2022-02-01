from math import ceil, floor

n = int(input())
a = list(x + 2 * 10 ** 9 for x in list(map(int, input().split())))
r = ceil(sum(a) / n)
print(r - 2 * 10 ** 9)
