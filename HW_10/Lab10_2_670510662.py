#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab10_2
# 204111 Sec 001

def longest_digit_run(n: int) -> int:
    n = list(map(int, str(n)))
    max_count = 1
    current_count = 1

    for i in range(1, len(n)):
        if n[i] == n[i - 1] :
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 1
    if current_count > max_count:
        max_count = current_count
    return max_count
        


if __name__ == '__main__':
    print("Testing...")
    # print(longest_digit_run(10221122))
    # print(longest_digit_run(11777332))
    # print(longest_digit_run(1177332))
    # print(longest_digit_run(1111111111))
    assert longest_digit_run(10221122) == 2
    assert longest_digit_run(11777332) == 3
    assert longest_digit_run(1177332) == 2
    assert longest_digit_run(1111111111) == 10
    print("AllPass!!")