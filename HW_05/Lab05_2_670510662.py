#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# Lab05_2
# 204111

def main():
    # print(count_down_to_songkran(int(input()), int(input()), int(input())))
    test_countdown()

def count_down_to_songkran(d: int,m: int,y :int):    
    
    if m < 4 :
        Leap_year_status = Leap_status(y) 
        Feb = Feb_days(Leap_year_status)
        
        if(m==1):
            return (31-d)+Feb+31+(13)
        elif(m==2):
            return (Feb-d)+31+(13)
        elif(m==3):
            return (31-d)+(13)

    elif m  > 4 :
        Leap_year_status = Leap_status(y+1)
        Feb = Feb_days(Leap_year_status)
        
        if(m==5):
            return (31-d)+(31*6)+(30*3)+Feb+(13)
        elif(m==6):
            return (30-d)+(31*6)+(30*2)+Feb+(13)
        elif(m==7):
            return (31-d)+(31*5)+(30*2)+Feb+(13)
        elif(m==8):
            return (31-d)+(31*4)+(30*2)+Feb+(13)
        elif(m==9):
            return (30-d)+(31*4)+(30)+Feb+(13)
        elif(m==10):
            return (31-d)+(31*3)+(30)+Feb+(13)
        elif(m==11):
            return (30-d)+(31*3)+Feb+(13)
        elif(m==12):
            return (31-d)+(31*2)+Feb+(13)
    elif m == 4:                                   
        if d<13:
            return 13-d
        elif d>13:
            Leap_year_status = Leap_status(y+1) 
            Feb = Feb_days(Leap_year_status)
            return (30-d) + (31*7) + (30*3) + 13 + Feb
        elif d==13:
            return 0 
    
def Feb_days(Leap_year_status):
    if Leap_year_status==True:
        return 29
    else:
        return 28

def Leap_status(y :int):
    if y % 4 == 0:
        if y % 400 == 0:
            return True
        elif y % 100 == 0:
            return False
        else:
            return True
    else:
        return False

def test_countdown():
    assert count_down_to_songkran(1,1,2024) == 103 ; print("passed!!!")
    assert count_down_to_songkran(1,2,2024) == 72 ; print("passed!!!")
    assert count_down_to_songkran(1,3,2024) == 43 ; print("passed!!!")
    assert count_down_to_songkran(1,5,2024) == 347 ; print("passed!!!")
    assert count_down_to_songkran(1,6,2024) == 316 ; print("passed!!!")
    assert count_down_to_songkran(1,7,2024) == 286 ; print("passed!!!")
    assert count_down_to_songkran(1,8,2024) == 255 ; print("passed!!!")
    assert count_down_to_songkran(1,9,2024) == 224 ; print("passed!!!")
    assert count_down_to_songkran(1,10,2024) == 194 ; print("passed!!!")
    assert count_down_to_songkran(1,11,2024) == 163 ; print("passed!!!")
    assert count_down_to_songkran(1,12,2024) == 133 ; print("passed!!!")
    assert count_down_to_songkran(12,4,2024) == 1 ; print("passed!!!")
    assert count_down_to_songkran(13,4,2024) == 0 ; print("passed!!!")
    assert count_down_to_songkran(14,4,2024) == 364 ; print("passed!!!")
    assert count_down_to_songkran(13,4,2025) == 0 ;print('pass!!!')
    assert count_down_to_songkran(13,4,2024) == 0 ;print('pass!!!')
    assert count_down_to_songkran(13,4,2023) == 0 ;print('pass!!!')
    assert count_down_to_songkran(1,2,2024) == 72  ;print('pass!!!')
    assert count_down_to_songkran(14,4,2023) == 365  ;print('pass!!!')
    assert count_down_to_songkran(4,2,2025) == 68  ;print('pass!!!')
    assert count_down_to_songkran(1,1,2024) == 103 ;print('pass!!!')
    assert count_down_to_songkran(12,4,2024) == 1 ;print('pass!!!')
    assert count_down_to_songkran(12,4,2025) == 1 ;print('pass!!!')
    assert count_down_to_songkran(15,2,2024) == 58 ;print('pass!!!')
    assert count_down_to_songkran(31,3,2024) == 13 ;print('pass!!!')
    assert count_down_to_songkran(20,3,2024) == 24 ;print('pass!!!')
    assert count_down_to_songkran(14,4,2024) == 364 ;print('pass!!!')
    assert count_down_to_songkran(14,4,2025) == 364 ;print('pass!!!')
    assert count_down_to_songkran(14,4,2023) == 365 ;print('pass!!!')
    assert count_down_to_songkran(29,2,2024) == 44 ;print('pass!!!')
    assert count_down_to_songkran(31,12,2024) == 103 ;print('pass!!!')
    assert count_down_to_songkran(31,12,2025) == 103 ;print('pass!!!')
    assert count_down_to_songkran(31,12,2023) == 104 ;print('pass!!!')
    assert count_down_to_songkran(27,10,2023) == 169 ;print('pass!!!')
    assert count_down_to_songkran(27,10,2024) == 168  ; print('pass!!!')
    assert count_down_to_songkran(31,10,2024) == 164 ; print('pass!!!')
    assert count_down_to_songkran(13,10,2024) == 182 ; print('pass!!!')
    assert count_down_to_songkran(13,10,2023) == 183 ; print('pass!!!')
    assert count_down_to_songkran(13,10,2023) == 183 ; print('pass!!!')
    assert count_down_to_songkran(23,8,2023) == 234 ; print('pass!!!')
    assert count_down_to_songkran(1,4,1600) == 12 ; print('pass!!!')
    assert count_down_to_songkran(1,4,1600) == 12 ; print('pass!!!')
    assert count_down_to_songkran(22,7,3000) == 265 ; print('pass!!!')
    assert count_down_to_songkran(11,11,11) == 154 ; print('pass!!!')

if __name__ == "__main__":
    main()