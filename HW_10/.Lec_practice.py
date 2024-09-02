def sum_1_to_n(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def while_1():
    x = 3
    ans = 0
    iters_left = x
    while iters_left != 0:
        ans += x
        iters_left -= 1
        print(str(x)+'*'+str(iters_left)+'='+str(ans))

def gcd(a, b):
    r = a % b
    while(r != 0):
        a = b
        b = r
        r = a % b
    return b

def guess_num():
    key = 6
    for i in range(5):
        n = int(input('Input number: '))
        if n == key:
            print('Congratulations! You guessed it.')
            break
        elif n > key:
            print('Too High! Try again.')
        else:
            print('Too Low! Try again.')
    else:
        print('You failed to guess the number after 5 attempts.')


def score_average():
    total_count = 30
    score_count = 0
    total = 0
    while score_count < total_count:
        score = float(input("Enter score:"))
        if score < 0 or score > 100 :
            continue
        
        total += score
        score_count += 1
    return total / score_count

def int_power(x, y):
    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result
        
def int_to_bin(x):
    result = ""
    while x > 0:
        result = str(x % 2) + result
        x //= 2
    return result
    # อันนี้สั้นกว่า
    # return '{0:b}'.format(x)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

def test_emurate():
    s = 'abcd'
    for i,l in enumerate(s):
        print(i, l)

    for i in range(len(s)):
        print(i, s[i])

    for l in s:
        print(l)
    


def merge_list(list_a, list_b):
    len_a = len(list_a)
    len_b = len(list_b)
    i=0
    j=0
    list_c = []
    
    while i < len_a and j < len_b:
        if list_a[i] < list_b[j]:
            list_c.append(list_a[i])
            i += 1
        else:
            list_c.append(list_b[j])
            j += 1
    if i < len_a :
        return list_c
    if j < len_b :
        return list_c + list_b[j:]
    return list_c

def merge_list_1(list_a, list_b):
    if not list_a:
        return list_b
    if not list_b:
        return list_a
    
    if list_a[0] < list_b[0]:
        sub_task = list_a[0]
        sub_sol = merge_list_1(list_a[1:], list_b)
    else:
        sub_task = list_b[0]
        sub_sol = merge_list_1(list_a, list_b[1:])
    
    return [sub_task] + sub_sol

import random
def rand_num_in_range(lo, hi):
    return lo + (hi - lo) * random.random()

def is_in_circle(x, y):
    return x**2 + y**2 <= 1

def find_pi(sample):
    num_in_circle = 0
    for s in range(sample):
        x = rand_num_in_range(0, 1)
        y = rand_num_in_range(0, 1)
    if is_in_circle(x, y):
        num_in_circle += 1
    return (num_in_circle / sample) * 4

def longestWord(*args):
    if (len(args) == 0): return None
    result = args[0]
    for word in args:
        if (len(word) > len(result)):
            result = word
    return result

def sive_of_eratosthenes(n):
    list_of_n = list(range(2, n+1))
    for current_num in list_of_n:
        if current_num > 1:
            for multiple in range(current_num*2, n+1, current_num):
                list_of_n[multiple-2] = 0
    list_of_prime = list(filter(lambda x: x != 0, list_of_n))
    print(list_of_prime)

def eratosthenes(n, show_step: bool=False):
    list_number = list(range(2, n + 1))
    pir = 2
    index = 0

    while pir ** 2 <= n:
        list_number = list(filter(lambda x: x == pir or x % pir != 0, list_number))


        if show_step:
            print(str(pir) + ':', list_number)
            
        index += 1
        pir = list_number[index]

    return list_number
    

if __name__ == "__main__":
    # print(sum_1_to_n(3))
    # print(factorial(5))
    # while_1()
    # print(gcd(246,72))
    guess_num()
    # print(int_power(2.5,3))
    # print(int_to_bin(10))
    # print(score_average())
    # print(int_to_bin(28))
    # print(find('abcd','d'))
    # print(count_letter('apple','p'))
    
    # list_a =[1, 3,4, 5,6]
    # list_b =[2, 5, 7, 9, 10]
    # print(merge_list(list_a,list_b))
    # print(merge_list_1(list_a,list_b))
    
    # test_emurate()
    
    # print(find_pi(10000))
    
    # print(longestWord("this", "is", "really", "nice")) # really
    # mywords = ["this", "is", "really", "nice"]
    # print(longestWord(mywords))  # ['this', 'is', 'really', 'nice']
    # print(longestWord(*mywords)) # really
    # sive_of_eratosthenes(100)
    # print(eratosthenes(20,True))