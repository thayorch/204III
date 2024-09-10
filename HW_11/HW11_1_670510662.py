#usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW11_1
# 204111 Sec 001

unit_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_list = ['', '', "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
thousands_list = ["", "thousand", "million", "billion"]


def words_to_num(words):
    setter = words.split()
    for i in range(len(setter)):
        if "-" in setter[i]:
            print(setter[i])
        else:
            continue
    return        

if __name__ == "__main__":
    print(words_to_num('fourteen'))
    print(words_to_num('two hundred forty-eight'))
    print(words_to_num('one hundred eleven '))
    print(words_to_num('''forty-two billion six hundred forty-one
million three hundred twenty-three
thousand eight hundred sixty-two'''))