with open("input.txt", "r") as f:
    x, y, z, w = list(map(int, f.readline().split()))

r = 0

for i in range(w // x + 1):  # x
    for j in range((w - i * x) // y + 1):  # y
        k = (w - x * i - y * j) / z
        if k % 1 == 0 and w // z >= k >= 0:
            r += 1
            # print((i, j, k))

print(r)

with open("output.txt", "w") as g:
    g.write(str(r))
