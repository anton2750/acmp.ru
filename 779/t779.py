def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def main():
    r = 0
    with open("input.txt", "r") as f:
        n = int(f.readline())

        for i in range(n):
            a = ""
            while True:
                l = f.read(1)
                if l == ' ' or l == '':
                    break
                a += l
            r += int(a) / n

    with open("output.txt", "w") as g:
        g.write(str(int_r(r)))


if __name__ == "__main__":
    main()
