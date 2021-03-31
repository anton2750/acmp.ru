with open("input.txt", "r") as f:
    with open("output.txt", "w") as o:
        a = int(f.readline())
        b = int(f.readline())
        if a > b :
            o.write(">")
        elif a < b:
            o.write("<")
        else:
            o.write("=")
