#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW11_1
# 204111 Sec 001
   

# def permu(seq1, seq2, res=()):
#     if not seq1 and not seq2:
#         return ['>'.join(res + seq1 + seq2)]
#     p1 = permu(seq1[1:], seq2, res + (seq1[0],))
#     p2 = permu(seq1, seq2[1:], res + (seq2[0],))
#     return p1 + p2


def split_and_merge(n: int) -> list[str]:
    # Slide w11_a_lec_1_recursion_part_ii [Assignment Page 16]
    
    base_object = tuple(map(str,range(1,n+1)))  
    map_object = tuple(map(int,range(1,n+1)))
    new_list = []
    result = []

    for i in range(len(map_object)):
        new_list = tuple(map(str ,filter(lambda x: x != map_object[i], map_object)))      
        result += arrival_sequences((base_object[i],),new_list)

    # return base_object, new_list
    return list(set(result))


def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str]) -> list[str]:
    list_of_seq = []
    def generate_seq(l_lane, r_lane, result: list, list_of_seq: list, i=0, j=0):
        if i == len(l_lane) and j == len(r_lane):
            list_of_seq.append('>'.join(result))
            return None

        if i < len(l_lane):
            generate_seq(l_lane, r_lane, result + [l_lane[i]], list_of_seq,  i + 1, j)

        if j < len(r_lane):
            generate_seq(l_lane, r_lane, result + [r_lane[j]], list_of_seq, i, j + 1)    
    generate_seq(l_lane, r_lane, [], list_of_seq)
    return list_of_seq
    

if __name__ == '__main__':
    # print(split_and_merge(3))   # ['1>2>3', '1>3>2', '2>1>3', '2>3>1','3>1>2']
    print(split_and_merge(4))   # ['2>2>3>4', '1>2>4>3', '1>3>2>4', '1>3>4>2', '1>4>2>3',
                                # '2>1>3>4','2>1>4>3', '2>3>1>4', '2>3>4>1',
                                # '2>4>1>3', '3>1>2>4', '3>1>4>2', '3>4>1>2', '4>1>2>3']
