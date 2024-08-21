#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW02_1
# 204111 Sec 001

# รับค่า m1, b1, m2, b2
m1 = float(input('m1 : '))
b1 = float(input('b1 : '))
m2 = float(input('m2 : '))
b2 = float(input('b2 : '))

# แทนค่าในสมการหาจุดตัด
X = (b2-b1)/(m1-m2)
Y = m1*X+b1

# แสดงผล
print(f"Lines intersect at ({X:.2f},{Y:.2f})")