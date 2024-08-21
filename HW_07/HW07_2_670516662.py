#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW07_2
# 204111 Sec 001

def main():
    # print(medal_allocation([9, 8, 7, 6, 5, 4, 3, 2]) )
    # print(medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2]))
    # print(medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]))
    # print(medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]))
    test()

def medal_allocation(list_a: list[int]) -> tuple[list[int], list[int], list[int]]:
    
    list_a = sorted(list_a,reverse=True)
    
    medal_map = list(map(lambda x: list_a_to_medal(x, list_a), list_a))
    gold = list(filter(lambda score: medal_map[list_a.index(score)] == 'gold', list_a))
    silver = list(filter(lambda score: medal_map[list_a.index(score)] == 'silver', list_a))
    bronze = list(filter(lambda score: medal_map[list_a.index(score)] == 'bronze', list_a))
    
    return (gold, silver, bronze)

def list_a_to_medal(x,list_a):
    if(x == list_a[0] and x != 0):
        return 'gold'
    else:
        if(x == list_a[1] and len(list_a) > 1) and x != 0:
            return 'silver'
        else:
            if(x == list_a[2] and len(list_a) >2 and x != 0):
                return 'bronze'
            else:
                None


def test():
    # assert medal_allocation([9, 8, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7]); print("Passed")
    # assert medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7, 7]); print("Passed")
    # assert medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9], [], [8]); print("Passed")
    # assert medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9, 9, 9], [], []); print("Passed")
    assert medal_allocation([9, 8, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7])
    assert medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7, 7])
    assert medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9], [], [8])
    assert medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9, 9, 9], [], [])
    assert medal_allocation([0,0,0,0,0]) == ([],[],[])
    assert medal_allocation([3,2,2,1]) == ([3],[2,2],[])
    assert medal_allocation([1,1,1]) == ([1,1,1],[],[])
    assert medal_allocation([1,0,0]) == ([1],[],[])
    assert medal_allocation([2,1,0,0]) == ([2],[1],[])
    assert medal_allocation([2,2,1,1,1,0,0]) == ([2,2],[],[1,1,1])
    print("!! All Pass !!")
if __name__ == "__main__":
    main()