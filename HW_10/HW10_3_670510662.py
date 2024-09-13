#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW10_3
# 204111 Sec 001


def polynomial_addition(p1, p2):
    list_poly = sorted((p1 + p2), reverse=True)
    # print(list_poly)
    result = []
    index = 0
    
    # index in list
    while index != len(list_poly):
        print(result)

        if index + 1 >= len(list_poly):
            result.append(list_poly[index])
            break

        if list_poly[index][0] == list_poly[index + 1][0]:
            result.append((list_poly[index][0], list_poly[index][1] + list_poly[index + 1][1]))
            index += 2
            continue
        
        else:
            result.append(list_poly[index])
            index += 1
            
# remove coeff == 0
    result = list(filter(lambda x: x[1] != 0, result))
    

    return result
    
    
    
if __name__ == '__main__':
    print("Testing...")
    assert polynomial_addition([(2, 6), (1, 34), (0, -8)], [(2, -6), (0, 2), (1, 1)]) == [(1, 35), (0, -6)]
    print("AllPass!!")
    