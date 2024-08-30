#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab07_2
# 204111 Sec 001

def main():
    # test()
    square_frame(4)

def square_frame(n: int, sep: str=' ') -> str:
     
    sqr_num = list(map(lambda i: i+1,range((n**2)-(n-2)**2)))
    sqr_num = list(map(lambda i: str(i).zfill(len(str(max(sqr_num)))),sqr_num))
    most_value = sqr_num[-1]

    lists_top = sqr_num[0:n]
    lists_right = sqr_num[n:2*n-2]
    lists_buttom = sqr_num[2*n-2:3*n-2]
    lists_left =  sqr_num[3*n-2:4*n+4][::-1]
    
    # return lists_top, *zip(lists_right, lists_left), lists_buttom
    
    #lists_x = list(zip(lists_right, lists_left))
    # return lists_x

    lists_top = list(map(lambda i: str(i),lists_top))
    lists_buttom = list(map(lambda i: str(i),lists_buttom))[::-1]
    
    lists_top = sep.join(lists_top)
    
    list_center = cenntered_list(lists_left, lists_right, sep, n, lists_top, len(str(most_value)))
    print(lists_top + '\n' + '\n'.join(list_center) + '\n' + sep.join(lists_buttom)) 

def cenntered_list(lists_left, lists_right, sep, n,lists_top, max_len):
    len_something = len(lists_top) - 2 * max_len
    return  list(map(lambda left, right: str(left)+ sep * len_something + str(right), lists_left, lists_right)) 
    # return  list(map(lambda left, right: str(left) + sep * (2 * (len(lists_right)-1 )) + str(right), lists_left, lists_right))
    


def test():
    assert square_frame(3) == """1 2 3\n8   4\n7 6 5"""
    assert square_frame(4,'.') == """01.02.03.04\n12.......05\n11.......06\n10.09.08.07\n""" 

if __name__ == "__main__":
    main()