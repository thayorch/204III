#!/usr/bin/env python3
# Ice-lnwza
# 670510662
# Sec 001

def reverse_cap(list_a):
    
    list_first = list(map(lambda i: list_a[i][0].lower(), range(len(list_a))))
    list_last = list(map(lambda i:list_a[i][1:].upper() if list_a[i] != list_first else '', range(len(list_a))))
    list_all = list(map(lambda i:''.join(list_first[i])+''.join(list_last[i]) , range(len(list_a))))
    return list_all

if __name__ == '__main__':

    print(reverse_cap(['I', 'bought', 'two', 'bananas']))
    assert reverse_cap(['I', 'bought', 'two', 'bananas']) == \
        ['i', 'bOUGHT', 'tWO', 'bANANAS']

    print("All OK!")
