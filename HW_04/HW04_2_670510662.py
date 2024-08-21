#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW04_2
# 204111 Sec 001

def main():
    # print(minute_diff(int(input()),int(input()),str(input()), int(input()),int(input()),str(input())))
    test_minute_diff()

# implement this function
def minute_diff(h1: int, m1: int, p1: str,
                h2: int, m2: int, p2: str) -> int:
 
    if(p1 == 'PM' and h1!=12 and h1>=1 and h1<=12 and m1>=0 and m1<=59):
        h1 += 12
    elif(p1 == 'AM' and h1 == 12 and h1>=1 and h1<=12 and m1>=0 and m1<=59):
        h1 = 0
    
    if(p2 == 'PM' and h2!=12 and h2>=1 and h2<=12 and m2>=0 and m2<=59):
        h2 += 12
    elif(p2 == 'AM' and h2 == 12 and h2>=1 and h2<=12 and m2>=0 and m2<=59):
        h2 = 0
        
    diff1 = (h1 * 60) + m1
    diff2 = (h2 * 60) + m2
    
    return abs(diff2-diff1)

# test function
def test_minute_diff():
    assert minute_diff(8, 23, 'AM', 8, 24, 'AM') == 1
    assert minute_diff(8, 23, 'AM', 1, 24, 'PM') == 301
    assert minute_diff(1, 24, 'PM', 8, 23, 'AM') == 301
    assert minute_diff(12, 0, 'PM', 12, 0, 'PM') == 0
    
if __name__ == '__main__':
    main()
    
    