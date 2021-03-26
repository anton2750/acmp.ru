def counter(r):
    pass


def permutation(n):
    r = [*range(1, n + 1)]

    for i in r:
        yield i


def main():
    with open("input.txt", "r") as f:
        n, k = list(map(int, f.readline().split()))
        # print(n, k)
    r = permutation(n)
    for i in r:
        print(i)

    with open("output.txt", "w") as g:
        g.write('ERROR')


if __name__ == "__main__":
    main()
