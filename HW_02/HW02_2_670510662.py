#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW02_2
# 204111 Sec 001

import math

# รับค่า x, y
x = int(input("x : "))
y = int(input("y : "))

# sum1 = ((y**3)/3) + ((y**2)/2) + (y/6)
# sum2 = (((x-1)**3)/3) + (((x-1)**2)/2) + ((x-1)/6)

# หาผลรวมsumค่า y
sum1 = (y*(y+1)*(2*y+1))/6
# หาผลรวมค่า x
sum2 = ((x-1)*(x)*(2*x-1))/6
# นำผมรวมค่า y - ผลรวมค่า x
sum = sum1-sum2
# แสดงผล
print(f"sum is {math.ceil(sum)}")