def anti_zero(n):
    if n[0] != '0' or len(n) == 1:
        return n

    for i in range(0, len(n)):
        if n[i] != '0':
            return n[i] + n[1:i] + '0' + n[i + 1:]


with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = f.readline().strip()
        b = f.readline().strip()

        if a[0] == '-':
            sign_a = -1
            a = anti_zero(''.join(sorted(a[1:])))
        else:
            sign_a = 1
            a = ''.join(sorted(a, reverse=True))

        if b[0] == '-':
            sign_b = -1
            b = ''.join(sorted(b[1:], reverse=True))
        else:
            sign_b = 1
            b = anti_zero(''.join(sorted(b)))

        o.write(str(sign_a * int(a) - sign_b * int(b)))
