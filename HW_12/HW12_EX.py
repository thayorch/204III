#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW12_EX
# 204111 Sec 001

def xmas_tree(n: int) -> str:
    return star(n) + leaves(n) + base(n)



def star(n: int):
    sky = ' ' * (2 * (n + 4) + 3) + '\n'
    line = ' ' * (n + 4) + '|' + ' ' * (n + 4) + '\n'
    star = ' ' * (n + 2) + '--*--' + ' ' * (n + 2) + '\n'
    line_italic = ' ' * (n + 3) + '/|\\' + ' ' * (n + 3) + '\n'
    return sky + line + star + line_italic
    
def leaves(n):
    layer = ''
    row = 4
    for i in range(n):
        if i >= 1:
            row = 3

        border = 2 + i
        if i < 1:
            border = 1 + i

        for j in range(row, 0, -1):
            layer += ' ' * (j - 1)
            layer += ' ' * (n - i - 1)
            layer += '/' + '* ' *border + '*' + '\\'
            layer += ' ' * (j - 1)
            layer += ' ' * (n - i - 1) + '\n'
            border += 1

    return layer

def base(n):
    truck = ' ' * (n + 3) + '|||' + ' ' * (n + 3) + '\n'
    root = '_' * (n + 3) + '|||' + '_' * (n + 3) + '\n'
    return truck + root



if __name__ == '__main__':
    print(xmas_tree(3))
