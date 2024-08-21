#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab08_2
# 204111 Sec 001

def main():
    test()
    
def reverse_digits(x: int) -> int:
    def reverse(num: int, reverse_num: int) -> int:
        if num == 0:
            return reverse_num
        return reverse(num // 10, (reverse_num*10)+(num%10))
    
    sign = -1 if x < 0 else 1
    reverse_num = reverse(abs(x), 0)
    return sign * reverse_num
    
def test():
    assert reverse_digits(1234) == 4321 ;print('pass')
    assert reverse_digits(1) == 1 ;print('pass')
    print("All tests passed!!s")
    
if __name__ == "__main__":
    main()