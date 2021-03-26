def main():
    e = []  # четный
    o = []  # нечетный

    with open("input.txt", "r") as f:
        f.readline()  # just read a line
        values = list(map(int, f.readline().split()))
        for v in values:
            if v % 2 == 0:
                e.append(v)
            else:
                o.append(v)

    with open("output.txt", "w") as g:
        g.writelines([' '.join(str(i) for i in o), "\n"])
        g.writelines([' '.join(str(i) for i in e), "\n"])
        g.write('YES') if len(e) >= len(o) else g.write('NO')


if __name__ == "__main__":
    main()
