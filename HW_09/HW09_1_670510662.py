#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW09_1
# 204111 Sec 001

def left_max(list_a: list[int]) -> list[int]:
    max_value = max(list_a)
    left_max_list = [max_value - num for num in list_a]
    return left_max_list

if __name__ == '__main__':
    print("Testing...")
    assert left_max([2, 8, 1]) == [2, 8, 8]
    assert left_max([3, 3, 1, 1, 2, 4]) == [3, 3, 3, 3, 3, 4]
    print("AllPass!!")