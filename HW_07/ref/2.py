 exp = coefficients_ex(coefficients, index)
    if(coefficients[index] == '0'):   #  0 x var
        return ''
    
    
    if(coefficients[index]=='1' and power[index] != '0' and power[index] != '1'):
        return f"{variable}^{power[index]} "
    
    if(power[index] == max(power) and power[index] != '1' and power[index] != '0'):   
        return f"{coefficients[index]}{variable}^{power[index]} "
    
    elif(power[index] == '1'):                                 # coe * var = 2var
        if(coefficients[index] == '1'):                        # 1 * var = var
            return f"{exp} {variable} "
        
        if(coefficients[index-1] == '0'):
            return f"{exp} {coefficients[index]}{variable} "
        
        else:                                                  # 2 * var = 2var
            return f"{exp} {coefficients[index]}{variable} "
        
    elif(power[index] == '0'):                                 # var**0                       
        
        if(coefficients[index] != '0' and coefficients[index] != '1'): 
            return f"{exp} {abs(int(coefficients[index]))}"
        elif(coefficients[index-1] != '0'  and coefficients[index] == '0'): 
            return ''
        else: 
            return f"{exp} {coefficients[index]}"


    else:
        return f"{exp} {abs(int(coefficients[index]))}{variable}^{power[index]} "                     

def coefficients_ex(coefficients, i):
    if(float(coefficients[i]) > 0):
        return '+'
    elif(float(coefficients[i]) < 0):
        return '-'
    else:
        return ''