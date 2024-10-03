#!usr/bin/env python3
# Thadchanon Maidee(Ice-lnwza)
# 670510662
# HW14_3
# 204111 Sec 001

from string import ascii_lowercase
from functools import reduce 

def radix_word(list_x: list[str], show_step: bool = False) -> None:

    for i in range(max([len(x) for x in list_x]) - 1, -1, -1):
        d = {}

        for word in list_x:
            if len(word) <= i:
                d[' '] = d.get(' ', [])
                d[' '].append(word)
            else:
                d[word[i]] = d.get(word[i], [])
                d[word[i]].append(word)

        keys_word = d.keys()
        rad_word = [d[key] if key in keys_word else [] for key in ' ' + ascii_lowercase]
        list_x[:] = reduce(lambda x, y: x + y, rad_word)

        if show_step:
            print(list_x)



if __name__ == '__main__':
    list_x = ['beer', 'wine', 'vinegar', 'vodka']
    radix_word(list_x, True)
    print('--------')
    print(list_x)