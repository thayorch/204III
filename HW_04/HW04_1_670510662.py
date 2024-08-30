#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW04_1
# 204111 Sec 001

import math
def main():
    test()
    # print(calculate_exp(int(input()), int(input())))

def calculate_exp(p: int, c: int) ->int:
    sum_candy = p+c-2       # ผลรวมpidgeyและcandy ลบออกด้วย pidgey, candy ที่ได้รอบสุดท้าย 
    exp = 0
    if(p==0):
        return 0
    # candy มีมากพอที่จะ evolve ทุกตัว
    if((sum_candy//11)<p):
        exp=(sum_candy//11)*1000
    else:                
        exp= p*1000        
        
    return exp
        
def test():
    assert calculate_exp(1,12)==1000 # มีcandy เพียงพอในการ evolve 1 ครั้ง
    print("Case Passed!!")
    assert calculate_exp(2,12)==1000 # มีcandy เพียงพอในการ evolve 1 ครั้ง
    print("Case Passed!!")
    assert calculate_exp(2,22)==2000 # evolve รอบแรกแล้วนำ Pidgeotto ไปแลกแคนดี้ เพื่อให้เพียงพอต่อการ evolve ตัวที่สอง
    print("Case Passed!!")
    assert calculate_exp(20,1) == 1000
    print("Case Passed!!")
    assert calculate_exp(20,11) == 2000
    print("Case Passed!!")
    assert calculate_exp(1,12) == 1000
    print("Case Passed!!")
    assert calculate_exp(11,12) == 1000
    print("Case Passed!!")
    assert calculate_exp(24,0) == 2000
    print("Case Passed!!")
    assert calculate_exp(13,0) == 1000
    print("Case Passed!!")
    assert calculate_exp(2,12) == 1000
    print("Case Passed!!")
    assert calculate_exp(2,22) == 2000
    print("Case Passed!!")
    assert calculate_exp(120,0) == 10000
    print("Case Passed!!")
    assert calculate_exp(6,62) == 6000
    print("Case Passed!!")
    assert calculate_exp(6,61) == 5000
    print("Case Passed!!")
    assert calculate_exp(1200,0) == 108000
    print("Case Passed!!")
    assert calculate_exp(0,0) == 0
    print("Case Passed!!")

    

    
if __name__ =='__main__':
    main()