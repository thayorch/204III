#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# Lab04_1
# 204111 Sec 001

# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function circle_intersect()
import math 

def main():
    # print(circle_intersect(float(input()), float(input()), float(input()), float(input()), float(input()), float(input())))
    test_circle_intersect()
    

def circle_intersect(x1: float, y1: float, r1: float,
                     x2: float, y2: float, r2: float, epsilon=10**-6) -> int:
    distance = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    k = distance-(r1+r2)
    # print(f"distance : {distance}\nk : {k}")
    if(k < -epsilon):
        return 1
    elif(k >= -epsilon  and k <= +epsilon):
        return 0
    else:
        return -1

def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    print("Pass!!")
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    print("Pass!!")
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1
    print("Pass!!")

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("Spacified Epsilon Pass!!")
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=5) == 0
    print("Spacified Epsilon Pass!!")


if __name__ == '__main__':
    main()
