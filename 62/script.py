with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = ord(f.read(1)) - 64
        b = int(f.read(1))

        o.write('BLACK') if (a + b) % 2 == 0 else o.write('WHITE')

        # for b in range(8, 0, -1):
        #     for a in range(1, 9):
        #         # v = 'B ' if (a + b) % 2 == 0 or a == b else 'W '
        #         v = f'{chr(a + 64)}{b}:B ' if (a + b) % 2 == 0 else f'{chr(a + 64)}{b}:W '
        #         print(v, end='')
        #     print()
