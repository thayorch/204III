#!usr/bin/env python3


def patterned_message(message: str, pattern: str) -> None:
    message = message.replace(" ","")
    new_pattern = pattern.replace('*','{}')
    message = message*pattern.count('*')
    print(new_pattern.format(*message))

if __name__ == "__main__":
    patterned_message("123", "** *** ** ** *")
    patterned_message("D and C",'''
***************
****** ******
***************
''')
