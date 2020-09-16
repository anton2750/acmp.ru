with open("input.txt", "r") as file1:
    string = file1.readline()
    max_l = 0
    temp_l = 0
    for i in string:
        if i == "0":
            temp_l += 1
        else:
            if max_l < temp_l:
                max_l = temp_l
            temp_l = 0

    file2 = open("output.txt", "w").write(str(max_l))