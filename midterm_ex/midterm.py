# 1
def  generate_p_triple(m: int, n: int) -> None:
    a = (m**2) - (n**2)
    b = 2*m*n
    c = (m**2) + (n**2)
    print(a ,b ,c)

# 2
def lucky_name(name: str) -> bool:
    if(name[0] in 'aeiou' and name[-1] not in 'aeiou'):
        return True
    if(name[-1] in 'aeiou' and name[0] not in 'aeiou'):
        return True
    else:
        return False

# 3
def count_lucky_number(start: int, stop: int):
    return len(list(filter(lambda x:'7' not in str(x) and x% 7 ==0,range(start,stop))))

# 4
from functools import reduce
def find_min(list_a: list[int]):
    return reduce(lambda x, y: x if x<y else y, list_a)

def find_min_recusive(list_a: list[int]):
    if(len(list_a)==1):
        return list_a[0]
    
    head = list_a[0]
    tail = find_min_recusive(list_a[1:])
    
    if head > tail :
        return head
    return tail

# 4
def median(list_a: list[int]) -> float:
    list_a = sorted(list_a)[::-1]
    index = len(list_a)//2
    if len(list_a) % 2 ==1:
        return list_a[index]
    return (list_a[index] + list_a[index-1]) / 2

# 5
def  adjacent_sum(list_a: list[int])-> list[int]:
    return map(lambda x,y: x+y, list_a, list_a[1:])

def adjecent_sum2(list_a: list[int])-> list[int]:
    return map(lambda x: list_a[x] + list[x-1], range(1,len(list_a)))
# 6
def same_letter(str1 : str, str2 : str):
    left = list(filter(lambda x: x in str1.lower(), 'abcdefghijklmnopqrstuvwxyz'))
    right = list(filter(lambda x: x in str2.lower(), 'abcdefghijklmnopqrstuvwxyz'))
    return left == right

# Part 2
def same_letter1(str1, str2):
    left1 = list(map(lambda char: char.lower(), filter(str.isalpha,str1)))
    right1 = list(map(lambda char: char.lower(), filter(str.isalpha,str2)))
    return all(map(lambda char: char in left1,right1)) and all(map(lambda char: char in right1,left1))

# Part 3
# Find Mode
# list_a = [40, 15 , 40, 20, 30, 30, 40, 80, 40]
# list.count(_)
# 

def find_mode(score_list: list[int]) -> list[int]:
    