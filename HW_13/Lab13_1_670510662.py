#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab13_1
# 204111 Sec 001

def matrix_mult(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]] :
    if not m1[0] or not m2[0]:
        return None
    
    m1dim = all(len(row) == len(m1[0]) for row in m1)
    m2dim = all(len(row) == len(m2[0]) for row in m2)

    if not m1dim or not m2dim : return None

    if len(m1[0]) != len(m2):
        return None

    else:
        result = []
        for i in range(len(m1)): 
            row = [] 
            for j in range(len(m2[0])):  
                row.append(0)  
            result.append(row) 

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    result[i][j] += m1[i][k] * m2[k][j]
        
        return result
        

if __name__ == '__main__':
    m1 = list(input())
    m2 = list(input())
    print(matrix_mult(m1,m2))
