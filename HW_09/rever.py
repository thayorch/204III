def rev_help(x, div=None):
    x = abs(x)
    if div is None:
        div = 10**(len(str(x))-1)
    
    # base case
    if div <= 1:
        return x

    # D & C
    head = x % div
    tail = div // 10
    
    # combine
    return rev_help(head, tail) * 10 + (x // div)

def rev_digit(x):
    if x<0:
        return rev_help(x)*(-1)
    else:
        return rev_help(x)
    
if __name__ == '__main__':
    print(rev_digit(1234))