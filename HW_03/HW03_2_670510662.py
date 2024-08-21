#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# HW03_2
# 204111 Sec 001

def main():
    x  = int(input())
    y  = int(input())
    print(kth_digit(x, y))

def kth_digit(number: int, k: int) -> int :
    return (abs(number) // (10 ** k)) % 10

if __name__ == '__main__':
    main()