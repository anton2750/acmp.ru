def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())

    # def counter(lvl):
    #     r = 0
    #     for i in range(1, 10):
    #         if lvl > 1:
    #             r += counter(lvl - 1)
    #         else:
    #             r += 1
    #     return r
    #
    # count = counter(n)

    # 1-9 LOOP does not work
    # def mult(lvl):
    #     r = 0
    #     for i in range(1, 10):
    #         if lvl > 1:
    #             r += i * mult(lvl - 1)
    #         else:
    #             r += i
    #     return r
    #
    # result = mult(n)

    # BRUTE FORCE does not work
    # result = 0
    # for i in range(10 ** (n - 1), 10 ** n):
    #     t = 1
    #     c = i
    #     for j in range(n):
    #         t *= c % 10
    #         if c % 10 == 0:
    #             break
    #         c = c // 10
    #     result += t

    # print('n =', n)
    # print('c =', count)
    # print('r =', result)

    with open("output.txt", "w") as g:
        g.write(str((5 ** n) * (9 ** n)))


if __name__ == "__main__":
    main()
