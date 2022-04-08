with open("output.txt", "w") as g:
    with open("input.txt", "r") as f:
        N = int(f.readline())
        L = list(map(int, f.readline().split()))

        last_index = 0
        while True:
            last_index = L.index(L[0], last_index + 1)
            possible_option = L[0:last_index]
            # print(last_index, possible_option)

            if (len(L) - 1) % len(possible_option) != 0:
                continue

            # magic:
            temp = L[:-1]
            while temp:
                if possible_option != temp[0:len(possible_option)]:
                    break
                del temp[0:len(possible_option)]
            if not temp:
                print(len(possible_option))
                g.write(str(len(possible_option)))
                break
