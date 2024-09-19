#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW12_1
# 204111 Sec 001

def scramble(word: str)->list[str]:
    if len(word) == 1:
        return {word}
    else:
        result = set()
        for word_target in word:
            for item in scramble(word.replace(word_target, "",1)):        
                result.append(word_target + item)
        return list(result)
    
if __name__ == '__main__':
    print(scramble("abcdefghij"))
    # print(scramble('Cat'))  
