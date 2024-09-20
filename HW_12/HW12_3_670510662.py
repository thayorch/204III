#!usr/bin/env python3k
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW12_3
# 204111 Sec 001

def ms_mine_hint(m: int, n: int, bomb_list: list[tuple[int]]) -> dict[tuple[int], int]:
    bomb_list = set(bomb_list) 
    result = dict()
    # print(bomb_list)

    for i in bomb_list:

        around = [(i[0]-1,i[1]),(i[0]+1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1),(i[0]-1,i[1]-1),(i[0]+1,i[1]-1),(i[0]-1,i[1]+1),(i[0]+1,i[1]+1)] 
        # print(around)
        for j in around:
            if (j in bomb_list) or not(j[0] <= (m-1) and j[0] >= 0 and j[1] <= (n-1) and j[1] >= 0):
                continue
            if j[0] <= (m-1) and j[0] >= 0 and j[1] <= (n-1) and j[1] >= 0:
                result[j] = result.get(j,0) +1
    return result

if __name__ == "__main__":
    print(ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]))
    assert ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]) == \
        {(0, 0): 1, (0, 2): 2, (1, 0): 3, (1, 1): 5}
    print("OK")
