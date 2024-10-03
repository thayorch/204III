#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab14_2
# 204111 Sec 001

# *** binary search ***

def search_event(list_x: list[tuple[str]],key: str, show_steps: bool=False) -> tuple[str] | None:
    # list_x = list_a[:]
    low = 0
    high = len(list_x) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if show_steps:
            print('[%d]:' % mid, list_x[mid][0])

        if key == list_x[mid][0]:
            return list_x[mid]

        if less_than(key, list_x[mid][0]):
            high = mid - 1
        else:
            low = mid + 1

    return None

def less_than(date_1: list[str],date_2: list[str]):
    month = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    
    d_1, m_1, y_1 = date_1.split('/')
    d_2, m_2, y_2 = date_2.split('/')
    
    if int(y_1) != int(y_2):
        return int(y_1) < int(y_2)
    if month[m_1] != month[m_2]:
        return month[m_1] < month[m_2]
    return int(d_1) < int(d_2)

# if __name__ == "__main__":
#     list_x = [('11/Jan/1900', 'Event A'), ('5/Dec/2001', 'Event B'),('5/Dec/2002', 'Event C'), ('21/Aug/2008', 'Event D'),('9/Mar/2013', 'Event E'), ('11/Mar/2017', 'Event F'),('7/May/2019', 'Event G'), ('29/Feb/2032', 'Event H'),('9/Nov/2042', 'Event I')]
#     assert search_event(list_x, '29/Feb/2032') == ('29/Feb/2032', 'Event H')
#     assert search_event(list_x, '23/Aug/2008') == None
#     print("---")
#     list_x = [('11/Nov/1900',"A"),("12/Nov/1900","B"),("13/Nov/1900","C")]
#     event = search_event(list_x, '11/Nov/1900', show_steps=True)
#     print(event)
if __name__ == "__main__":
    list_x = [('11/Jan/1900', 'Event A'), ('5/Dec/2001', 'Event B'),
('5/Dec/2002', 'Event C'), ('21/Aug/2008', 'Event D'),
('9/Mar/2013', 'Event E'), ('11/Mar/2017', 'Event F'),
('7/May/2019', 'Event G'), ('29/Feb/2032', 'Event H'),
('9/Nov/2042', 'Event I')]
    event = search_event(list_x, '29/Feb/2032')
    print('---')
    print(event)
