#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW12_2
# 204111 Sec 001

#     0     ,        1       ,   2  
# <location>, <treasure_type>, <value>

import sys

def main():
    treasures = read_input()
    assert total_value('Gold', treasures) == 1090
    assert total_value('Ruby', treasures) == -1


def read_input():
    treasures = {}
    for line in sys.stdin:
        if line[0] == "#": 
            continue
        line = line.split(",")
        line = list(map(str.strip,line))
        # print(line)

        location = line[0]
        value = int(line[2])

        if not line[1] in treasures: 
            treasures[line[1]] = []
        treasures[line[1]] += [(location,value)]
        
    # print(treasures)
    return treasures


def total_value(treasure_type, treasures):
    total = 0
    
    if treasure_type not in treasures:
        return -1
    
    for i in treasures[treasure_type]:
        total += i[1]
    return total


if __name__ == '__main__':
    main()