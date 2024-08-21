#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab05_1
# 204111

def main():
    print(palindrome_without(str(input()),str(input())))
    # test_palindrome_without()

def palindrome_without(text: str, c: str)->bool:
    text= text.lower()
    c = c.lower()
    text = text.replace(c, ' ')
    reverse_text = ''.join(reversed(text))


    text = text.replace(' ', '')
    reverse_text = reverse_text.replace(' ', '')
    # print(text, reverse_text)
    if(text == reverse_text and text != '' and reverse_text != ''):
        return True
    else:
        return False
    
def test_palindrome_without():
    assert palindrome_without('Banana', 'b') == True
    assert palindrome_without('Swap of paws', 'f') == True
    assert palindrome_without('T', 't') == False
    print("All test cases passed!")

if __name__ == "__main__":
    main()