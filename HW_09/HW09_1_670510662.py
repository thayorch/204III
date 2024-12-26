#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW09_1
# 204111 Sec 001

# def left_max(list_a: list[int],current_max=None,i=0) -> list[int]:
#     if i == len(list_a):
#         return list_a
    
#     if current_max is None:
#         current_max = list_a[0]
    
#     current_max = max(list_a[i], current_max)
#     if(list_a[i] < current_max):
#         list_a[i] = current_max
    
#     # print(current_max)
#     return left_max(list_a, current_max, i+1)


def left_max(list_a:list[int]) -> list[int]:
    list_a = list(filter(lambda x: x>=0,list_a))
    if len(list_a) <= 1: return list_a
    if list_a[0] >= list_a[1]:
        list_a[1] = list_a[0]
        now = list_a[1]
        return [now] + left_max(list_a[1:])
    now = list_a[0]
    return [now] + left_max(list_a[1:])


from functools import reduce
def left_max(list_a: list[int]) -> list[int]:
    return list(reduce(lambda x, y: x + [max(x[-1], y)], list_a[1:], [list_a[0]]))


if __name__ == '__main__':
    print("Testing...")
    assert left_max([2, 8, 1]) == [2, 8, 8]
    assert left_max([3, 3, 1, 1, 2, 4]) == [3, 3, 3, 3, 3, 4]
    assert left_max([5, 4, 3, 2, 1,]) == [5, 5, 5, 5, 5]
    assert left_max([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert left_max([7]) == [7]
    assert left_max([1,2,3,4,5]) == [1, 2, 3, 4, 5]    
    # print(left_max([2,8,1]))
    print("AllPass!!")