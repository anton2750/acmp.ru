f = open("input.txt", "r")
g = open("output.txt", "w")
g.write(str(int(f.readline()) * int(f.readline())))