f = open("../tasks/input.txt.txt", "r")
g = open("../tasks/output.txt", "w")
g.write(str(int(f.readline()) * int(f.readline())))