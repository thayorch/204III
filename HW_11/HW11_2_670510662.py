#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW11_1
# 204111 Sec 001

def power_set(s):
    result = []
    def subset(index, current):
        if index == len(s):
            result.append(current[:])
            return
        
        subset(index + 1, current)
        
        current.append(s[index])
        subset(index + 1, current)
        
        current.pop()
    
    subset(0, [])
    return result



def split_and_merge(n: int) -> list[str]:
    # Slide w11_a_lec_1_recursion_part_ii [Assignment Page 16]
    full_set = [str(i) for i in range(1, n + 1)] 
    power_set_list = power_set(full_set)
    result = set()
    
    for l_lane in power_set_list:
        r_lane = [x for x in full_set if x not in l_lane]
        result |= (arrival_sequences(l_lane, r_lane))
    
    return list(result)



def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str]) -> set[str]:
    def arr_rec(l_lane, r_lane):
        #base case
        if not l_lane:
            return {'>'.join(r_lane)}
        if not r_lane:
            return {'>'.join(l_lane)}

        temp = arr_rec(l_lane[1:], r_lane)
        q1 = set(map(lambda x: l_lane[0]+'>'+x, temp))
        
        temp = arr_rec(l_lane, r_lane[1:])
        q2 = set(map(lambda x: r_lane[0]+'>'+x, temp))

        return q1 | q2
    return arr_rec(l_lane, r_lane)

if __name__ == '__main__':
    print(split_and_merge(3))   # ['1>2>3', '1>3>2', '2>1>3', '2>3>1','3>1>2']
    # print(split_and_merge(4))   # ['2>2>3>4', '1>2>4>3', '1>3>2>4', '1>3>4>2', '1>4>2>3',
    #                             # '2>1>3>4','2>1>4>3', '2>3>1>4', '2>3>4>1',
                                # '2>4>1>3', '3>1>2>4', '3>1>4>2', '3>4>1>2', '4>1>2>3']
