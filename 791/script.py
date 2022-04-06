a = int(input())
r = []
if a not in [i for i in range(1, 9)]:
    r.append(a - 8)
if a not in [i * 8 + 1 for i in range(0, 8)]:
    r.append(a - 1)
if a not in [i * 8 for i in range(1, 9)]:
    r.append(a + 1)
if a not in [56 + i for i in range(1, 9)]:
    r.append(a + 8)
r.sort()
print(*r)
