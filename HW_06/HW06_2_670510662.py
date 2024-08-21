#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW06_2
# 204111 Sec 001

def main():
    # print(decode("abcde","-2"))
    print(decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 -9 9 .
'''))
    
    test_decode_functions()


def decode_helper(code_table, str_index)->str:  # รับรหัส 1 ตัว แล้วคืน 1 อักขระที่ถูกต้อง
    if(str_index == '.') : return '\n'
    elif(str_index):
        str_index = int(str_index)
        if( str_index > len(code_table)-1) : return '_'
        elif(str_index < -len(code_table)): return '_'
        return code_table[str_index]
        
    return '_'


def decode(code_table, text):
    # แยกรหัสทั้งหมด ให้กลายเป็น list เช่น ['3', '.', '5', '3', '4', '2', '.', ...]
    l_text = text.split()
    # เรียกใช้ฟังก์ชัน decode_helper() ที่มีหน้าที่รับรหัสหนึ่งตัว แล้วคืน 1 อักขระที่ถูกต้อง
    result_list = list(map(lambda x: decode_helper(code_table, x), l_text))
    # รวม list ของอักขระ ให้เป็น string
    result = ''.join(result_list)
    return result


def test_decode_functions():
    code_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    # Test cases for decode_helper
    assert decode_helper(code_table, '0') == 'A'
    assert decode_helper(code_table, '1') == 'B'
    assert decode_helper(code_table, '2') == 'C'
    assert decode_helper(code_table, '3') == 'D'
    assert decode_helper(code_table, '4') == 'E'
    assert decode_helper(code_table, '5') == 'F'
    assert decode_helper(code_table, '6') == 'G'
    assert decode_helper(code_table, '7') == '_'  # Out of range
    assert decode_helper(code_table, '.') == '\n'  # Newline character
    
    # Test cases for decode
    assert decode(code_table, "0 1 2 3 4 5 6") == "ABCDEFG"
    assert decode(code_table, "0 . 1 2 . 3 4 5 6") == "A\nBC\nDEFG"
    assert decode(code_table, "3 . 5 3 4 2 . 0 1") == "D\nFDEC\nAB"
    assert decode(code_table, "7 8 9") == "___"  # All out of range
    
    print("All tests passed!")



if __name__ == '__main__':
    main()

