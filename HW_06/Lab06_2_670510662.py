#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab06_2
# 204111 Sec 001

def main(): 
    list_a = [1,2,3,4]
    dest_rotate_list(list_a, 1)
    print(list_a)
    # dest_rotate_list([1, 2, 3, 4], 105)
    # dest_rotate_list([1, 2, 3, 4], -3)

             
def dest_rotate_list(list_a: list[int], n: int) -> None:
    if(abs(n)>len(list_a)):
        n = n % len(list_a)        

    list_a[:] = list_a[-n:] + list_a[:-n]
    
if __name__ == '__main__':
    main()