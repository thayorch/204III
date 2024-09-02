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




def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str]) -> list[str]:
    list_of_seq = []
    def generate_seq(l_lane, r_lane, result: list, list_of_seq: list, i=0, j=0):
        if i == len(l_lane) and j == len(r_lane):
            list_of_seq.append('>'.join(result))
            return None

        if i < len(l_lane):
            generate_seq(l_lane, r_lane, result + [l_lane[i]], list_of_seq,  i + 1, j, )

        if j < len(r_lane):
            generate_seq(l_lane, r_lane, result + [r_lane[j]], list_of_seq, i, j + 1)    
    generate_seq(l_lane, r_lane, [], list_of_seq)
    return list_of_seq

    
    
    

if __name__ == '__main__':
    print("Testing...")
    # print(arrival_seq(('R32',), ('O9', 'O5')))
    # print(arrival_seq(('R2','R4'), ('O34', 'O22')))
    assert arrival_sequences(('R32',), ('O9', 'O5')) == ['R32>O9>O5', 'O9>R32>O5', 'O9>O5>R32']
    assert arrival_sequences(('R2','R4'), ('O34', 'O22')) == ['R2>R4>O34>O22',
'R2>O34>R4>O22',
'R2>O34>O22>R4',
'O34>R2>R4>O22',
'O34>R2>O22>R4',
'O34>O22>R2>R4']
    print("All pass!!")