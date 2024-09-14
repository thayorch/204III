#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW11_3
# 204111 Sec 001


def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:
    first_letter = list(map(lambda x: x[0], name_list))
    name_index_len = list(map(lambda x: len(x), name_list))
    dicts = dict(map(lambda x: (sum(name_index_len[:x]), name_list[x]), range(len(name_index_len))))
    letter = list(''.join(name_list))
    
    # print(dicts)  # { start_index : 'name' } 
    star , rhyme = 0 , 0
    # star : at star_index
    # rhyme : count ... to rhyme_len  => check()

    while len(name_list) > 1:
        star = star % len(letter)
        if letter[star] == '*' : star += 1
        elif rhyme == (rhyme_len - 1):
            if letter[star] in first_letter:
                name_list.remove(dicts[star])
                letter = letter[:star] + (['*']*(len(dicts[star]))) + letter[(star+(len(dicts[star]))):]
                # print(letter)
                if len(name_list) == 1:
                    return name_list[0]
            else : letter[star] = '*'
            star += 1
            rhyme = 0
        else :
            star += 1
            rhyme += 1
        
    return name_list[0]

if __name__ == '__main__':
    print(eeny_meeny(['John', 'Ann', 'Tom']))       # 'John'
    print(eeny_meeny(['John', 'Ann', 'Tom'], 5))    # 'Tom'
    print(eeny_meeny(['Ann', 'John', 'Meeneoi']))   # 'Meeneoi'
    print(eeny_meeny(['Ann', 'Atom']))              # 'Ann'  
    print(eeny_meeny(['Anna', 'Atom']))             # 'Atom'
