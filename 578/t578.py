n = int(input())


def step(n):
    if n != 0:
        x = n % 3 if n % 3 != 0 else 3
        n -= x
        n = n // 3
        step(n)
        print(x, end="")
    return 0


step(n)