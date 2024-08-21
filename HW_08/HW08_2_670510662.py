#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW08_2
# 204111 Sec 001

def main():
    test()
    # print(skip_list("ABCD"))

def skip_list(word: str) -> list[str]:
    def splitter(word_eiei , n) -> list[str]:

        if n >= len(word_eiei):
            return []        
        skip_str = word_eiei[n::n+1] if n < len(word_eiei) else ""
        
        return [skip_str] + splitter(word, n + 1)
    
    return splitter(word, 0)

def test():
    assert skip_list("ABCD") == ["ABCD", "BD", "C", "D"]
    assert skip_list("hello!") == ["hello!", "el!", "l!", "l", "o", "!"]
    assert skip_list("a") == ["a"]
    print("!! All pass !!")

if __name__ == '__main__':
    main()