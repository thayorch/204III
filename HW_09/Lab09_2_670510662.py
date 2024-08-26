#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab09_2
# 204111 Sec 001


def  life_path(n: int) -> int:
    if(len(str(n)) == 1):
        return n
    else:
        return life_path(sum(list(map(int, str(n)))))

if __name__ == '__main__':
    print("Testing...")
    assert life_path(13092004) == 1
    assert life_path(7) == 7
    assert life_path(35) == 8
    print("AllPass!!")