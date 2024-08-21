#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW07_1
# 204111 Sec 001

def main():
    # print(print_polynomial([(2, -6), (0, -8), (1, 34)],'x'))
    # print(print_polynomial([(4, -6), (2, -8), (3, 34)],'x'))
    # print(print_polynomial([(4, -6), (2, -8), (3, 0)],'x'))
    # print(print_polynomial([(0, 0),  (1, 1)],'y'))
    # print(print_polynomial([(0, 0),  (1, 0)],''))
    # # print(print_polynomial([(0, 0)],'y'))
    # print(print_polynomial([(0, -5)],'y')) ###
    # print(print_polynomial([(1, 4), (1, 1), (3, 6)],'N'))
    # print(print_polynomial([(2,0), (0, -1)], 's'))
    # print(print_polynomial([(2, 6), (0, 0), (1, 0)],"x"))
    # print(print_polynomial([(5, 1), (4, -1), (0, 1)],"x"))
    # print(print_polynomial([(0, 1), (1, -1)],"x"))
    # print(print_polynomial([(2, -100000), (1 , -1),(0 , -1),(3 , -1)],"x"))
    # print(print_polynomial([(1, 0.0001),(1,0)], "x"))
    # print(print_polynomial([(0, 0), (1, 5)],'y'))
    # print(print_polynomial([(0,0),(1,0)], "x")) # 0
    # print(print_polynomial([(0, 0), (1, 5)],'y'))
    # print(print_polynomial([(0, 5), (1, 5)],'x'))
    # print(print_polynomial([(2, 0), (0, -1), (1, 0)],"x"))
    # print(print_polynomial([(5, 1), (4, 1), (0, 1)],"x"))
    # print(print_polynomial([(5, 1), (4, -1), (0, 1)],"x"))
    # print(print_polynomial([(0, 5), (1, 0)],'y'))
    print(print_polynomial([(70,51), (1,-27)],'F'))
    test_polinomial() 

def print_polynomial(pc_list: list[tuple[int, float]], v: str):
    
    temp = sorted(pc_list ,key =lambda x: x[0],reverse=True)
    # return temp
    lists_zero_power = list(filter(lambda x: x[0] == 0,temp))
    lists_max_power = list(filter(lambda x: x == max(temp) and x[0] != 0,temp))
    lists_other_power = list(filter(lambda x: x[0] != 0 and x != max(temp) ,temp))
    # print (lists_zero_power,lists_other_power,lists_max_power)
    # return lists_zero_power
    # return lists_other_power
    # return temp[-1]
    # return temp, lists_zero_power, lists_other_power, lists_max_power

    start = list(map(lambda x: max_list_case(x[0],x[1],v) ,lists_max_power))
    mid = list(map(lambda x: other_power_case(x[0],x[1],v) ,lists_other_power))
    ends = list(map(lambda x: zero_power_case(x[1]) ,lists_zero_power))
    # print(start, mid, ends)
    # return ''.join(ends)
    # return start + ends
    if(len(''.join(start).strip())+len(''.join(mid).strip()) == 0):
        return (''.join(ends)).replace(' ','').strip('+')
    else:
        return (''.join(start) + ''.join(mid)+''.join(ends)).strip('+ ')
        
    
    
def max_list_case(p,c,v):
    if(c == 0):
        return ''
    if(abs(c) == 1 and p==1):
        if(c > 0):
            return f"{v} "
        else:
            return f"-{v} "
    elif(abs(c) == 1 and p!=1):
        if(c > 0):
            return f"{v}^{p} "
        else:
            return f"-{v}^{p} "
    elif(p==1):
        return f"{c}{v} "
    else:
        return f"{c}{v}^{p} "
    
def other_power_case(p,c,v):
    if(c > 0):
        if(p == 1 and c == 1):
            return f"+ {v} "
        elif(p == 1 and c != 1):
            return f"+ {c}{v} "
        elif(c==1):
            return f"+ {v}^{p} "
        else:
            return f"+ {c}{v}^{p} "
    elif(c < 0):
        if(p == 1 and c == -1):
            return f"- {v} "
        elif(p == 1 and c != -1):
            return f"- {abs(c)}{v} "
        elif(c==-1):
            return f"- {v}^{p} "
        else:
            return f"- {abs(c)}{v}^{p} "
    else:
        return ''

