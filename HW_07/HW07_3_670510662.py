#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW07_3
# 204111 Sec 001

unit_list = [ '' , "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_list = ['', '', "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
thousands_list = ["", "thousand", "million", "billion"]



def main():
    print(num_to_word(1))
    print(num_to_word(248))
    print(num_to_word(111))
    print(num_to_word(10))
    print(num_to_word(42641323862))
    print(num_to_word(999999))
    print(num_to_word(1000))
    
    # for i in range(10000):
        # print(i, num_to_word(i))
    test()

def num_to_word(n: int) -> str:
    if n == 0:
        return 'zero'
    length_num = str(n)

    # count digits
    if len(length_num) <= 3:
        # xxx
        result = three_digits_to_word(n)
    elif len(length_num) <= 6:
        # xxx,xxx
        result = three_digits_to_word(n // 1000) + ' thousand ' + three_digits_to_word(n % 1000)
    elif len(length_num) <= 9:
        # xxx,xxx,xxx
        if (n % (10 ** 6)) // 1000 == 0:
            # xxx,xxx,000
            result = three_digits_to_word(n // (10 ** 6)) + ' million ' + three_digits_to_word(n % 1000)
        else:
            result = (
                    three_digits_to_word(n // (10 ** 6)) + ' million '
                    + three_digits_to_word((n % (10 ** 6)) // 1000)
                    + ' thousand ' + three_digits_to_word(n % 1000)
            )
    else:
        # xxx,xxx,xxx,xxx
        result = ten_dit_to_twelve(n)

    return result.strip()


def ten_dit_to_twelve(n: int) -> str:
    tuple_three_dit_word = tuple(map(three_digits_to_word, slic_num(n)))
    # tuple of (xxx,xxx,xxx,xxx)
    if slic_num(n)[1] == 0:
        if slic_num(n)[2] == 0:
            if slic_num(n)[3] == 0:
                # xxx,000,000,000
                return tuple_three_dit_word[0] + ' billion'
            # xxx,000,000,xxx
            return tuple_three_dit_word[0] + ' billion ' + tuple_three_dit_word[3]
        else:
            # xxx,000,xxx,xxx
            return tuple_three_dit_word[0] + ' billion ' + tuple_three_dit_word[2] + ' thousand ' + tuple_three_dit_word[3]
    else:
        if slic_num(n)[2] == 0:
            # xxx,xxx,000,xxx
            return tuple_three_dit_word[0] + ' billion ' + tuple_three_dit_word[1] + ' million ' + tuple_three_dit_word[3]
        # xxx,xxx,xxx,xxx
        return tuple_three_dit_word[0] + ' billion ' + tuple_three_dit_word[1] + ' million ' + tuple_three_dit_word[2] + ' thousand ' + tuple_three_dit_word[3]


def slic_num(a: int) -> tuple:
    list_a = list(str(a))
    if len(list_a) == 10:
        # x,xxx,xxx,xxx
        raw_tuple_data = list_a[0], ''.join(list_a[1:4]), ''.join(list_a[4:7]), ''.join(list_a[7:])
        int_raw_data = tuple(map(int, raw_tuple_data))
        return int_raw_data
    if len(list_a) == 11:
        # xx,xxx,xxx,xxx
        raw_tuple_data = ''.join(list_a[:2]), ''.join(list_a[2:5]), ''.join(list_a[5:8]), ''.join(list_a[8:])
        int_raw_data = tuple(map(int, raw_tuple_data))
        return int_raw_data
    if len(list_a) == 12:
        # xxx,xxx,xxx,xxx
        raw_tuple_data = ''.join(list_a[:3]), ''.join(list_a[3:6]), ''.join(list_a[6:9]), ''.join(list_a[9:])
        int_raw_data = tuple(map(int, raw_tuple_data))
        return int_raw_data


def three_digits_to_word(num: int) -> str:
    hundred, ten, one = div(num)
    return data(hundred, ten, one)


def data(hundred: int, ten: int, one: int) -> str:
    """" change from number to word    """
    str_0_to_9 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    str_10_to_19 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                    'nineteen']
    str_20_to_99 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if hundred == 0:
        # x < 100
        if ten == 0:
            # x < 10
            return str_0_to_9[one]
        else:
            # 10 <= x <= 19
            if ten == 1:
                return str_10_to_19[one]
            else:
                # x%10 == 0
                if one == 0:
                    return str_20_to_99[ten]
                else:
                    # x%10 != 0 and 20<= x <= 99
                    return str_20_to_99[ten] + '-' + str_0_to_9[one]
    else:
        if ten == 0 and one == 0:
            # x%100 == 0
            return str_0_to_9[hundred] + ' hundred'
        else:
            if ten == 1:
                # x hundred and {10 -> 19}
                return str_0_to_9[hundred] + ' hundred ' + str_10_to_19[one]
            elif ten == 0:
                # x hundred qnd {0 -> 9}
                return str_0_to_9[hundred] + ' hundred ' + str_0_to_9[one]
            else:
                if one == 0:
                    # x hundred and {20 -> 99}
                    return str_0_to_9[hundred] + ' hundred ' + str_20_to_99[ten]
                else:
                    # x hundred and xty-x
                    return str_0_to_9[hundred] + ' hundred ' + str_20_to_99[ten] + '-' + str_0_to_9[one]

def div(n: int) -> tuple:
    number = n
    rem1 = 100
    hundred, rem = divmod(number, rem1)
    rem2 = 10
    ten, one = divmod(rem, rem2)
    # x*100 + y*10 + z -> (x,y,z)
    return hundred, ten, one

def test():
    assert num_to_word(0) == 'zero' ;print("pass")
    assert num_to_word(14) == 'fourteen' ;print("pass")
    assert num_to_word(248) == 'two hundred forty-eight';print("pass")
    assert num_to_word(101) == 'one hundred one';print("pass")
    assert num_to_word(111) == 'one hundred eleven';print("pass")
    assert num_to_word(200) == 'two hundred';print("pass")
    assert num_to_word(999999) == "nine hundred ninety-nine thousand nine hundred ninety-nine";print("pass")
    assert num_to_word(42641323862) == "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two";print("pass")
    print("!! ALL PASS !!")


if __name__ == '__main__':
    main()