#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# Lab03_2
# 204111 Sec 001

import math
def main():
    x = int(input())
    print(f"{rectangle_area(x):.2f}")
   
def rectangle_area(x: float):
    return ((2/7)*math.sqrt(5)*x)**2

if __name__ == '__main__':
    main()