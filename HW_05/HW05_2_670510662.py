#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW05_2
# 204111


def main():
    print(roman_numeral(int(input())))
    # test_roman()
def roman_numeral(n: int) -> str:
    if n >= 1000:
        return "M" + roman_numeral(n-1000)
    elif n >= 900:
        return "CM" + roman_numeral(n-900)
    elif n >= 500:
        return "D" + roman_numeral(n-500)
    elif n >= 400:
        return "CD" + roman_numeral(n-400)
    elif n >= 100:
        return "C" + roman_numeral(n-100)
    elif n >= 90:
        return "XC" + roman_numeral(n-90)
    elif n >= 50:
        return "L" + roman_numeral(n-50)
    elif n >= 40:
        return "XL" + roman_numeral(n-40)
    elif n >= 10:
        return "X" + roman_numeral(n-10)
    elif n >= 9:
        return "IX" + roman_numeral(n-9)
    elif n >= 5:
        return "V" + roman_numeral(n-5)
    elif n >= 4:
        return "IV" + roman_numeral(n-4)
    elif n >= 1:
        return "I" + roman_numeral(n-1)
    return ""

def test_roman():
    assert roman_numeral(1) == 'I'
    assert roman_numeral(4) == 'IV'
    assert roman_numeral(5) == 'V'
    assert roman_numeral(9) == 'IX'
    assert roman_numeral(10) == 'X'
    assert roman_numeral(40) == 'XL'
    assert roman_numeral(50) == 'L'
    assert roman_numeral(90) == 'XC'
    assert roman_numeral(100) == 'C'
    assert roman_numeral(400) == 'CD'
    assert roman_numeral(500) == 'D'
    assert roman_numeral(900) == 'CM'
    assert roman_numeral(1000) == 'M'
    assert roman_numeral(4999) == 'MMMMCMXCIX'
    print("Passed!!")

if __name__ == '__main__':
    main()