#!usr/bin/env python3

def readfile(filename, mode="rt"):
    with open(filename, mode, encoding="utf-8" ) as input_:
        return input_.read()

def square_matrix_bin_to_int(filename)->list[int]:
    bin = readfile(filename)
    x = bin.splitlines()
    x = list(map(lambda index : list(index),x))
    
    red = vertical_to_int(x)
    blue = horizontal_to_int(x)
    yellow = left_top_to_int(x)
    green = left_bottom_to_int(x)
    
    summaries = [red, blue, yellow, green] 
    summaries = list(map(lambda i: int(i,2),summaries))
    return  summaries


# Compass Binary

def vertical_to_int(x):
    target = len(x)//2
    return "".join(map(lambda index: index[target] ,x))

def horizontal_to_int(x):
    target = len(x)//2
    return "".join(x[target])

def left_top_to_int(x):  
    result = []
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                result.append(x[i][j])
    return "".join(result)

def left_bottom_to_int(x):
    result = []
    for i in range(len(x)):
        result.append(x[i][(len(x)-1)-i])
    return "".join(reversed(result))

    
if __name__ == '__main__':
    print(square_matrix_bin_to_int("infile2.txt"))