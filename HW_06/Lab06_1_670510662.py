#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab06_1
# 204111 Sec 001

def main():
    print(triangle(9))
    # test_triangle()

def triangle(n):
    lists_1 = list(range(1, n+1)) # [1, 2, 3, 4]
    lists_2 = list(map(lambda x: str(list(list_dot(x) if(check_map(x,n)) else list_star(x))) , lists_1))
    
    return lists_2
    # lists_2 = list(map(lambda n: ,lists_2)) 
    # lists_2 = list(map(lambda x: str(lists_2), lists_2))
    
    triangle_list = '\n'.join(lists_2).replace(',','').replace(' ','').replace('\'','').replace('[','').replace(']','').replace('\"','').replace('#',' ')+'\n'
    return triangle_list

def list_dot(x):
    # return list(map(lambda j: j,range((2*x)-1)))
    list_j = list(map(lambda j: j,range((2*x)-1)))
    return list(map(lambda i: dot_con(i,list_j),list_j))

    
def list_star(x):
    # return '* '*((2*x)-1)
    list_j = list(map(lambda j: j,range((2*x)-1)))
    # return list_j
    return list(map(lambda i: '*' if(i%2==0) else '#' ,list_j))

def dot_con(i,list_j):
    if(i==0):
        return '*'
    elif(i==len(list_j)-1):
        return '*'
    else:
        return '.'

def check_map(x: int, n: int):
    if x != 1 and x != n:
        return True
    


def test_triangle():

    T3 = '''*
*.*
* * *
'''

    T7 = '''*
*.*
*...*
*.....*
*.......*
*.........*
* * * * * * * \n
'''

    assert triangle(3) == T3
    assert triangle(7) == T7
    print("OK")


if __name__ == '__main__':
    main()