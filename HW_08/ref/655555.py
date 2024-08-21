#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW08_3
# 204111 Sec 001

def main():
    test()

def is_anagram(s1: str, s2: str) -> bool:
    def clean_string(s: str) -> str:
        def recursive_clean(s
                            
                            : str) -> str:
            if not s:
                return ""
            char = s[0]
            rest = recursive_clean(s[1:])
            if char.isalpha():
                return char.lower() + rest
            return rest
        return recursive_clean(s)
    
    def count_letters(s: str) -> list:
        def recursive_count(s: str, counts: list) -> list:
            if not s:
                return counts
            char = s[0]
            rest = s[1:]
            index = ord(char) - ord('a')
            if 0 <= index < 26:  # alphabetic char num
                counts[index] += 1
            return recursive_count(rest, counts)
        
        return recursive_count(s, [0] * 26)  # List for each letter from 'a' to 'z'
    
    def compare_lists(l1: list, l2: list) -> bool:
        if not l1 and not l2:
            return True
        if not l1 or not l2:
            return False
        if l1[0] != l2[0]:
            return False
        return compare_lists(l1[1:], l2[1:])
    
    s1_clean = clean_string(s1)
    s2_clean = clean_string(s2)
    
    if len(s1_clean) != len(s2_clean):
        return False
    
    count1 = count_letters(s1_clean)
    count2 = count_letters(s2_clean)
    
    return compare_lists(count1, count2)

    
    
    
def test():
    assert is_anagram("Tom Marvolo Riddle", "I am Lord Voldemort!!!") is True
    assert is_anagram("cat", "tab") is False
    assert is_anagram("Nissan", "Insane") is False
    print("!! All pass !!")

if __name__ == '__main__':
    main()