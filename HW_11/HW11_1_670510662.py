# usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW11_1
# 204111 Sec 001


unit_list = {
    "zero":0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
    'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
    'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,'eighty': 80, 'ninety': 90, 'hundred': 100
}

thousand = {
    'thousand': 1000, 'million': 10 ** 6, 'billion': 10 ** 9
}

def words_to_num(words):
    words = words.replace('-', ' ')
    for sep in thousand:
        words = words.replace(sep, sep + ',')
    words = list(map(lambda i: i.split(), filter(lambda j: j, words.split(','))))
    # print(words)
    numbers = list(map(lambda j: list(map(lambda i: unit_list[i] if i in unit_list else thousand[i], j)), words))

    for i in numbers:
        while len(i) > 1:
            if i[0] < i[1]:
                i[0] = i[0] * i[1]
                del i[1]
            else:
                i[0] = i[0] + i[1]
                del i[1]
    # print(numbers)

    return sum(map(lambda x:x[0],numbers))

if __name__ == "__main__":
    print(words_to_num("fourteen"))
    print(words_to_num("two hundred forty-eight"))
    print(words_to_num("one hundred eleven "))
    print(
        words_to_num(
            """forty-two billion six hundred forty-one
million three hundred twenty-three
thousand eight hundred sixty-two"""
        )
    )

