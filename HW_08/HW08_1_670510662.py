#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW08_1
# 204111 Sec 001

from math import isclose
def main():
    # print(pi(0))
    # print(pi(2))
    # print(pi(5))
    
    test_pi()
    # pass


# 4 / (2x * 2x+1 * 2x+2)
# คี่ == + | คู่ == - 
def pi(n):
    def avr_decimal(n, avr):
        if n < 1:
            return avr
        term = (4 / ((2*n) * (2*n+1) * (2*n+2)))
        if n % 2 == 0:
            avr -= term
        if n % 2 != 0:
            avr += term
        return avr_decimal(n-1, avr)
    
    return 3+avr_decimal(n, 0)


def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("All OK!")


if __name__ == '__main__':
    main()
