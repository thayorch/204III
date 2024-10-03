#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab14_1
# 204111 Sec 001

def sort_date(list_x: list[str], show_steps: bool=False):
    for i in range(1, len(list_x)):
        j = i
        while j > 0 and lower_than(list_x[j],list_x[j-1]) :
            list_x[j], list_x[j-1] = list_x[j-1], list_x[j]                
            j -= 1

        if show_steps:
            print(f"{i}: {list_x}")

def lower_than(date_1: list[str],date_2: list[str]):
    month = {
    'ม.ค.': 1, 'ก.พ.': 2, 'มี.ค.': 3, 'เม.ย.': 4, 'พ.ค.': 5, 'มิ.ย.': 6,
    'ก.ค.': 7, 'ส.ค.': 8, 'ก.ย.': 9, 'ต.ค.': 10, 'พ.ย.': 11, 'ธ.ค.': 12
    }
    
    d_1, m_1, y_1 = date_1.split('/')
    d_2, m_2, y_2 = date_2.split('/')
    
    if int(y_1) != int(y_2):
        return int(y_1) < int(y_2)
    if month[m_1] != month[m_2]:
        return month[m_1] < month[m_2]
    return int(d_1) < int(d_2)

    
if __name__ == '__main__':
    list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544']
    sort_date(list_x)
    print('---')
    print(list_x)
