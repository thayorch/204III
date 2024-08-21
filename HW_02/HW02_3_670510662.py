#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW02_3
# 204111 Sec 001

# รับค่าราคาเดิม
oldPrice = float(input("Old price: "))
# แทนค่าและคำนวณในสมการ
newPrice = (((oldPrice-50)//100)*100)+98
# แสดงผล
print(f"New Price: {int(newPrice)}")