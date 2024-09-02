#!usr/bin/env python3 
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Sec001

def main():
    print(skip_double([1, 1, 1, 1]))
    print(skip_double([1, 1, 1, 1, 1]))
    print(skip_double([1]))
    print(skip_double([5, 10]))
    print(skip_double([1, 2, 3, 4]))




def skip_double(list_a: list[int]) -> list[int]:
    reversed_list = list(reversed(list_a))
    map_list = list(map(lambda i: check_list(i,reversed_list) ,range(len(reversed_list))))
    return list(reversed(map_list))

def check_list(i, reversed_list):
    if(i%2==0):
        return reversed_list[i]
    else: 
        return reversed_list[i]*2


if __name__ == '__main__':
    main()