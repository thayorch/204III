#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab10_1
# 204111 Sec 001

def comma_separated(n: int, group: int=3):
    if group > 0:
        n = list(str(n))[::-1]
        ncount = len(n)
        if ncount < group: 
            return ''.join(n[::-1])
        elif ncount >= group:
            if group >= 3:
                for i in range((ncount//group)):
                    n.insert(((group+i) + (group*i)) ,',')    
                    # print(n)
                if ncount % group == 0:
                    return ''.join(n[::-1])[1:]
                else:
                    return ''.join(n[::-1])                                     
                    
            else:
                for i in range(ncount//group+1):
                    n.insert(group*i+i ,',')
                if ncount % group == 0:
                    return ''.join(n[1:][::-1])[1:]
                else:
                    return ''.join(n[1:][::-1])
        return n




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