#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW07_1
# 204111 Sec 001

def main():
    print(print_polynomial([(2, -6), (0, -8), (1, 34)],'x'))
    print(print_polynomial([(4, -6), (2, -8), (3, 34)],'x'))
    print(print_polynomial([(4, -6), (2, -8), (3, 0)],'x'))
    print(print_polynomial([(0, 0),  (1, 1)],'y'))
    print(print_polynomial([(0, 0),  (1, 0)],'y'))
    test_polinomial()


def print_polynomial(pc_list: list[tuple[int, float]], v: str):
   temp = sorted(pc_list ,key =lambda x: x[0],reverse=True)
   power_out = list(map(lambda x: str(x[0]) ,temp))  
   coefficients_out = list(map(lambda x: str(x[1]),temp))
   lists = list(map(lambda i:  check_lists(power_out,coefficients_out, v, i), range(len(temp))))
   return ''.join(lists).strip()
   
def check_lists(power, coefficients, variable, index):
    exp = coefficients_ex(coefficients, index)
    if(coefficients[index] == '0' and power[index] != '0'):  
        return ''
    
    if(power[index] == max(power) and power[index] != '1' and power[index] != '0'):   
        return f"{coefficients[index]}{variable}^{power[index]} "
    
    elif(power[index] == '1'):                                
        if(coefficients[index] == '1'):                        
            return f"{variable} "
        
        if(coefficients[index-1] == '0'):
            return f"{coefficients[index]}{variable} "
        
        else:                                                
            return f"{exp} {coefficients[index]}{variable} "
        
        
        
    elif(power[index] == '0'):                                            
        if(coefficients[index-1] != '0'  and coefficients[index] != '0'): 
            return f"{exp} {abs(int(coefficients[index]))} "
        elif(coefficients[index-1] != '0'  and coefficients[index] == '0'): 
            return ''
        
        if(coefficients[index-1] == '0'): 
            return f"{coefficients[index]}"


    else:
        return f"{exp} {abs(int(coefficients[index]))}{variable}^{power[index]} "
    
        
    
    
                                 

def coefficients_ex(coefficients, i):
    if(float(coefficients[i]) > 0):
        return '+'
    elif(float(coefficients[i]) < 0):
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
    assert print_polynomial([(0, 0), (1, 0)],'y') == '0' ;print("Pass !!")
    

if __name__ == "__main__":
    main()