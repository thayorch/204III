#!usr/bin/env python3 
# Thadchanon Maidee(Ice-lnwza)
# 670510662
# HW15_3
# 204111 Sec 001

# (px, py, r)
# Q1 (+,+)
# Q2 (-,+)
# Q3 (-,-)
# Q4 (+,-)

def count_segment(list_a: list[tuple[float]]) -> tuple[int]:
    q1,q2,q3,q4 = 0,0,0,0 
    # print(px, py, r)
    for index in list_a:
        px, py, r = index
        zero_radius = ((px**2) + (py**2))**(1/2)
        # print(zero_radius) 
        if px > 0 and py > 0:   #Q1
            q1 += 1
            if px - r < 0:
                q2 += 1
            if py - r < 0:
                q4 += 1 
            if zero_radius < r:
                q3 += 1
        elif px < 0 and py > 0:   #Q2
            q2 += 1
            if px + r > 0:
                q1 += 1
            if py - r < 0:
                q3 += 1
            if zero_radius < r:
                q4 += 1
        elif px < 0 and py < 0:   #Q3
            q3 += 1
            if px + r > 0:
                q4 += 1
            if py + r > 0:
                q1 += 1
            if zero_radius < r:
                q2 += 1
        elif px > 0 and py < 0:   #Q4
            q4 += 1
            if px - r < 0:
                q3 += 1
            if py + r > 0:
                q1 += 1
            if zero_radius < r:
                q2 += 1

        elif px < 0 and py == 0:
            if py + r > 0:
                q2 += 1
            if py - r < 0:
                q3 += 1
            if zero_radius < r:
                q1 += 1
                q4 += 1

        elif px > 0 and py == 0:
            if py + r > 0:
                q1 += 1
            if py - r < 0:
                q4 += 1
            if zero_radius < r:
                q2 += 1
                q3 += 1

        elif px == 0 and py < 0:
            if px + r > 0:
                q4 += 1
            if px - r < 0:
                q3 += 1
            if zero_radius < r:
                q1 += 1
                q2 += 1
        elif px == 0 and py > 0:
            if px + r > 0:
                q1 += 1 
            if px - r < 0:
                q2 += 1
            if zero_radius < r:
                q3 += 1
                q4 += 1
        else:
            q1 += 1
            q2 += 1
            q3 += 1
            q4 += 1
    # print(q1,q2,q3,q4)
    return (q1, q2, q3, q4)

if __name__ == "__main__":
    count_segment([(0,0,1)])
    # list_x = [(2, 7, 1.5), (3.2, 2.5, 4.06), (-5.5, -4.5, 2.5), (2, -5.2, 3), (7.2, -2.8, 1.2)]
    # print(count_segment(list_x))
    # assert count_segment([(2, 7, 1.5),(3.2, 2.5, 4.06),(-5.5, -4.5, 2.5),(2, -5.2, 3),(7.2, -2.8, 1.2)]) == (2,1,2,3)
