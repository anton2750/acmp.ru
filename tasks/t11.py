my_dict = {}


def step(n):
    global my_dict, k_max
    if my_dict.get(n):
        return my_dict.get(n)
    if n == 0:
        return 1
    my_sum = 0
    new_k = min(k_max, n)
    for i in range(new_k + 1)[1::]:
        my_sum += step(n - i)
    my_dict.update({n: my_sum})
    return my_sum


k_max, n_total = map(int, (input().split(" ")))
print(step(n_total))
