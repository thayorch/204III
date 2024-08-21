#!/usr/bin/env python3
# Ice-lnwza
# 670510662
# Sec 001

from math import isclose,log2

def log2_list(list_a):
    list_a[:] = list(map(lambda x: log2(x), list_a))
    pass
    
if __name__ == '__main__':

    list_a = [1, 2, 4]
    # list_a = log2_list(list_a)
    
    # print(log2(list_a[1]))
    print(log2_list(list_a))
    assert all(map(lambda x, y: isclose(x, y, abs_tol=0.001),
                   list_a, [0.0, 1.0, 2.0]))

    print("All OK!")