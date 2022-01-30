with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        m = int(f.readline())

        if m in [12, 1, 2]:
            o.write("Winter")
        elif m in [3, 4, 5]:
            o.write("Spring")
        elif m in [6, 7, 8]:
            o.write("Summer")
        elif m in [9, 10, 11]:
            o.write("Autumn")
        else:
            o.write("Error")
