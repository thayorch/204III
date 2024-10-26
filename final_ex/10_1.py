#!usr/bin/env python3

def comma_separated(n: int, group: int=3):
    n = str(n)
    range_ = list(range(-len(n),0,group)) # start from behind
    # print(range_)
    str_ = list(n)
    str_ = list(map(lambda x: f',{str_[x]}' if -x in range_ else str_[x],range(len(n))))
    # print(str_)
    return ''.join(str_)

if __name__ == '__main__':
    print("Testing...")
    # print(comma_separated(100000))
    # print(comma_separated(3400))
    assert comma_separated(3400) =="3,400"
    assert comma_separated(3400,4) =="3400"
    assert comma_separated(781588,5) =="7,81588"
    assert comma_separated(1234) =="1,234"
    assert comma_separated(1000000) =="1,000,000"
    assert comma_separated(100000) =="100,000"
    print("AllPass!!")
