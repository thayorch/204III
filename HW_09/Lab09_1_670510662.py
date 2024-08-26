#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab09_1
# 204111 Sec 001

def patterned_message(message: str, pattern: str) -> None:
     # Remove spaces from the message
    clean_message = message.replace(" ", "")
    # Initialize the index for the clean message
    msg_index = 0
    # Length of the cleaned message
    msg_len = len(clean_message)
    
    # Define a function to replace '*' with the corresponding message character
    def replace_star(line):
        nonlocal msg_index
        return ''.join(
            clean_message[(msg_index + i) % msg_len] if char == '*' else char
            for i, char in enumerate(line)
        )

    # Split the pattern into lines and apply the replace_star function to each line
    result = '\n'.join(replace_star(line) for line in pattern.splitlines())

    # Update msg_index after processing each line
    msg_index += sum(line.count('*') for line in pattern.splitlines())

    # Print the result
    print(result)

if __name__ == "__main__":
    patterned_message("123", "** *** ** ** *")
    patterned_message("D and C",'''
***************\n
******   ******\n
***************\n
''')
    patterned_message("Three Diamonds!",'''
  * * *
 *** *** ***
 ***** ***** *****
 *** *** ***
 * * *
''')
