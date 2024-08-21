#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# Lab03_1
# 204111 Sec 001

import math

def main():
    # รับค่า พท.ผิว
    serface_area = int(input("input surface area: "))
    # แสดงค่าปริมาตรทรงกลม
    print(f"volume = {sphere_volume(find_r_from_surface_area(serface_area)):.2f}")

# หาค่า r จากพท.ผิว
def find_r_from_surface_area(surface_area: float) -> float :
    return math.sqrt(surface_area/(4*math.pi))

# คำนวณหาค่าปริมาตร
def sphere_volume(radius: float):
    return ((4/3)*math.pi*(radius**3))

if __name__ == '__main__':
    main()