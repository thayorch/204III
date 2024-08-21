#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab07_1
# 204111 Sec 001

def main():
    print(corner_frame(4))
    # test()

def corner_frame(n):
    lists = list(map(lambda i: str(list(map(str, map(lambda j: max(i, j), range(1, n+1))))).strip('[]'),range(1, n+1)))
    # return lists
    
    return '\n'.join(lists).replace('\'','').replace(',','') + '\n'


def test():
    assert corner_frame(4) == """1 2 3 4\n
    2 2 3 4\n
    3 3 3 4\n
    4 4 4 4\n
    """
    
if __name__ == "__main__":
    main()