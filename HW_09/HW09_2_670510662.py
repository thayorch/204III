#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW09_2
# 204111 Sec 001

from math import isclose
def median_of_median(list_a: list[float]) -> float:
    if not list_a: 
        return 0
    if len(list_a) == 1:
        return list_a[0]
    if len(list_a) == 2:
        return sum(list_a)/2    

    if(len(list_a) >= 3):
        list_1 = list_a[:len(list_a)//3]
        list_2 = list_a[(len(list_a)//3):(len(list_a)//3)*2]
        list_3 = list_a[(len(list_a)//3)*2:]
        lists = [median_of_median(list_1), median_of_median(list_2), median_of_median(list_3)]
        return sum(lists)-max(lists)-min(lists)
        

if __name__ == '__main__':
    print("Testing...")
    # print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))
    epsilon=10**-3
    assert isclose(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]), 21.0, abs_tol=epsilon)
    print("AllPass!!")