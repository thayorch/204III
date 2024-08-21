#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW03_3
# 204111 Sec 001

def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print(set_kth_digit(x, y, z))

def kth_digit(number: int, k: int) -> int :
    return (abs(number) // (10 ** k)) % 10

def set_kth_digit(number: int, k: int, value: int) -> int:
    digit_number = kth_digit(abs(number), k)
    return (abs(number) - (digit_number*(10**k))) + ((value)*(10**k))

if __name__ == '__main__':
    main()