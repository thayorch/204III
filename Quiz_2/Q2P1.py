#!usr/bin/env python3 
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Sec001

def main():
    test()

def replace_in_range(text: str, start: int, stop: int, old_c: str, new_c: str) -> str :
    lists_text = list(text)
    if start <-len(text):
        start = 0
    if(stop>len(text)):
        stop = len(text)

    before_range_text = lists_text[:start]
    in_range_text = map(lambda i: check_index(i, old_c, new_c),lists_text[start:stop])
    after_range_text = lists_text[stop:]
        
    # return list(l)

    return ''.join(before_range_text)+''.join(in_range_text)+''.join(after_range_text)


def check_index(i, old_c, new_c):
    if(str(i).lower()==old_c):
        if(str(i).islower()):
            return new_c.lower()
        elif(str(i).isupper()):
            return new_c.upper()
    return i
   

def test():
    assert replace_in_range('Happy birthday', 3, 10, 'p', 'e') == 'Hapey birthday' ;print('Pass')
    assert replace_in_range('Happy birthday', 3, 10, 'z', 'e') == 'Happy birthday' ;print('Pass')
    assert replace_in_range('Happy birthday', 0, 14, 'h', 'w') == 'Wappy birtwday' ;print('Pass')
    assert replace_in_range('Happy birthday', 3, 10, 'y', 'i') == 'Happi birthday' ;print('Pass')
    assert replace_in_range('Happy birthday', -9, 14, 'y', 'i') == 'Happy birthdai' ;print('Pass')
    assert replace_in_range('Happy birthday', 3, 14, 'y', 'i') == 'Happi birthdai' ;print('Pass')
    assert replace_in_range('Happy birthday', -100, 100, 'y', 'i') == 'Happi birthdai' ;print('Pass')


if __name__ == '__main__':
    main()