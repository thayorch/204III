#!/usr/bin/env python3
# Ice-lnwza
# 670510662
# Sec 001

#  9-15 ahp
#  [0] - [1] :  Year
#  [-1][-2][-3] : Key



def transform_id(int_id):
    lists = str(int_id)
    return f"{''.join(lists[-3])}{''.join(lists[-2])}{''.join(lists[-1])}-{''.join(lists[0])}{''.join(lists[1])}"


if __name__ == '__main__':
    assert transform_id(650241555) == '555-65'
    assert transform_id(670510662) == '662-67'
    print("All OK!")
