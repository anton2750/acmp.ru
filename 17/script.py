with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = int(f.readline())
        numbers = list(map(int, f.readline().split()))
        circle = [numbers[0]]
        length = 1

        current = 0
        temp = 0
        for i in numbers:
            current += 1
            temp += 1

            try:
                if i == circle[temp - 1]:
                    continue
            except IndexError:
                pass

            if i == circle[0]:
                temp = 1
            else:
                circle = numbers[0:current]
                length = current

        o.write(str(len(circle)))
