#!usr/bin/env python3

# def median_of_median(list_a: list[float]) -> float:
#
#     def median(list_):
#         len_ = len(list_)
#         mid = len_//2
#         if len_%2 == 1: return list_[mid]
#         return (list_[mid] + list_[mid-1])/2
#
#     if len(list_a) == 3: 
#         return float(sum(list_a) - min(list_a) - max(list_a))
#
#     if len(list_a) == 2:
#         return float(median(list_a))
#
#     if len(list_a) == 1:
#         return float(list_a[0])
#
#     step = len(list_a)//3
#     step_a,step_b = step,2*step
#
#     list_1 = list_a[:step_a]
#     list_2 = list_a[step_a:step_b]
#     list_3 = list_a[step_b:] # remainder will got median
#
#     list_1 = median_of_median(list_1)
#     list_2 = median_of_median(list_2)
#     list_3 = median_of_median(list_3)
#
    # return median_of_median([list_1,list_2,list_3]) # find median

def median_of_median(list_a: list[float]) -> float:
    if not list_a: 
        return 0
    if len(list_a) == 1:
        return list_a[0]
    if len(list_a) == 2:
        return sum(list_a)/2    

    if(len(list_a) >= 3):
        list_1 = list_a[:len(list_a)//3]
        list_2 = list_a[(len(list_a)//3):(len(list_a)//3)*2]
        list_3 = list_a[(len(list_a)//3)*2:]
        lists = [median_of_median(list_1), median_of_median(list_2), median_of_median(list_3)]
        return sum(lists)-max(lists)-min(lists)
        

if __name__ == "__main__":
    print(median_of_median([28,29,87, 14, 13, 21, 19, 27, 23, 30, 16, 3]))
    print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))
    print(median_of_median([1,1,1,1,1,1,1,1,1]))
