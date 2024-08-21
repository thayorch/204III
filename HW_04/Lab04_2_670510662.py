#!/usr/bin/env python3
# Thadchanon Maidee (ICE)
# 670510662
# Lab04_2
# 204111 Sec 001

def main():
    my_min_mid_max(int(input()), int(input()),int(input())) 

def my_min_mid_max(a:int, b:int,c:int ) -> None:
    
    # เงื่อนไข max
    if(a>=b and a>=c):
        max_ = a    
    elif(b>=a and b>=c):
        max_ = b
    else:
        max_ = c
    
    # เงื่อไข min
    if(a<=b and a<=c):
        min_ = a    
    elif(b<=a and b<=c):
        min_ = b
    else:
        min_ = c    
        
    # เงื่อนไข mid 
    if((a!=max_ and a!=min_) or (a==b or a==c)):
        mid_ = a
    elif((b!=max_ and b!=min_) or (b==a or b==c)):
        mid_ = b
    else:
        mid_ = c
    

    

    print(f"min = {min_}\nmid = {mid_}  \nmax = {max_}")

if __name__ == '__main__':
    main()