#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW12_3
# 204111 Sec 001

def main():
    assert ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]) == \
        {(0, 0): 1, (0, 2): 2, (1, 0): 3, (1, 1): 5}
    print("OK")


def ms_mine_hint(m: int, n: int, bomb_list: list[tuple[int]]) -> dict[tuple[int], int]:
    d = dict()
    print_board(m, n, bomb_list)
    return d    

if __name__ == "__main__":
    main()
