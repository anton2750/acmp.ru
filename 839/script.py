with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:

        while True:
            char = f.read(1)
            if not char:
                break

            if char == '0':
                o.write('NO')
                quit()

        o.write('YES')
