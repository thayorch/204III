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

def three_digits_to_word(n: int) -> str:
    if(n == 0):
        return ""
    if(n < 20):
        return unit_list[n]
    if(n < 100):
        return tens_list[n // 10] + ("-" + unit_list[n % 10] if (n % 10 != 0) else "")
    return unit_list[n // 100] + " hundred" + (" " + three_digits_to_word(n % 100) if (n % 100 != 0) else "")


def num_to_word(num: int) -> str:
    if (num == 0):
        return "zero"
    if(num < 1000):
        return three_digits_to_word(num)
    else:        
        split_number =  list(reversed(spliter(num))) 
        # return split_number
        lists = list(map(lambda x: " " +(three_digits_to_word(x) + " " + thousands_list[split_number.index(x)]).strip(), split_number))
        lists = list(reversed(lists))
        return ''.join(lists).strip()

def spliter(number):
        if number == 0:
            return []
        else:
            return spliter(number // 1000) + [number % 1000]

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