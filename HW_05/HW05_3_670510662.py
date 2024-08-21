#!/usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza007)
# HW05_3
# 204111

def main():
    # print(is_valid_license("9AB8954"))
    # print("666WIFIPASSWORD".isupper())
    test()

def is_valid_license(license_str: str) -> bool:
    if(len(license_str) >= 3 and 
       len(license_str) <= 7 and
       license_str.isupper()       
    ):
        if(license_str[0:1].isalpha() and license_str[2:].isdigit() and len(license_str[3:])<4):
            return True
        elif(license_str[0].isdigit() and license_str[1].isalpha() and license_str[2].isalpha() and license_str[3:].isdigit()):
            return True
        elif(license_str.isdigit() and len(license_str) == 4 and not(license_str.isalpha())):
            return True
        else:
            return False
    else:
        return False
               

def test():
    assert is_valid_license("A9") is False
    assert is_valid_license("9AB8954") is True
    assert is_valid_license("CD700") is True
    assert is_valid_license("9999") is False
    assert is_valid_license("999D1234") is False
    assert is_valid_license("AA11111") is False
    assert is_valid_license("CD700") == True
    assert is_valid_license("9AB8954") == True
    assert is_valid_license("9999") == False
    assert is_valid_license("99D1234") == False
    assert is_valid_license("9AB89A4") == False
    assert is_valid_license("9C4567") == False
    assert is_valid_license("AB444A") == False
    assert is_valid_license("AA11111") == False
    print("Passed !!!")


if __name__ == '__main__':
    main()