#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW10_1
# 204111 Sec 001

def eratosthenes(n, show_step: bool=False):
    list_number = list(range(2, n + 1))
    pir = 2
    index = 0

    while pir ** 2 <= n:
        list_number = list(filter(lambda x: x == pir or x % pir != 0, list_number))
        if show_step:
            print(str(pir) + ':', list_number)
        index += 1
        pir = list_number[index]
    return list_number

if __name__ == '__main__':
    print(eratosthenes(20, True))