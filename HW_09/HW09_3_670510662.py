#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW09_3
# 204111 Sec 001

def unmask_id(masked_id: str) -> list[str]:
    star_count = masked_id.count('*')
    
    if star_count == 0:
        return [masked_id]
    if star_count == 1:
        return [masked_id[:-1] + str(check_digit(list(masked_id.replace("-","")), star_count))[-1]]
    
                



    
def check_digit(list_a: list[int], count_a: int):
    return 11 - sum(list(map(lambda x,i: int(x)*i  , list_a[:-1], list(reversed(range(count_a+1, len(list(list_a))+1))) )))%11
    

if __name__ == "__main__":
    # print("Testing...")
    print(unmask_id('1-2345-67890-12-3'))
    print(unmask_id('1-2345-67890-12-*'))
    print(unmask_id('1-2345-67890-1*-*'))
#     assert unmask_id('1-2345-67890-1*-*') == ['1-2345-67890-10-4',
# '1-2345-67890-11-2',
# '1-2345-67890-12-1',
# '1-2345-67890-13-9',
# '1-2345-67890-14-7',
# '1-2345-67890-15-5',
# '1-2345-67890-16-3',
# '1-2345-67890-17-1',
# '1-2345-67890-18-0',
# '1-2345-67890-19-8']
    # print("AllPass!!")