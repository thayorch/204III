#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW04_3
# 204111 Sec 

def main():
    test_is_overlapped()


def is_overlapped(l1: float, t1: float, w1: float, h1: float,
                  l2: float, t2: float, w2: float, h2: float) -> bool:
    
    if(l2+w2>l1+w1 and l2+w2>l1 and l2>l1+w1 and l2>l1) or  \
    (l1+w1>l2+w2 and l1+w1>l2 and l1>l2+w2 and l1>l2) or \
    (t2+h2>t1+h1 and t2+h2>t1 and t2>t1+h1 and t2>t1) or (t1+h1>t2+h2 and t1+h1>t2 and t1>t2+h2 and t1>t2):
        return False
    else: 
        return True   


def test_is_overlapped():
    assert is_overlapped(10, 10, 50, 75, 30, 55, 60, 60) is True ;print("Passed !!")
    assert is_overlapped(10, 10, 50, 75, 70, 55, 60, 60) is False; print("Passed !!")

if __name__ == "__main__":
    main()