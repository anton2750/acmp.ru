# def sum_till_one(e):
#     return e + sum_till_one(e - 1) if e != 1 else 1


f = open('input.txt', 'r')
g = open("output.txt", 'w')
n = int(f.read())

s = 0

if n > 0:
    s = int((1 + n) / 2 * n)
if n == 0:
    s = 1
if n < 0:
    s = int((-1 + n) / 2 * abs(n)) + 1

g.write(str(s))