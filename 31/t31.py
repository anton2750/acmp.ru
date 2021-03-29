def main():
    def all_perms(elements):
        if len(elements) <= 1:
            yield elements
        else:
            for perm in all_perms(elements[1:]):
                for i in range(len(elements)):
                    yield perm[:i] + elements[0:1] + perm[i:]

    def counter(r):
        test = 0
        for i in range(len(r)):
            if r[i] == i + 1:
                test += 1
        return 1 if test == k else 0

    with open("input.txt", "r") as f:
        n, k = list(map(int, f.readline().split()))

    # total = 0
    match = 0
    a = [*range(1, n + 1)]
    for p in all_perms(a):
        # total += 1
        match += counter(p)

    # print('total=', total)
    # print('match=', match)

    with open("output.txt", "w") as g:
        g.write(str(match))


if __name__ == "__main__":
    main()
