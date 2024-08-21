#!/usr/bin/env python3
# Ice-lnwza
# 670510662
# Sec 001

from math import isclose
# H.M = n / [ (1/x[0]) + (1/x[1]) + (1/x[2]) + (1/x[3]) + ... ]
def harmonic_mean(list_a):
    return len(list_a)/sum(list(map(lambda i: 1/list_a[i], range(len(list_a)))))

if __name__ == '__main__':
    print(harmonic_mean([1,2,2,2]))
    assert isclose(harmonic_mean([1, 2, 2, 2]), 1.6, abs_tol=0.001)
    print("All OK!")
