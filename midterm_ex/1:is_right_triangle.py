#!usr/bin/env python3
# Ice-lnwza
# 670510662
# Sec 001

def is_right_triangle(a, b, c):
    lists = [a, b, c]
    lists = sorted(lists)
    a = lists[0]
    b = lists[1]
    c = lists[2]
    if a**2 + b**2 == c**2:
        return True
    return False
    
def test_is_right_triangle():
    assert is_right_triangle(1, 2, 3) is False
    assert is_right_triangle(5, 3, 4) is True
    assert is_right_triangle(5, 12, 13) is True
    assert is_right_triangle(5, 13, 13) is False
    print("All tests passed!")



if __name__ == '__main__':
    assert is_right_triangle(3, 4, 5) is True
    print("All OK!")

