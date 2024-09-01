#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW10_2
# 204111 Sec 001

# l_lane เป็น Tuple ของ String แทนเลขประจารถจากบริษัทแดงที่วิ่งทางซ้าย  
# r_lane เป็น Tuple ของ String แทนเลขประจารถจากบริษัทส้มที่วิ่งทางขวา 
# กำหนดให้แต่ละบริษัทมีรถในขบวนอย่างน้อยหนึ่งคัน โดย String ของลำดับที่เป็น Output จะอยู่ในรูป เลขประจำรถคั่นด้วย '>'

# l[0]>l[1]>r[0]>r[1]
# l[0]>r[0]>r[1]>l[1]
# l[0]>r[0]>l[1]>r[1]

# r[0]>l[0]>l[1]>r[1]
# r[0]>l[0]>r[1]>l[1] 
# r[0]>r[1]>l[0]>l[1]



def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str], result=[]) -> list[str]:
    l_lane = list(l_lane)
    r_lane = list(r_lane)
    
    l_len = len(l_lane)
    r_len = len(r_lane)
    
    

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