def zero_power_case(c):
    if(c > 0):
        return f"+ {c}"
    elif(c < 0):
        return f"- {abs(c)}"
    else:
        return ''




def test_polinomial():
    # assert print_polynomial([(2, -6), (0, -8), (1, 34)],'x') == '-6x^2 + 34x - 8' ;print("Pass !!")
    # assert print_polynomial([(4, -6), (2, -8), (3, 34)],'x') == '-6x^4 + 34x^3 - 8x^2';print("Pass !!")
    # assert print_polynomial([(2, -6), (0, -8), (1, 34)],'y') == '-6y^2 + 34y - 8' ;print("Pass !!")
    # assert print_polynomial([(2, 6), (0, -8), (1, 34)],'y') == '6y^2 + 34y - 8' ;print("Pass !!")
    # assert print_polynomial([(2, 6.5), (0, -8)],'y') == '6.5y^2 - 8' ;print("Pass !!")
    assert print_polynomial([(4, -6), (2, -8), (3, 34),(6,34),(1,5)],'x') == '34x^6 - 6x^4 + 34x^3 - 8x^2 + 5x' ;print("Pass !!")
    assert print_polynomial([(4, -6), (2, -8), (3, 0)],'x') == '-6x^4 - 8x^2' ;print("Pass !!")
    assert print_polynomial([(0, 0), (1, 1)],'y') == 'y' ;print("Pass !!")
    # assert print_polynomial([(0, 0), (1, 0)],'y') == 0 ;print("Pass !!")
    assert print_polynomial([(0, 0), (1, 5)],'y') == '5y' ;print("Pass !!")
    assert print_polynomial([(0, 5), (1, 0)],'y') == '5' ;print("Pass !!")
    assert print_polynomial([(0, 5), (1, 5)],'x') == '5x + 5' ;print("Pass !!")
    assert print_polynomial([(2, -66), (0, -8), (1, 34)],"x")=='-66x^2 + 34x - 8'
    assert print_polynomial([(2, -66), (1, 34)],"x")=='-66x^2 + 34x'
    assert print_polynomial([(2, 6), (0, -8), (1, 34)],"y")=='6y^2 + 34y - 8'
    assert print_polynomial([(2, -6), (0, -1), (1, 34)],"x")=='-6x^2 + 34x - 1'
    assert print_polynomial([(2, -6), (0, 1), (1, 34)],"x")=='-6x^2 + 34x + 1'
    assert print_polynomial([(2, 6), (0, 0), (1, 0)],"x")=='6x^2'
    assert print_polynomial([(2, 0), (0, -1), (1, 0)],"x")=='-1'
    assert print_polynomial([(5, 2), (4, -2), (1, 0)],"x")=='2x^5 - 2x^4'
    assert print_polynomial([(5, 1), (4, 1), (0, 1)],"x")=='x^5 + x^4 + 1'
    assert print_polynomial([(1, 5), (0, 1)],"x")=='5x + 1'
    assert print_polynomial([(0, 1), (1, 1)],"x")=='x + 1'
    assert print_polynomial([(0, 1), (1, -1)],"x")=='-x + 1'
    assert print_polynomial([(1, 0), (0 , -2)],"x")=='-2'
    assert print_polynomial([(0 , -1)],"x")=='-1'
    assert print_polynomial([(0 , -2)],"x")=='-2'
    assert print_polynomial([(0 , 1)],"x")=='1'
    assert print_polynomial([(0 , 2)],"x")=='2'
    assert print_polynomial([(1 , 2)],"x")=='2x'
    assert print_polynomial([(1 , 1)],"x")=='x'
    assert print_polynomial([(1 , -1)],"x")=='-x'
    assert print_polynomial([(1 , -2)],"x")=='-2x'
    assert print_polynomial([(2 , -1)],"x")=='-x^2'
    assert print_polynomial([(2 , 1)],"x")=='x^2'
    assert print_polynomial([(2, -100000), (1 , -1),(0 , -1),(3 , -1)],"x")=='-x^3 - 100000x^2 - x - 1'
    # assert print_polynomial([(1, 0.0001),(1,0)], "x") == ''
    print('allpass')
    
if __name__ == '__main__':
    main()