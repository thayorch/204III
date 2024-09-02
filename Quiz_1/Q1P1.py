#!usr/bin/env python3
# Ice-lnwza

import math
def cal_area(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
    a = d((x1, y1), (x2, y2))
    b = d((x2, y2), (x3, y3))
    c = d((x3, y3), (x1, y1))
    
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def d(p,q):
    return math.sqrt((q[0]-p[0])**2 + (q[1]-p[1])**2)
    
    
def test_cal_area():
    epsilon = 10**-4
    assert math.isclose(cal_area(0, 9, 0, 5, 6, 7), 12.0, abs_tol=epsilon)
    assert math.isclose(cal_area(6, -9, -8, 4, 8, -7), 27.0, abs_tol=epsilon)
    assert math.isclose(cal_area(8, -7, 1, 5, 2, -9), 43.0, abs_tol=epsilon)
    assert math.isclose(cal_area(6, -3, 7, -9, 6, 2), 2.5, abs_tol=epsilon)
    assert math.isclose(cal_area(3, 1, 10, -8, -8, -9), 84.5, abs_tol=epsilon)
    print("All OK!")


if __name__ == '__main__':
    test_cal_area()
