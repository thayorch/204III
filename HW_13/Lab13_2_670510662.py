#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab13_2
# 20411 Sec 001

def square_matrix(list_x: list[list]) -> None:

    _matrix = [len(list_x)]
    for i in list_x:
        _matrix.append(len(i))

    for row in list_x:
        while len(row) < max(_matrix):
            row.append(0)

    while len(list_x) < max(_matrix):
        list_x.append([0] * max(_matrix))

if __name__ == '__main__':
    list_x = [[1, 2], [1, 2, 3], [1, 2], [1, 2], [1]]  
    square_matrix(list_x)
    print(list_x)
