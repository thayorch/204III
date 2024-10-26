#!usr/bin/env python3 

def life_path(n: int) -> int:
    if(len(str(n)) == 1):
        return n
    else:
        return life_path(sum(list(map(int, str(n)))))



if __name__ == "__main__":
    print(life_path(13092004))
    # assert life_path(13092004) == 1
