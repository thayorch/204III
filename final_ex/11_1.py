#!usr/bin/env python3

keys = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
def word_count(text: str) -> dict[str, int]:
    new_text = text.split()
    print(list(map(lambda x : x.strip(keys) ,new_text)))



if __name__ == '__main__':
    word_count("He doesn't want to pay $40,000 for anew car, but his wife doesn't seem to care.")
