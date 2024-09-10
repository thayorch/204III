#!usr/bin/env
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab11_1
# 20411 Sec 001


def matching_sum(t: tuple[int], target_value: int) -> list[int]:
    sum = {}
    for i, n in enumerate(t):
        if target_value - n in sum:
            return [target_value - n, t[i]]
        sum[n] = i
    return []


if __name__ == '__main__':
    print(matching_sum((5, 2), 7))
    print(matching_sum((1,), 7))
    print(matching_sum((10, -1, 1, -8, 3, 1), 2)    )
    assert matching_sum((1,), 1) == []
    