a = int(input())
l, r, t, d = a - 1, a + 1, a - 8, a + 8

res = []

et = [i for i in range(1, 9)]
el = [i * 8 + 1 for i in range(0, 8)]
er = [i * 8 for i in range(1, 9)]
ed = [56 + i for i in range(1, 9)]

if a not in et:
    res.append(t)
if a not in el:
    res.append(l)
if a not in er:
    res.append(r)
if a not in ed:
    res.append(d)

res.sort()

print(res)