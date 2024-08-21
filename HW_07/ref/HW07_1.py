#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW07_1
# 204111 Sec 001

def main():
    print(print_polynomial([(2, -66), (0, -8), (1, 34)],'x'))
    print(print_polynomial([(4, -6), (2, -8), (3, 34)],'x'))
    print(print_polynomial([(4, -6), (2, -8), (3, 0)],'x'))
    print(print_polynomial([(0, 0),  (1, 1)],'y'))
    print(print_polynomial([(0, 0),  (1, 0)],'y'))
    print(print_polynomial([(0, 0)],'y'))
    print(print_polynomial([(0, 5)],'y'))
    print(print_polynomial([(1, 4), (1, 1), (3, 6)],'N'))
    print(print_polynomial([(2,0), (0, -1)], 's'))
    print(print_polynomial([(2, 6), (0, 0), (1, 0)],"x"))
    print(print_polynomial([(5, 1), (4, -1), (0, 1)],"x"))
    print(print_polynomial([(0, 1), (1, -1)],"x"))
    print(print_polynomial([(2, -100000), (1 , -1),(0 , -1),(3 , -1)],"x"))
    print(print_polynomial([(1, 0.0001),(1,0)], "x"))
    test_polinomial()


def print_polynomial(pc_list: list[tuple[int, float]], v: str):
   temp = sorted(pc_list ,key =lambda x: x[0],reverse=True)
   power_out = list(map(lambda x: x[0],temp))  
   coefficients_out = list(map(lambda x: x[1],temp))
   lists = list(map(lambda i:  check_lists(power_out,coefficients_out, v, i), range(len(temp))))
   return ''.join(lists).lstrip('+ ').strip()
   
def check_lists(power, coefficients, variable, index):
    exp = coefficients_ex(coefficients, index)
    
    if(coefficients[index] == 0):   #  0 x var
        return ''
    
    if(power[index] == max(power) and power[index] != 1 and power[index] != 0 and abs(coefficients[index]) != 1):   
        return f"{coefficients[index]}{variable}^{power[index]} "
    
    
    if(abs(coefficients[index])==1 and power[index] != 0 and power[index] != 1):
        if(coefficients[index] > 0):
            if(power[index] == 1):
                return f"+ {variable} "
            elif(power[index] == 0):
                return f"+ {coefficients[index]}"
            else:
                return f"{variable}^{power[index]} "
        if(coefficients[index] < 0):
            if(power[index] == 1):
                return f"- {variable} "
            elif(power[index] == 0):
                return f"- {coefficients[index]}"
            else:
                if(power[index] == max(power)):
                    return f"-{variable}^{power[index]} "
                else:
                    return f"- {variable}^{power[index]} "
                    
                
        return f"{variable}^{power[index]} "
    
    
    if(power[index] == 1):                                 # coe * var = 2var
        if(abs(power[index]) == max(power)):
            return f"{exp}{variable} "
        if(abs(coefficients[index]) == 1):                        # 1 * var = var
            return f"{exp} {variable} "
        if(coefficients[index-1] == 0):
            return f"{exp} {coefficients[index]}{variable} "
        else:                                                  # 2 * var = 2var
            return f"{exp} {coefficients[index]}{variable} "
        
    if(power[index] == 0):                                 # var**0                   
        
        if(coefficients[index] != 0 ): 
            if(coefficients[index-1] != 0):
                return f"{exp} {abs(int(coefficients[index]))}"
            return f"{exp}{abs(int(coefficients[index]))}"
        elif(coefficients[index-1] != 0  and coefficients[index] == 0): 
            return ''
        else:
            return f"{exp} {coefficients[index]}"


    else:
        return f"{exp} {abs(int(coefficients[index]))}{variable}^{power[index]} "                     

def coefficients_ex(coefficients, i):
    if(coefficients[i] > 0):
        return '+'
    elif(coefficients[i] < 0):
        return '-'
    else:
        return ''
        
        
def test_polinomial():
    assert print_polynomial([(2, -6), (0, -8), (1, 34)],'x') == '-6x^2 + 34x - 8' ;print("Pass !!")
    assert print_polynomial([(4, -6), (2, -8), (3, 34)],'x') == '-6x^4 + 34x^3 - 8x^2';print("Pass !!")
    assert print_polynomial([(2, -6), (0, -8), (1, 34)],'y') == '-6y^2 + 34y - 8' ;print("Pass !!")
    assert print_polynomial([(2, 6), (0, -8), (1, 34)],'y') == '6y^2 + 34y - 8' ;print("Pass !!")
    assert print_polynomial([(2, 6.5), (0, -8)],'y') == '6.5y^2 - 8' ;print("Pass !!")
    assert print_polynomial([(4, -6), (2, -8), (3, 34),(6,34),(1,5)],'x') == '34x^6 - 6x^4 + 34x^3 - 8x^2 + 5x' ;print("Pass !!")
    assert print_polynomial([(4, -6), (2, -8), (3, 0)],'x') == '-6x^4 - 8x^2' ;print("Pass !!")
    assert print_polynomial([(0, 0), (1, 1)],'y') == 'y' ;print("Pass !!")
    assert print_polynomial([(0, 0), (1, 0)],'y') == 0 ;print("Pass !!")
    assert print_polynomial([(0, 0), (1, 5)],'y') == '5y' ;print("Pass !!")
    assert print_polynomial([(0, 5), (1, 0)],'y') == '5' ;print("Pass !!")
    assert print_polynomial([(0, 5), (1, 5)],'x') == '5x + 5' ;print("Pass !!")
    assert print_polynomial([(2, -66), (0, -8), (1, 34)],"x")=='-66x^2 + 34x - 8'
    assert print_polynomial([(2, 6), (0, -8), (1, 34)],"y")=='6y^2 + 34y - 8'
    assert print_polynomial([(2, -6), (0, -1), (1, 34)],"x")=='-6x^2 + 34x - 1'
    assert print_polynomial([(2, -6), (0, 1), (1, 34)],"x")=='-6x^2 + 34x + 1'
    assert print_polynomial([(2, 6), (0, 0), (1, 0)],"x")=='6x^2'
    assert print_polynomial([(2, 0), (0, -1), (1, 0)],"x")=='-1'
    assert print_polynomial([(5, 2), (4, -2), (1, 0)],"x")=='2x^5 - 2x^4'
    assert print_polynomial([(5, 1), (4, -1), (0, 1)],"x")=='x^5 - x^4 + 1'
    assert print_polynomial([(0, 1), (1, 1)],"x")=='x + 1'
    assert print_polynomial([(0, 1), (1, -1)],"x")=='-x + 1'
    assert print_polynomial([(1, 0), (0 , -2)],"x")=='-2'
    assert print_polynomial([(2, -100000), (1 , -1),(0 , -1),(3 , -1)],"x")=='-x^3 - 100000x^2 - x - 1'
    assert print_polynomial([(1, 0.0001),(1,0)], "x") == ''
    print('allpass')
    

if __name__ == "__main__":
    main()