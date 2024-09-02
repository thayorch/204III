#!/usr/bin/env python3
# @Author: kk
# @Last Modified time: 2022-09-24 21:16:41

cat = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''


def main():
    # print(cat_altar(int(input())))
    n=1
    for i in range(len(cat_altar(n).split('\n'))):
        print("".join(cat_altar(n).split('\n')[i]))
    
    # print(cat_altar(3))


def cat_altar(n):
    return cat*n


if __name__ == '__main__':
    main()
