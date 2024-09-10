#!usr/bin/env python3
def patterned_message(message: str, pattern: str) -> None:
    star = pattern.count('*')
    pattern = pattern.replace('*','{}')
    message = message.replace(' ','')
    message = message*star     
    print(pattern.format(*message)) 

if __name__ == '__main__':
    assert patterned_message("123", "** *** ** ** *") == '12 312 31 23 1'
    