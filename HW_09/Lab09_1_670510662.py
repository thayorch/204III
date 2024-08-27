#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab09_1
# 204111 Sec 001

def patterned_message(message: str, pattern: str) -> None:
    message = message.replace(" ", "")
    pattern_without_ = pattern.replace(" ", "")
    star_count = len(pattern_without_)
    
    # print(star_count)
    def pattern_x(msg_index=None):
        if msg_index is None:
            msg_index = 0
        if msg_index >= len(message):
            print(result)
        result = '\n'.join()
        print(result)

if __name__ == "__main__":
    patterned_message("123", "** *** ** ** *")
