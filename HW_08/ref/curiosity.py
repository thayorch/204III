list_a = [166, 164, 156, 175, 172, 156, 182, 180, 171, 159]
print('max-min')
def find_max(list_a):
    from functools import reduce
    return reduce(lambda x, y: x if x > y else y, list_a) # return last True
print(find_max(list_a))

def find_max(list_a):
    if len(list_a) == 1:return list_a[0]
    # divide & conquer)
    head = list_a[0]
    tail = list_a[1:] 
    max_tail = find_max(tail)
    # combine
    if max_tail > head: return max_tail
    else:return head
print(find_max(list_a))
print('=========')
print('factorial')
def factorial(x):
    if x == 1 or x == 0:return 1
    now = x
    next_ = factorial(x-1)
    return now*next_
print(factorial(5))
print('=========')
print('fibonacci')
def fibonacci(n):
    if n == 1 or n == 2:return 1
    R = fibonacci(n-1) # growth
    r = fibonacci(n-2) # new born
    total = R+r
    return total
print(fibonacci(3))
print(fibonacci(5))
print('=========')
print('prime')
def prime_number(n,div = 2):
    if div > n**0.5:
        print(n)
        return # none
    if n%div == 0:
        print(div,end=' * ')
        prime_number(n//div,div)
    else:
        prime_number(n,div+1)
prime_number(1,2)
prime_number(3,2)
prime_number(120,2)
print('=========')
print('kth')
def kth_term(k):
    if k <= 1:return 2
    return 2*k + kth_term(k-1)
print(kth_term(2))
print(kth_term(3))
print('=========')
print('digit print')
def dgt_print_h1(n):
    if n == 0: return
    dgt_print_h1(n//10)
    print(n % 10,end=' ')
    #return n%10
    
def dgt_print_t1(n, div=None):
    if div is None: div = 10**(len(str(n))-1)
    if div < 1: return
    print(n//div, end=" ")
    dgt_print_t1(n % div, div//10)
    
dgt_print_h1(3045)
print()
dgt_print_t1(3045)
print()
print('=========')
print('digit count')
def digit_count(n):
    if n < 10:return 1
    head_len= digit_count(n//10)
    tail_len = digit_count(n%10)
    return head_len+tail_len

print(digit_count(1234567890123456))
print(digit_count(10))
print(digit_count(1))
print('=========')
print('range sum')
def range_sum(lo,hi):
    if lo == hi: return lo
    head_sum = lo
    tail_sum = range_sum(lo+1,hi)
    return head_sum+tail_sum
print(range_sum(10,15))
print('=========')
print('power')
def power(base,exp):
    if exp==0:return 1
    result_head = base
    result_tail = power(base,exp-1)
    return result_head*result_tail
print(power(2,5))
print('=========')
print('digit sum')
def digit_sum(n):
    if n == 0:return 0 
    head = n%10
    tail = digit_sum(n//10)
    return head + tail 
print(digit_sum(1027))
print('=========')
print('list sum')
def list_sum(list_):
    if len(list_) == 0:return 0
    head = list_[0]
    tail = list_sum(list_[1:])
    return head + tail 
print(list_sum([2,3,5,7,11]))
print('=========')
print('interleave')
def interleave(list1,list2):
    if len(list1) == 0:return list2
    head = [list1[0]] + [list2[0]]
    tail = interleave(list1[1:],list2[1:])
    return head + tail
print(interleave([1,2,3],['a','b','c']))
print('=========')
print('vowel count')
def vowel_count(word):
    if len(word) == 0:return 0
    if word[0] in 'aeiou':head_count = 1
    else:head_count = 0
    tail_count = vowel_count(word[1:])
    return head_count + tail_count
print(vowel_count('happy birthday'))
print('=========')
print('pascal')
def pascal(i,j):
    if j == 0 or j == i:return 1
    above_left = pascal(i-1,j-1)
    above_right = pascal(i-1,j)
    return above_left + above_right
print(pascal(7,3))