with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        # k - lines per page
        # n - required line
        [k, n] = list(map(int, f.readline().split()))

        if n % k != 0:
            # page - page number
            # line = line on the page
            page = n // k + 1
            line = n % k
            o.write(f'{page} {line}')
        else:
            o.write(f'{n // k} {k}')
