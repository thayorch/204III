#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# Lab02_1
# 204111 Sec 001

import math
# รับค่า a, b, c 
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
# แทนคำคำนวณในสมการ
S = (a+b+c)/2
sum = math.sqrt(S*(S-a)*(S-b)*(S-c))
# แสดงผล
print(math.ceil(sum))