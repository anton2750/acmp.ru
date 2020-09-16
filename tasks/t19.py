def my_count(l):
    s = 0
    for number in l:
        for g in l[number].values():
            if g == "1":
                s += 1
    return s


def chess_map_print(l):
    for number in l:
        print(number, end=": ")
        for g in l[number].values():
            print(g, end=" ")
        print()
    print("   A B C D E F G H")
    pass


def main(p):
    def cross(l, letter, number):
        for i in range(-8, 8 + 1):
            try:
                if l[number + i][chr(ord(letter) + i)] == "0":
                    l[number + i][chr(ord(letter) + i)] = "1"
            except:
                continue

        for i in range(-8, 8 + 1):
            try:
                if l[number + i][chr(ord(letter) - i)] == "0":
                    l[number + i][chr(ord(letter) - i)] = "1"
            except:
                continue
        return l

    def vertical_horisoltal(l, letter, number):
        for i in range(1, 8 + 1):
            try:
                if l[i][letter] == "0":
                    l[i][letter] = "1"
            except:
                continue
        for i in range(ord('A'), ord('H') + 1):
            try:
                if l[number][chr(i)] == "0":
                    l[number][chr(i)] = "1"
            except:
                continue
        return l

    def hourse(l, letter, number):
        steps = [[-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2]]
        for i in steps:
            try:
                if l[number + i[0]][chr(ord(letter) + i[1])] == "0":
                    l[number + i[0]][chr(ord(letter) + i[1])] = "1"
            except:
                continue

        return l

    # generate map
    chess_map = {g: {chr(i): "0" for i in range(ord('A'), ord('I'))} for g in range(8, 0, -1)}

    # С„РµСЂР·СЊ:
    point_letter = p[0][0]
    point_number = int(p[0][1])
    chess_map[point_number][point_letter] = "f"
    chess_map = vertical_horisoltal(chess_map, point_letter, point_number)
    chess_map = cross(chess_map, point_letter, point_number)

    # Р»Р°РґСЊСЏ:
    point_letter = p[1][0]
    point_number = int(p[1][1])
    chess_map[point_number][point_letter] = "l"
    chess_map = vertical_horisoltal(chess_map, point_letter, point_number)

    # РєРѕРЅСЊ:
    point_letter = p[2][0]
    point_number = int(p[2][1])
    chess_map[point_number][point_letter] = "h"
    chess_map = hourse(chess_map, point_letter, point_number)

    chess_map_print(chess_map)

    return my_count(chess_map)


with open("output.txt", "w") as g:
    with open("input.txt", "r") as f:
        g.write(str(main(list(f.readline().split()))))