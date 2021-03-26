def main():
    e = []  # четный
    o = []  # нечетный

    with open("input.txt", "r") as f:
        f.readline()  # just read a line
        values = list(map(int, f.readline().split()))
        for v in values:
            e.append(v) if v % 2 == 0 else o.append(v)

    with open("output.txt", "w") as g:
        g.write('\n'.join([
            ' '.join(str(i) for i in o),
            ' '.join(str(i) for i in e),
            'YES' if len(e) >= len(o) else 'NO']))


if __name__ == "__main__":
    main()
