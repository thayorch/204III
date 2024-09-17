#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab12_2
# 204111 Sec 001
    
def multiply_polynomials(p1: list[int], p2: list[int]) -> list[int]:
    result = [0] * (len(p1) + len(p2) - 1) 
    for i in enumerate(p1):
        for j in enumerate(p2):
            result[i[0] + j[0]] += i[1] * j[1]
    return result
    
if __name__ == '__main__':
    print(multiply_polynomials([2, 0, 3],[4, 5])) 
