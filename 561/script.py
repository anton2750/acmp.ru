import time
import math

start_time = time.time()

# logs pre calcs:
# d = {(k, v): math.log(k, v) for k in range(2, 100) for v in range(2, 100)}
# t = {k: 1 / k for k in range(1, 100)}


class Tower:
    # magic:
    def formula(self):
        return str(self.base) + '**' + '**'.join(list(map(str, self.powers)))

    def __init__(self, i, data):
        self.i = i
        self.exp_count = data[0]
        self.base = data[1]
        # self.powers = data[2:] + [1] * (10 - len(data[2:])) # if needed
        self.powers = data[2:]

        self.value = eval(self.formula())

    def __str__(self):
        return str(self.i)

    def __repr__(self):
        return str(self.i)

    def __lt__(self, other):
        return self.value < other.value

    # def value(self):
    #     return 1


with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        # heavy metal:

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
        # c = 0
        # for i in range(2, 100):
        #     o.write(f'log(x, base from 2 to 99) : x={i:2.0f} -> ')
        #     for j in range(2, 100):
        #         c += 1
        #         o.write(f'{math.log(i, j):.2f} ')
        #     o.write('\n')
