#!usr/bin/env
# Thadchanon Maidee (Ice-lnwza)
# Lab11_1
# 20411 Sec 001

def matching_sum(t: tuple[int], target_value: int) -> tuple[int]:
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] + t[j] == target_value:
                return [t[i], t[j]]
            else:
                return [t[j], t[i]]
    return None


if __name__ == '__main__':
    print(matching_sum((5, 2), 7))
    assert matching_sum((1,), 1) == []
    