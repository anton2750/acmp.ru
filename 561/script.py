import math

# logs pre calcs:
d = {(k, v): math.log(k, v) for k in range(2, 100) for v in range(2, 100)}


class Tower:
    def __init__(self, data):
        self.exp_count = data[0]
        self.base = data[1]
        self.powers = data[2:] + [1] * (10 - len(data[2:]))

    def __str__(self):
        return str(self.base) + ' ** ' + '**'.join(list(map(str, self.powers)))

    def __repr__(self):
        return str(self.base) + ' ** ' + '**'.join(list(map(str, self.powers)))

    # def value(self):
    #     return 1


with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        # heavy load:
        total = int(f.readline())
        towers = {k: Tower(list(map(int, f.readline().split()))) for k in range(1, total + 1)}

        print(towers)

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
