#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW14_2
# 204111 Sec 001

def bottom_up_m_sort(list_x: list[int], show_steps: bool=False) -> None:
    list_x[:] = [[x] for x in list_x]

    while len(list_x) >= 1:

        if show_steps:
            print(list_x)

        if len(list_x) == 1:
            list_x[:] = list_x[0]
            break
        
        tmp = []

        for index in range(0, len(list_x), 2):

            if index+1 >= len(list_x):
                tmp.append(list_x[index])
                break

            sorted_ = []
            
            i = 0
            j = 0
            
            while i < len(list_x[index]) and j < len(list_x[index + 1]):
                if list_x[index][i] < list_x[index + 1][j]:
                    sorted_.append(list_x[index][i])
                    i += 1

                elif list_x[index][i] > list_x[index + 1][j]:
                    sorted_.append(list_x[index + 1][j])
                    j += 1

                else:
                    sorted_.extend([list_x[index][i], list_x[index + 1][j]])
                    i += 1
                    j += 1

            sorted_.extend(list_x[index][i:])
            sorted_.extend(list_x[index + 1][j:])
            tmp.append(sorted_)

        list_x.clear()
        list_x.extend(tmp)
            


if __name__ == '__main__':
    list_x = [3, 7, 4, 9, 5, 2, 6]
    bottom_up_m_sort(list_x, True)
    print('--------')
    print(list_x)
