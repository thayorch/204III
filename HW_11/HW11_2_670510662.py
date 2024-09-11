#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW11_1
# 204111 Sec 001
    
def split_and_merge(n: int) -> list[str]:
    # Slide w11_a_lec_1_recursion_part_ii [Assignment Page 16]
    base_object = set(map(int,range(1,n+1)))  # { 1 , 2 , 3 }
    list_1 = list()
    len_obj = len(base_object)

    while len_obj > 0:
        for i in base_object:
            list_1.append((i,))
        len_obj-=1
    return list_1
    # return list(map(lambda x:x,base_object))





    # return arrival_sequences() 

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
    print(split_and_merge(3))   # ['1>2>3', '1>3>2', '2>1>3', '2>3>1','3>1>2']

    # print(split_and_merge(4))   # ['1>2>3>4', '1>2>4>3', '1>3>2>4', '1>3>4>2', '1>4>2>3',
                                # '2>1>3>4','2>1>4>3', '2>3>1>4', '2>3>4>1',
                                # '2>4>1>3', '3>1>2>4', '3>1>4>2', '3>4>1>2', '4>1>2>3']
