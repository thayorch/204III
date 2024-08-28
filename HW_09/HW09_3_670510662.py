#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW09_3
# 204111 Sec 001

def unmask_id(masked_id: str) -> list[str]:
    # print( generate_possible_ids(masked_id.replace('-', '')))
    possible_ids = generate_possible_ids(masked_id.replace('-', ''))
    def recursive_filter(ids: list[str], index: int = 0, valid_ids: list[str] = None):
        if valid_ids is None:
            valid_ids = []
        if index >= len(ids):
            return valid_ids
        if is_valid_id(ids[index]) and ids[index][0] != '0':
            valid_ids.append(format_id(ids[index]))
        return recursive_filter(ids, index + 1, valid_ids)
    
    return recursive_filter(possible_ids)

# ฟังก์ชันตรวจสอบความถูกต้องของ ID
def is_valid_id(id_number: str) -> bool:
    id_number = id_number.replace('-', '')
    if len(id_number) != 13:
        return False
    total = sum(list(map(lambda x: int(id_number[x]) * (13-x),range(12)) ))
    return (11 - (total % 11)) % 10 == int(id_number[-1])

# สร้างความเป็นไปได้ทั้งหมด
def generate_possible_ids(masked_id: str, current_id: str = '', result: list = None) -> list[str]:
    if result is None:
        result = []
    
    if not masked_id:
        result.append(current_id)
        return result
    
    next_char = masked_id[0]
    rest_masked_id = masked_id[1:]
    
    if next_char == '*':
        def recursive_digit(digit: int):
            if digit < 10:
                generate_possible_ids(rest_masked_id, current_id + str(digit), result)
                recursive_digit(digit + 1)
        recursive_digit(0)
    else:
        generate_possible_ids(rest_masked_id, current_id + next_char, result)
    
    return result

# จัดรูป
def format_id(id_number: str) -> str:
    return f"{id_number[0]}-{id_number[1:5]}-{id_number[5:10]}-{id_number[10:12]}-{id_number[12]}"


if __name__ == "__main__":
    print("Testing...")
    # print(unmask_id('1-2345-67890-12-3'))
    # print(unmask_id('1-2345-67890-12-*'))
    # print(unmask_id('1-2345-67890-1*-*'))
    assert unmask_id('1-2345-67890-1*-*') == ['1-2345-67890-10-4',
'1-2345-67890-11-2',
'1-2345-67890-12-1',
'1-2345-67890-13-9',
'1-2345-67890-14-7',
'1-2345-67890-15-5',
'1-2345-67890-16-3',
'1-2345-67890-17-1',
'1-2345-67890-18-0',
'1-2345-67890-19-8']
    print("AllPass!!")