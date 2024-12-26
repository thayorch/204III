#!/usr/bin/env python3
# Ice-lnwza
# 670510662
# Sec 001


def count_4n5(n):
    return len(list(filter(lambda x: '4' in str(x) and '5' in str(x) , range(n+1))))


if __name__ == '__main__':
    print(count_4n5(99))
    # assert count_4n5(45) == 1
    # print("All OK!")
