#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW09_3
# 204111 Sec 001

def unmask_id(masked_id: str) -> list[str]:
    star_count = masked_id.count('*')
    
    all_ids = (f''.join(masked_id.split('-')))
    star_index = all_ids.index('*')
    sum_ids = str(11-sum(check_digit(all_ids, star_count)) % 11)
    replace_stars = lambda repl: ''.join(map(lambda i: repl.pop(0) if i in star_indices else all_ids[i], range(len(all_ids))))
    return list(map(lambda x, y: 's' if y == all_ids[star_index] else y  , range(13), all_ids))

    return list(map(lambda id_str: "{}-{}-{}-{}-{}".format(id_str[:1], id_str[1:5], id_str[5:10], id_str[10:12], id_str[12:]), valid_ids))
    

def check_digit(list_a: list[int], count_a: int):
    return list(map(lambda x,i: int(x)*i  , list_a, list(reversed(range(count_a+1, len(list(list_a))+1))) )) 
    

if __name__ == "__main__":
    print("Testing...")
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
    print("AllPass!!")