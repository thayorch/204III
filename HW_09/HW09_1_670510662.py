#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW09_1
# 204111 Sec 001

def left_max(list_a: list[int],current_max=None,i=0) -> list[int]:
    
    if current_max is None:
        current_max = list_a[0]

    if i >= len(list_a):
        return list_a
    
    current_max = max(current_max, list_a[i])
    
    if(list_a[i] < current_max):
        list_a[i] = current_max
        
    return left_max(list_a,current_max,i+1) 

if __name__ == '__main__':
    print("Testing...")
    # print(left_max([2, 8, 8, 8, 8, 1, 9]))
    assert left_max([2, 8, 1]) == [2, 8, 8]
    assert left_max([3, 3, 1, 1, 2, 4]) == [3, 3, 3, 3, 3, 4]
    print("AllPass!!")