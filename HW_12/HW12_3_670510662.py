#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW12_3
# 204111 Sec 001


def ms_mine_hint(m: int, n: int, bomb_list: list[tuple[int]]) -> dict[tuple[int], int]:
    
    table = []
    
    for i in range(m):
        for j in range(n):
            table.append((i,j))
    # print(table)
    # print(bomb_list)
    bomb_track = list(map(lambda x: 0,table))
    for i in range(len(table)):
        if table[i] in bomb_list:
            bomb_track[i] = 1
    print(bomb_track)
    
    result = dict()

    for i in range(len(bomb_track)):
        if bomb_track[i] == 0:
            result[table[i]] = (bomb_track[i])
        else : continue

    print(result)

    return 



#
# def bomb_around(bomb_track: list[tuple[int]], index: tuple[int]):
#     if index[0] == 0 and index[1] == 0:
#
#         return
#
if __name__ == "__main__":
    assert ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]) == \
        {(0, 0): 1, (0, 2): 2, (1, 0): 3, (1, 1): 5}
    print("OK")
