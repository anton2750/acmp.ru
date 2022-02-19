e = {1: 1, 2: 0, 3: 0}


def a():
    e[1], e[2] = e[2], e[1]


def b():
    e[3], e[2] = e[2], e[3]


def c():
    e[1], e[3] = e[3], e[1]


d = input()
for i in d:
    globals()[i.lower()]()

print(e[1] * 1 + e[2] * 2 + e[3] * 3)
