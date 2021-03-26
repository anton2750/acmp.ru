T = 0


def I(v):
    X, Y, X1, Y1, X2, Y2, X3, Y3, X4, Y4 = v

    def t(X1, Y1, X2, Y2, X3, Y3):
        def d(X1, Y1, X2, Y2):
            return ((X1 - X2) ** 2 + (Y1 - Y2) ** 2) ** 0.5

        AB = d(X1, Y1, X2, Y2)
        BC = d(X2, Y2, X3, Y3)
        CA = d(X3, Y3, X1, Y1)
        p = (AB + BC + CA) / 2
        return (p * (p - AB) * (p - BC) * (p - CA)) ** 0.5

    A = t(X, Y, X1, Y1, X2, Y2)
    B = t(X, Y, X2, Y2, X3, Y3)
    C = t(X, Y, X3, Y3, X4, Y4)
    D = t(X, Y, X4, Y4, X1, Y1)
    E = t(X1, Y1, X2, Y2, X4, Y4)
    F = t(X2, Y2, X3, Y3, X4, Y4)
    if round((A + B + C + D)) == round(E + F):
        return 1
    return 0


def L(v):
    X, Y, X1, Y1, X2, Y2, X3, Y3, X4, Y4 = v

    def f(X, Y, AX, AY, BX, BY):
        def p(X1, Y1, X2, Y2):
            return {'A': Y2 - Y1, 'B': X1 - X2, 'C': Y1 * (X2 - X1) - X1 * (Y2 - Y1)}

        AX, BX = min(AX, BX), max(AX, BX)
        AY, BY = min(AY, BY), max(AY, BY)
        line = p(AX, AY, BX, BY)
        if (line["A"] * X + line["B"] * Y + line["C"] == 0) and AX <= X and X <= BX and AY <= Y and Y <= BY:
            return 1
        return 0

    if f(X, Y, X1, Y1, X2, Y2) or f(X, Y, X2, Y2, X3, Y3) or f(X, Y, X3, Y3, X4, Y4) or f(X, Y, X4, Y4, X1, Y1):
        return 1
    return 0


def m(v):
    if L(v) or I(v):
        return 1
    return 0


with open("../tasks/input.txt", "r") as f:
    n = int(f.readline())
    for i in range(n):
        T += m(list(map(int, f.readline().split())))
with open("../tasks/output.txt", "w") as o:
    o.write(str(T))