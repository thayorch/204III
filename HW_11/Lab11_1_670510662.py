#!usr/bin/env
# Thadchanon Maidee (Ice-lnwza)
# Lab11_1
# 20411 Sec 001

def word_count(text: str) -> dict[str,int]:    
    words = text.strip("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~").lower().split()
    lists = map(lambda x: x.strip("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"), words)
    
    # return list(lists)
    word_count = {}
    for word in lists:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
    
if __name__ == '__main__':
    print(word_count("He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."))