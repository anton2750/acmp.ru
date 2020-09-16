import math

f_input = open('input.txt', 'r')
f_output = open("output.txt", 'w')

min_limit_dict = {}
general_dict = {}


def min_limit_calc(n):
    if min_limit_dict.get(n):
        return min_limit_dict.get(n)
    temp = math.ceil((-1 + (1 + 8 * n) ** 0.5) / 2)
    min_limit_dict.update({n: temp})
    return temp


def step(previous_step, n_left):
    global general_dict
    if general_dict.get((previous_step, n_left)):
        return general_dict.get((previous_step, n_left))

    if n_left == 0:
        return 1

    local_counter = 0

    min_limit = min_limit_calc(n_left)
    max_limit = min(previous_step - 1, n_left)
    for i in range(max_limit + 1)[min_limit:]:
        local_counter += step(i, n_left - i)
    general_dict.update({(previous_step, n_left): local_counter})
    return local_counter


n = int(f_input.read())
total_counter = step(n + 1, n)

print(total_counter)
f_output.write(str(total_counter))
