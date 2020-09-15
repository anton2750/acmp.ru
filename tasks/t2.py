n = int(input())
a = abs(n)
s = int((1 + a) / 2 * a)
print(s if n > 0 else 1 - s)