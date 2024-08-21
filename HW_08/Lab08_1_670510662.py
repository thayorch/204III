#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab08_1
# 204111 Sec 001

def main():
    test()
    
def gcd(x: int, y: int):
    
    r = y%abs(x)
    if r != 0:
        return gcd(r,abs(x))             
    if r == 0:
        return abs(x)
    
def test():
    assert gcd(19,71) == 1 ;print("pass")
    assert gcd(-39, 78) == 39 ;print("pass")
    print("All tests passed!")
    
if __name__ == "__main__":
    main()