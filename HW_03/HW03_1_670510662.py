#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW03_1
# 204111 Sec 001

import math

def main():
    test_nearest_odd()
    # print(nearest_odd(float(input())))

# implement ฟังก์ชันนี้ให้ถูกต้อง
def  nearest_odd(x: float) -> int:
    return (math.ceil(x)) - ((math.ceil(x)%2 - 1) %2)


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_nearest_odd() -> None:
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    assert nearest_odd(9.6) == 9
    print("All OK!")


if __name__ == '__main__':
    main()