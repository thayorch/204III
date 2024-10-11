# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab15_1
# 204111 Sec 001

def sum_nested_list(list_a: list, deep=1):
    if not list_a:
        return 0
    lists = list(filter(lambda x:isinstance(x,list), list_a))
    list_x = list(filter(lambda x:not isinstance(x,list),list_a))
    
    return sum(map(lambda x: x*deep, list_x)) + sum(sum_nested_list(sub,deep + 1) for sub in lists)

if __name__ == "__main__":
   print(sum_nested_list([1, 2, [[3, [[4], 5]], [6, 7]]]))
