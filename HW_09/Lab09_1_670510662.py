#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab09_1
# 204111 Sec 001

def patterned_message(message: str, pattern: str) -> None:
    message = message.replace(" ", "")
    len_star = pattern.count("*")
    len_mess = len(message)
    
    if len_star > len_mess:
        message = message*len_star        
    # print(message)
    pattern = pattern.replace("*", "{}")
    print(pattern.format(*message))
if __name__ == "__main__":
    patterned_message("123", "** *** ** ** *")
