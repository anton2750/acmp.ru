a = bin(int(input()))
c = 0
for i in a[2:]:
    c += 1 if i == '1' else 0
print(c)