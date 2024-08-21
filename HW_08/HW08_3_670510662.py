#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW08_3
# 204111 Sec 001


    # apl_list_1 same alp_list_2
    # ord(a) = 97 
    # list[ord('some-char') - 97 ] index นั้นๆ +1 check ความเท่ากัน

def main():
    test()
    # print(is_anagram("_.icez5__","1icest"))
    # print(is_anagram("cat", "tab"))
    # print(is_anagram("bbaa", "aaab"))

def is_anagram(s1: str, s2: str) -> bool:
    
    aph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # print(aph_list)
    
    s1 = list(filter(lambda x: x.isalpha(),s1.lower()))
    s2 = list(filter(lambda x: x.isalpha(),s2.lower()))
    
    if(len(s1)!=len(s2)):
        return False
    
    def check_aph_count(s: str, i: int, lists: list):
        if i < 0:
            return lists
        lists[ord(s[i])-ord('a')] += 1
        return check_aph_count(s, i-1, lists)
    
    lists_1 = check_aph_count(s1, len(s1)-1, [0]*len(aph_list))
    lists_2 = check_aph_count(s2, len(s2)-1, [0]*len(aph_list))
    # print(lists_1,'\n',lists_2)
    return lists_1==lists_2
    
    
def test():
    assert is_anagram("Tom Marvolo Riddle", "I am Lord Voldemort!!!") is True
    assert is_anagram("cat", "tab") is False
    assert is_anagram("Nissan", "Insane") is False
    print("!! All pass !!")

if __name__ == '__main__':
    main()