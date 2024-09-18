#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW12_1
# 204111 Sec 001

def scramble(word: str)->list[str]:
    result = list(map(lambda x: word[1:],range(len(word)) ))
    word_target = word[0]
    
    # for i in range(len(word)):
    #     result.insert(i+1, word_target)
    #     print(i)
    return result
    
    
if __name__ == '__main__':
    print(scramble('Cat'))
    # assert scramble('Cat') == ['Cat', 'Cta', 'aCt' ,'atC', 'tCa', 'taC'] 