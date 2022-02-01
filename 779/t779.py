from math import ceil, floor

n = int(input())
a = tuple(map(int, input().split()))
r = sum(a) / n
print(ceil(r) if r >= 0 else floor(r))
