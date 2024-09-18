#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab12_1
# 204111 Sec 001

from math import ceil, floor

def display_calendar(month: int, year: int) -> None:
    
    _1stday = gregorian(month, year)
    total_day = days(month, year)
    row = ceil((_1stday + total_day) / 7) + 1
    after1st_day = list(range(1, total_day + 1))

    counter = 0
    
    for i in range(row):
        if i == 0:
            print('Su Mo Tu We Th Fr Sa')
        else:
            for j in range(7):
                if counter < _1stday:
                    print('--', end=' ')
                    counter += 1

                else:
                    if counter >= len(after1st_day) + _1stday:
                        break
                    if counter < _1stday + 9:
                        print(' ' + str(after1st_day[counter - _1stday]), end=' ')
                        counter += 1
                        continue
                    print(after1st_day[counter - _1stday], end=' ')
                    counter += 1
            print('')


def gregorian(month: int, year: int):
    m = month
    Y = year
    
    if m <= 2:
        m += 12
        Y -= 1
    K = Y % 100
    J = floor(Y / 100)

    h = (1 + floor((13 * (m + 1)) / 5) + K + floor(K / 4) + floor(J / 4) - 2 * J) % 7
    
    if h == 0 : 
        return 6
    return h - 1


def leap_year(year: int):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def days(month:int, year:int):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if leap_year(year) == True:
            return 29
        return 28


if __name__ == '__main__':    
    display_calendar(2, 2024)
    # display_calendar(2, 2021)
    # display_calendar(2, 2022)
    # display_calendar(2, 2023)
    # display_calendar(2, 2024)
