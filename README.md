# acmp.ru

Мои варианты решения задач с портала олимпиадного программирования acmp.ru написанные на языке python

# IO templates:

One line, multiple variables:

```
with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        [a, b, c] = list(map(int, f.readline().split()))
        o.write(f'{a} {b} {c}')
```

One variable - integer:

```
with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = int(f.readline())
        o.write(f'{a}')
```

Two lines - two strings:

```
with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = f.readline().strip()
        b = f.readline().strip()
        o.write(f'{a}')
        o.write(f'{b}')
```

One integer variable from/to console:

```
a = int(input())
print(a)
```

test