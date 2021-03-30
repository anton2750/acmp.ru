def main():
    r = set()

    def sum(s, a):
        if s == 0:
            temp = [0] * 3
            for i in a:
                temp[d[i]] += 1
            r.add(str(temp))
            pass

        for i in [x, y, z]:
            if ((s - i) % x == 0 or (s - i) % y == 0 or (s - i) % z == 0) and s >= i:
                sum(s - i, a + [i])
        pass

    with open("input.txt", "r") as f:
        x, y, z, w = list(map(int, f.readline().split()))

    d = {x: 0, y: 1, z: 2}
    sum(w, [])
    for i in r:
        print(i)

    print(len(r))
    with open("output.txt", "w") as g:
        g.write(str(len(r)))


if __name__ == "__main__":
    main()
