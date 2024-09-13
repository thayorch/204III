#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW11_3
# 204111 Sec 001


def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:
    first_letter = list(map(lambda x: x[0], name_list))
    letter = list(''.join(name_list))
    list_track = []
    
    while len(name_list) > 1:
    
        for i in range(len(letter)):
            if (i*rhyme_len)-1 < len(letter) and i != 0 :
                # print(f"pop : {(i*rhyme_len)-1}",end='\n===\n')
                list_track.append(letter[(i*rhyme_len)-1])

        for i in range(len(list_track)):
            if list_track[i] in first_letter:
                name_list.pop(first_letter.index(list_track[i]))
                return eeny_meeny(name_list)
            else:
                # print(f"remove : {list_track[i]}",end='\n===\n')
                letter.remove(list_track[i])
                continue
            
            
    return ''.join(name_list)
    
    
    
    
    
    
    
    # score = []
    # def fec(letter):
    #     for i in range(len(letter)):
    #             if (i*rhyme_len)-1 < len(letter) and i != 0 :
    #                 print(f"pop : {(i*rhyme_len)-1}",end='\n===\n')
                    
    #                 if letter[(i*rhyme_len)-1] in first_letter:
    #                     name_list.pop(first_letter.index(letter[(i*rhyme_len)-1]))
                        
    #                     first_letter.pop(first_letter.index(letter[(i*rhyme_len)-1]))
    #                 score.append(letter[(i*rhyme_len)-1])
    #                 letter.pop((i*rhyme_len)-1)
    # fec(letter)
    # return name_list, letter,first_letter, score
    
            
    
        
    # def helper(letter: list, name_list: list, index: int) -> str:
    #     if index >= len(letter):
    #         index = index % rhyme_len
        
    #     if letter[index] in first_letter:
    #         name_list.pop(first_letter.index(letter[index]))
    #         first_letter.pop(first_letter.index(letter[index]))
        
    #     letter.pop(index)
    #     new_index = (index * rhyme_len - 1) 
    #     return helper(letter, name_list, new_index)
    
    # return helper(letter, name_list, index)

if __name__ == '__main__':
    print(eeny_meeny(['John', 'Ann', 'Tom']))       # 'John'
    print(eeny_meeny(['John', 'Ann', 'Tom']))       # 'John'
    print(eeny_meeny(['Ann', 'Atom']))           # 'Ann'  
    print(eeny_meeny(['John', 'Ann', 'Tom'], 5))    # 'Tom'
    
    print(eeny_meeny(['Ann', 'John', 'Meeneoi']))   # 'Meeneoi'
    print(eeny_meeny(['Ann', 'John', 'Mee-neoi']))  # 'Ann'