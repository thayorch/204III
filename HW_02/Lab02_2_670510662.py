#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# Lab02_2
# 204111 Sec 001

# 1 Day = 24 Hour = 1440 min = 86400 s 
# 1 Hour = 60 min  

# รับค่ามิลลิวินาที
msIn = int(input("ms:"))
# ผลหลักมิลลิวินาที
ms = msIn % 1000
sIn = msIn // 1000
# ผลหลักวินาที
s = sIn % 60
# ผลหลักนาที
minIn = sIn // 60
min = minIn % 60
# ผลหลักวัน
day = minIn // 1440
# ผลหลักชม.
hour = (minIn // 60) - (day*24)
# แสดงผล
print(f"{day} day(s), {hour} hour(s), {min} minute(s), {s} second(s), and {ms} millisec(s)")