#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW10_2
# 204111 Sec 001

# l_lane เป็น Tuple ของ String แทนเลขประจารถจากบริษัทแดงที่วิ่งทางซ้าย  
# r_lane เป็น Tuple ของ String แทนเลขประจารถจากบริษัทส้มที่วิ่งทางขวา 
# กำหนดให้แต่ละบริษัทมีรถในขบวนอย่างน้อยหนึ่งคัน โดย String ของลำดับที่เป็น Output จะอยู่ในรูป เลขประจำรถคั่นด้วย '>'

def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str], result=[]) -> list[str]:
    l_lane = list(l_lane)
    r_lane = list(r_lane)
    
    l_len = len(l_lane)
    r_len = len(r_lane)
    
    if l_len == 0 and r_len == 0:
        return result
    
    if l_len > 0 :
        # l_head = l_lane[0]
        result.append(l_lane.pop(0))
        l_tail = l_lane[:]
    if r_len > 0 :
        # r_head = r_lane[0] 
        result.append(r_lane.pop(0))
        r_tail = r_lane[:]

# append head
    return arrival_sequences(l_tail,r_tail,result)

    

if __name__ == '__main__':
    print("Testing...")
    # print(arrival_sequences(('R32',), ('O9', 'O5')))
    print(arrival_sequences(('R2','R4'), ('O34', 'O22')))
#     assert arrival_sequences(('R32',), ('O9', 'O5')) == ['O9>O5>R32',
# 'O9>R32>O5',
# 'R32>O9>O5']   
    assert arrival_sequences(('R2','R4'), ('O34', 'O22')) == ['R2>R4>O34>O22',
'R2>O34>R4>O22',
'R2>O34>O22>R4',
'O34>R2>R4>O22',
'O34>R2>O22>R4',
'O34>O22>R2>R4']
    print("All pass!!")