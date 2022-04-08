# case 1: one circle
# case 2: several circles


with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        total_length = int(f.readline())
        input_numbers = list(map(int, f.readline().split()))

        # setup:
        circle = [input_numbers[0]]
        circle_length = 1
        circle_iterator = 0
        global_iterator = 0

        # loop:
        for i in input_numbers:
            global_iterator += 1
            circle_iterator += 1

            try:
                if i == circle[circle_iterator - 1]:
                    continue
            except IndexError:
                pass

            # suppose it is a new circle:
            # items must be equal to be first one
            # circle iterator - 1 must be equal to circle length
            if i == circle[0] and circle_iterator - 1 == circle_length:
                circle_iterator = 1
            # suppose it is still the first loop:
            else:
                circle = input_numbers[0:global_iterator]
                circle_length = global_iterator
                circle_iterator = global_iterator

                # hot fix:
                # if global_iterator == total_length:
                #     circle_length = total_length - 1

        # hot fix:
        if circle_iterator != 1:
            circle_length = total_length - 1

        o.write(str(circle_length))
        print(circle_length)
