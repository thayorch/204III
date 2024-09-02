#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW10_EX
# 204111 Sec 001

cat = \
    ''' ／|、    
(°、。7   
 |、 ~ヽ  
 ᒐᒐ_f_ )ノ
__________'''

def main():
    # print(cat_altar(int(input())))
    print(cat_altar(1))
    print(cat_altar(2))
    print(cat_altar(3))
    print(cat_altar(4))
    # print(cat_altar(5))
    # print(cat_altar(6))


def cat_altar(n):
    result: str = ''
    altar = list(range(1, n)) + list(range(n, 0, -1))
    for line in range(5 * n, 0, -1):
        for i, cat in enumerate(altar, 1):
            if line - 1 < cat * 5:
                
                if line + 4 < cat * 5:
                    result += ' ' * 10
                    if i > n:
                        result += ' ' * 2

                else:

                    if i < n:
                        result += ''
                    if i > n:
                        result += '|'

                    if line%5 == 0 :
                        result += ' ／|、    '
                    elif line%5 == 4 :
                        result += '(°、。7   '
                    elif line%5 == 3 :
                        result += ' |、 ~ヽ  '
                    elif line%5 == 2 :
                        result += ' ᒐᒐ_f_ )ノ'
                    elif line%5 == 1 :
                        result += '__________'

                    if i > n:
                        result += ''
                    if i < n:
                        result += '|'

            else:
                result += ' ' * 11

        result += '\n'
    return result


if __name__ == '__main__':
    main()
