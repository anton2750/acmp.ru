n = int(input())
s = int((1 + abs(n)) / 2 * abs(n))
print(s if n > 0 else 1 - s)
