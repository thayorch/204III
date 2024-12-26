def main():
    return

import math

def merge(left, right):
    result = []
    i = 0
    j = 0
    for x in range(len(left) + len(right)):
        Left = i < len(left)
        Right = j < len(right)
        if Left and (not Right or left[i] <= right[j]):
            result.append(left[i])
            i += 1
        elif Right:
            result.append(right[j])
            j += 1

    return result

def bottom_up_m_sort(list_x: list[int], show_steps: bool = False) -> None:
    n = len(list_x)
    result = []
    for i in range(n):
        result.append([list_x[i]])
    if show_steps:
        print(result)

    for x in range(int(math.log2(n)) + 1):
        wide = 2 ** x
        merg_sublist = []
        for i in range(0, n, 2 * wide):
            j = min(i + wide, n)
            k = min(i + 2 * wide, n)
            merge_ = merge(list_x[i:j], list_x[j:k])
            list_x[i:i + len(merge_)] = merge_
            if show_steps:
                merg_sublist.append(merge_)

        if show_steps:
            print(merg_sublist)


if __name__ == '__main__':
    main() 