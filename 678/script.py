e = {1: 1, 2: 0, 3: 0}

for i in input():
    if i == 'A':
        e[1], e[2] = e[2], e[1]
    elif i == 'B':
        e[3], e[2] = e[2], e[3]
    else:
        e[1], e[3] = e[3], e[1]

print(sum([a * b for (a, b) in e.items()]))
