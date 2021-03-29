def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())

    # 1-9 LOOP does not work
    def mult(lvl):
        r = 0
        for i in range(1, 10):
            if lvl > 1:
                r += i * mult(lvl - 1)
            else:
                r += i
        return r

    r = mult(n)

    # BRUTE FORCE does not work
    # r = 0
    # for i in range(10 ** (n - 1), 10 ** n):
    #     t = 1
    #     c = i
    #     for j in range(n):
    #         t *= c % 10
    #         if c % 10 == 0:
    #             break
    #         c = c // 10
    #     r += t

    print(r)

    with open("output.txt", "w") as g:
        g.write(str(r))


if __name__ == "__main__":
    main()
