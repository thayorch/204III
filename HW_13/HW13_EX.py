#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW13_EX
# 204111 Sec 001

def sand_towers(list_a):
    tower = ''

    # - separate to 4 step
    # 1. top    (empty zone)
    tower += blue_sky(list_a)

    # 2. Flag at highest
    tower += flag(list_a)

    # 3. body of sand tower
    tower += big(list_a)

    # 4. base of sand tower
    tower += base(list_a)

    return tower


# " _ "
def blue_sky(list_a):
    sky = ''

    for i in list_a:
        sky += ' ' * (2 * (i - 1) + 3)

    sky += '  \n'
    return sky


# " + "
def flag(list_a):
    top_of_tow = max(list_a)
    flag_s = ' '

    for j in range(2):
        for i in list_a:
            flag_s += ' ' * i
            
            if j == 0:
                if i == top_of_tow:
                    flag_s += '|>>~'
                elif i < top_of_tow:
                    flag_s += '    '

            elif j == 1:
                if i == top_of_tow:
                    flag_s += '|   '
                elif i < top_of_tow:
                    flag_s += '    '

            flag_s += ' ' * (i - 3)

        flag_s += ' \n '

    for i in list_a:
        flag_s += ' ' * (i - 2)
        if i == top_of_tow:
            flag_s += '/^^^\\ '
        elif i < top_of_tow:
            flag_s += '      '
        flag_s += ' ' * (i - 3)

    flag_s += ' \n'

    return flag_s


def big(list_a):
    tower = ''
    top = max(list_a)
    for i in range(top - 2):
        tower += ' '

        for j in list_a:
            # highest
            if j == top:
                tower += ' ' * (top - i - 3)
                tower += '/'
                if top - i + 1 == j:
                    tower += '^' * 7
                else:
                    tower += ' ' * (2 * i + 5)
                tower += '\\'
                tower += ' ' * (top - i - 3)

            # lower than
            else:
                if i < top - j - 1:
                    tower += ' ' * (2 * j + 1)

                else:
                    tower += ' ' * (top - i - 3)
                    tower += '/'

                    # -------- top of tower ---------
                    if i == top - j - 1:
                        tower += '^' * 3

                    # --------- third floor ---------
                    elif i == top - j + 1:
                        tower += '^' * 7

                    # ---------- the other  ---------
                    else:
                        tower += ' ' * (2 * abs(- top + i + j) + 5)

                    tower += '\\'
                    tower += ' ' * (top - i - 3)

        tower += ' ' + '\n'

    return tower


def base(list_a):
    b = '/'
    tower = 1
    for i in list_a:
        b += ':' * 2 * i
        if tower == len(list_a):
            b += ':'
        else:
            b += '/'
        tower += 1

    b += '\\\n'
    return b

if __name__ == '__main__':
    print(sand_towers([9, 12, 6]))
