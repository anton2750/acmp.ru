import time
import math
import random

start_time = time.time()


# logs pre calcs:
# d = {(k, v): math.log(k, v) for k in range(2, 100) for v in range(2, 100)}
# t = {k: 1 / k for k in range(1, 100)}


class Tower:
    # magic here:
    def formula(self):
        return str(self.base) + '**' + '**'.join(list(map(str, self.powers)))

    def mpow(self, x):
        return x[0] if (len(x) == 1) else x[0] ** self.mpow(x[1:])

    def __init__(self, i, data):
        self.i = i
        self.exp_count = data[0]

        self.base = data[1]
        self.powers = data[2:] + [1] * (10 - len(data[2:]))

        self.numbers = data[1:]

        # value calculation:
        # self.value = eval(self.formula())
        self.value = self.mpow(self.numbers)

    def __str__(self):
        return str(self.i)

    def __repr__(self):
        return str(self.i)

    def __lt__(self, other):
        return self.value < other.value


with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        # heavy metal load:
        towers = [Tower(i, list(map(int, f.readline().split()))) for i in range(1, int(f.readline()) + 1)]
        result = ' '.join([str(x) for x in sorted(towers)])

        o.write(result)
        print(result)

        print("--- %s seconds ---" % (time.time() - start_time))

        # print(t)
        # print(d)

        # example how to use precalcs:
        # print(d[(2, 2)])

        # map of logs:
        # for i in range(2, 100):
        #     o.write(f'log(x, base from 2 to 99) : x={i:2.0f} -> ')
        #     for j in range(2, 100):
        #         o.write(f'{math.log(i, j):.2f} ')
        #     o.write('\n')
