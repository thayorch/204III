#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW06_1
# 204111 Sec 001

def main():
    # print(uniform('HaPpY'))
    t()
    
def uniform(line: str)->str:
    
    list_upper = filter(upper_count_status, list(line))
    list_lower = filter(lower_count_status, list(line))
    upper_count = len(list(list_upper))
    lower_count = len(list(list_lower))
    
    if upper_count>lower_count:
        return line.upper()
    elif lower_count>upper_count:
        return line.lower()
    else:
        return first_index_return(line)
    

def upper_count_status(line):
    if(line.isupper()):
        return True
    else:
        return False

def lower_count_status(line):
    if(line.islower()):
        return True
    else:
        return False
    
def first_index_return(line):
    if(line[0].isupper()):
        return line.upper()
    else:
        return line.lower()

def t():
    assert uniform('HaPpY') == 'HAPPY'
    assert uniform('helLo') == 'hello'
    assert uniform('aaaAAA') == 'aaaaaa'
    print("Pass!!")

if __name__ == '__main__':
    main()