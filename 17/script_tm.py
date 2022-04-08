import time

start_time = time.time()


# def check(sample, tail):
#     if not tail:
#         return True
#     else:
#         return sample == tail[0:len(sample)] and check(sample, tail[len(sample):])


def check(sample, tail):
    while tail:
        if sample != tail[0:len(sample)]:
            return False
        else:
            tail = tail[len(sample):]
    return True


with open("output.txt", "w") as g:
    with open("input.txt", "r") as f:
        total = int(f.readline())
        numbers = list(map(int, f.readline().split()))

        possible_length = total - 1
        length = 0
        while length < total - 1:
            length = numbers.index(numbers[0], length + 1)
            possible_option = numbers[0:length]
            # print(length, possible_option)

            if (total - 1) % length != 0:
                continue

            if check(possible_option, numbers[length:total - 1]):
                possible_length = length
                break

        print(possible_length)
        g.write(str(possible_length))

print("--- %s seconds ---" % "{:.2f}".format(time.time() - start_time))
