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
    # print(cat_altar(1))
    # print(cat_altar(2))
    # print(cat_altar(3))
    # print(cat_altar(4))
    # print(cat_altar(5))
    print(cat_altar(6))


def cat_altar(n):
    result = []
    if n == 1:
        return cat_head
    # Top
    for i in range(len(cat_head.split('\n'))):
        cat_head1 = "".join(cat_head.split('\n')[i])
        cat_head_and_space = (" "*10*(n-1))+cat_head1
        result.append(cat_head_and_space)
        
        
    for j in range(n-1):
        for i in range(len(cat_head.split('\n'))):
            
            cat_up1 = "".join(cat_up.split('\n')[i])
            # if j <= 0:
            cat_up_and_space = (" "*(10*((n-j)-n))) + cat_up1
            
            cat_down1 = "".join(cat_down.split('\n')[i])
            # cat_up_and_space = (" "*10*((n+j)-n))+cat_up1
            
            cat_down_and_space = (" "*(10*((n+j)-n+1))) + cat_down1
            
            result.append(cat_up_and_space + cat_down_and_space) 
            # print(j)
    return "\n".join(result)


if __name__ == '__main__':
    main()
