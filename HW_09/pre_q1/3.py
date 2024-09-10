def left_max(list_a: list[int]) -> list[int]:

    current = list_a[1]
    for i in range(len(list_a)):
        if list_a[i] < current:
            current = list_a[i]
        else:
            continue
    return list_a


if __name__ == "__main__":
    print(left_max([2, 8, 8]))
    assert left_max([2, 8, 1]) == [2, 8, 8]
