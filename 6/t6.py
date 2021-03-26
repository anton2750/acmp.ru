def main():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

    with open("input.txt", "r") as f:
        try:
            l1, n1, s, l2, n2 = list(f.read(5))
            with open("output.txt", "w") as g:
                if s == '-' and l1 in letters and l2 in letters and n1 in numbers and n2 in numbers:
                    ld, nd = [abs(ord(l1) - ord(l2)), abs(int(n1) - int(n2))]
                    if ld == 2 and nd == 1 or ld == 1 and nd == 2:
                        g.write('YES')
                    else:
                        g.write('NO')
                else:
                    g.write('ERROR')
        except Exception:
            with open("output.txt", "w") as g:
                g.write('ERROR')
            pass


if __name__ == "__main__":
    main()
