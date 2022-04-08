with open("input.txt", "w") as g:
    n = 30000
    g.write(f'{n}\n')
    for i in range(0, n):
        g.write(f'{1} ')
