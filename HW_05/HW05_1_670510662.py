#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW05_1
# 204111

def main():
    test_substitute_once()
    # print(substitute_once('Bidding', 'i', 'u'))

def substitute_once(text: str, old: str, new: str):
    index = text.find(old)
    # print(index)
    if index == -1:
        return text
    else:
        return text[:index] + new + text[index + len(old):]

def test_substitute_once():
    assert substitute_once('battle', 'b', 'c') == 'cattle'
    assert substitute_once('Bidding', 'i', 'u') == 'Budding'
    assert substitute_once('doesn\'t', 'n\'t', ' not') == 'does not'
    print('Passed !!!')


if __name__ == '__main__':
    main()

