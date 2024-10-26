#!usr/bin/env pyhton3

def left_max(list_a:list[int]) -> list[int]:
    list_a = list(filter(lambda x: x>=0, list_a))    
    if len(list_a) <= 1: 
        return list_a
    if list_a[0] >= list_a[1]:
        list_a[1] = list_a[0]
        count = list_a[1]
        return [count] + left_max(list_a[1:])
    count = list_a[0]
    return [count] + left_max(list_a[1:])



if __name__ == "__main__":
    print(left_max([2, 8, 1]))
