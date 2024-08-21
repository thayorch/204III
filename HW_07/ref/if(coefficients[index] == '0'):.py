if(coefficients[index] == '0'):
        if(power[index] == '0'):
            return '0'
        else:
            return ''
    elif(power[index] == '0' and coefficients[index] != '0'):
        if(int(coefficients[index]) > 0):
            return f"{'+ '+''.join(str(abs(int(coefficients[index]))))} " 
        elif(int(coefficients[index]) < 0):
            return f"{'- '+''.join(str(abs(int(coefficients[index]))))} "
    elif(power[index] == '1'):
        if(coefficients[index] == '1'):
            return f"{variable} "  
        elif(int(coefficients[index]) > 0):
            return f"{'+ '+''.join(coefficients[index])}{variable} " 
        elif(int(coefficients[index]) < 0):
            return f"{'- '+''.join(coefficients[index])}{variable} "
        else:
            return ''
    
    elif(power[index] == max(power)):
        return f"{''.join(coefficients[index])}{variable}^{''.join(power[index])} " 
    else:
        if(int(coefficients[index]) > 0):
            return f"{'+ '+''.join(str(abs(int(coefficients[index]))))}{variable}^{''.join(power[index])} " 
        elif(int(coefficients[index]) < 0):
            return f"{'- '+''.join(str(abs(int(coefficients[index]))))}{variable}^{''.join(power[index])} "