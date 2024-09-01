#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW10_2
# 204111 Sec 001

# l_lane เป็น Tuple ของ String แทนเลขประจารถจากบริษัทแดงที่วิ่งทางซ้าย  
# r_lane เป็น Tuple ของ String แทนเลขประจารถจากบริษัทส้มที่วิ่งทางขวา 
# กำหนดให้แต่ละบริษัทมีรถในขบวนอย่างน้อยหนึ่งคัน โดย String ของลำดับที่เป็น Output จะอยู่ในรูป เลขประจำรถคั่นด้วย '>'

def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str], result=[]) -> list[str]:
    
    l_len = len(l_lane)
    r_len = len(r_lane)
    
    if l_len != 0 :
        l_tail = l_lane[1:]
    if r_len != 0 :
        r_tail = r_lane[1:]
    
    if l_len == 0 and r_len == 0:
        return result

# append head
    if l_len>0 and r_len>0:
        result.append(l_lane[0]+'>'+r_lane[0])
        return arrival_sequences(l_tail, r_tail, result)
    

    
    
    # for i in range(l_len-1):
        # result.append(l_head)
        # result.append(r_head)
        # result.append("".join(l_tail[i]))
        # for j in range(r_len-1):
            # result.append("".join(r_tail[j]))
            
    return result
    

if __name__ == '__main__':
    print("Testing...")
    # print(arrival_sequences(('R32',), ('O9', 'O5')))
    print(arrival_sequences(('R2','R4'), ('O34', 'O22')))
    assert arrival_sequences(('R32',), ('O9', 'O5')) == ['O9>O5>R32',
'O9>R32>O5',
'R32>O9>O5']   
    assert arrival_sequences(('R2','R4'), ('O34', 'O22')) == ['R2>R4>O34>O22',
'R2>O34>R4>O22',
'R2>O34>O22>R4',
'O34>R2>R4>O22',
'O34>R2>O22>R4',
'O34>O22>R2>R4']
    print("All pass!!")