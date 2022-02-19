import math


def length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def square(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


x1, y1, x2, y2, x3, y3 = map(float, input().split())

a = length(x1, y1, x2, y2)
b = length(x1, y1, x3, y3)
c = length(x2, y2, x3, y3)

print('%0.1f' % square(a, b, c))
