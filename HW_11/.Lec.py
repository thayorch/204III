# Sets {}
def set_1():
    s= {2, 4, 5, 6, 7, 8, 9}
    print(2 in s)
    print(3 in s)
    for i in range(10):
        if i not in s:
            print(i, end=" ")
    print("\n")






if __name__ == "__main__":
    set_1()