#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW13_3
# 204111 Sec 001

import copy
def sum_d_product(m: list[list[int]]) -> int:
    mt= copy.deepcopy(m)
    # print(mt)
    if len(mt) == 2:
        a = mt[0][0]
        b = mt[0][1]
        c = mt[1][0]
        d = mt[1][1]
        return a * d + c * b
    results = []
    for i in range(0, len(mt), 2):
        result = []
        while mt[i]:
            a = mt[i][0]
            b = mt[i][1]
            c = mt[i+1][0]
            d = mt[i+1][1]
            # print(a,b,c,d)            
            dot_product =  a * d + c * b
            # print(dot_product)
            result.append(dot_product)
            
            mt[i] = mt[i][2:]
            mt[i+1] = mt[i+1][2:]
        results.append(result)
    return sum_d_product(results)



# def test():
#     import random
#     for _ in range(100):
#         sqrt = 2**(random.choice(range(1,10)))
#         #print(sqrt)
#         l = []
#         for i in set(range(sqrt)):
#             tmp = []
#             for j in set(range(sqrt)):
#                 tmp += [random.randint(0,999)]
#             l += [tmp]
#         print(l)
#         print(len(l),len(l[0]))
#         print(sum_d_product(l))


if __name__ == '__main__':
    # test()  
#     print(sum_d_product([[3, 3, 3, 2],
# [2, 0, 3, 1],
# [2, 1, 2, 3],
# [1, 0, 2, -1]]))
#
#     print(sum_d_product([[1, 1, 5, -1],
# [12, 2, -2, 0],
# [4, 8, 8, 12],
# [4, 12, 12, 15]]))


    print(sum_d_product([
        [3,4,3,3,0,4,4,3],
        [1,4,1,1,1,2,3,2],
        [5,5,2,3,3,5,5,5],
        [1,5,1,3,1,5,3,5],
        [3,0,5,1,4,5,3,1],
        [5,3,2,3,3,1,5,5],
        [2,2,4,1,4,1,4,5],
        [5,5,0,1,0,4,3,1]
    ]))




#
#     print(sum_d_product([[0, -1, -1, 3, 2, 3, -1, 3],
# [3, -1, -1, 2, 0, -1, 2, 1],
# [3, 0, 1, 2, 3, 1, 3, 1],
# [2, 2, 1, -1, -1, 2, 0, 3],
# [1, 3, 2, 1, 3, 2, 2, 1],
# [1, 2, 2, 1, 3, 3, 1, 3],
# [2, 2, 2, 2, 2, 2, 3, 3],
# [1, 3, 2, 3, 1, 1, 2, 2]]))
