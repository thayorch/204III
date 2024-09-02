#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW10_EX
# 204111 Sec 001
cat_up = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''
cat_down = \
    '''| ／|、    
|(°、。7   
| |、 ~ヽ  
| ᒐᒐ_f_ )ノ
|__________
'''
cat_head = \
    ''' ／|、    
(°、。7   
 |、 ~ヽ  
 ᒐᒐ_f_ )ノ
__________'''

def main():
    # print(cat_altar(int(input())))
    print(cat_altar(1))
    print(cat_altar(2))
    print(cat_altar(3))


def cat_altar(n):
    for i in range(len(cat_head.split('\n'))):
        cat_head1 = "".join(cat_head.split('\n')[i])
        cat_head_and_space = " "*(6*n+2)+cat_head1
        print(cat_head_and_space)
    for j in range(n-1):
        for i in range(len(cat_head.split('\n'))):
            if j==n-2:
                cat_up1 = "".join(cat_up.split('\n')[i])
                cat_down1 = "".join(cat_down.split('\n')[i])
                cat_up_and_space = (cat_up1)
                cat_down_and_space = (" "*10*n*(n-2))+cat_down1
                print(cat_up_and_space+cat_down_and_space)   
            elif j != n:
                cat_up1 = "".join(cat_up.split('\n')[i])
                cat_down1 = "".join(cat_down.split('\n')[i])
                cat_up_and_space = (" "*5*(n-1))+cat_up1
                cat_down_and_space = (" "*9*(n-2))+cat_down1
                print(cat_up_and_space+cat_down_and_space)                   
    return


if __name__ == '__main__':
    main()
