#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW06_3
# 204111 Sec 001

def main():
    # print(moving_average([1,2,3,4,5],3))
    test_moving_average()
    
    # len(list_x) : 5
    # [0, 1, 2, 3, 4, 5]
    # 
    # 5 - winsize(2) : 3
    # 
    
def moving_average(list_x: list[float], win_size: int) -> list[float]:
    return list(map(lambda i: sum(list_x[i:i+win_size]) / win_size , list(range(0, (len(list_x)+1)-win_size))))

def test_moving_average():
    assert moving_average([1,2,3,4,5],2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average([1,2,3,4,5],3) == [2.0, 3.0, 4.0]
    print("All passed!!")
if __name__ == '__main__':
    main()