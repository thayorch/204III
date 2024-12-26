#!usr/bin/env python3
# Thadchanon Maidee(Ice-lnwza)
# 670510662
# HW15_1
# 204111 Sec 001
    
def manga_add(manga_shelf: list[tuple[str, int]], new_m: tuple[str, int], show_steps: bool = False):
    low = 0
    high = len(manga_shelf)-1
    name_keys = new_m[0]
    val_keys = new_m[1]

    if not manga_shelf:
        manga_shelf.append(new_m)
        return
    while low <= high:
        mid = (low+high)//2
        if show_steps:
            print(f"[{mid}] {manga_shelf[mid]}")
        
        if name_keys == manga_shelf[mid][0]:
            if val_keys < manga_shelf[mid][1]: 
                high = mid - 1
            else: 
                low = mid + 1
        elif name_keys < manga_shelf[mid][0]:
            high = mid - 1
        else:
            low = mid + 1

    found = manga_shelf[mid]
    if name_keys < found[0]:
        manga_shelf.insert(mid, new_m)
    elif name_keys > found[0]:
        manga_shelf.insert(mid+1, new_m)
    else:
        if val_keys <= found[1]:
            manga_shelf.insert(mid, new_m)
        else:
            manga_shelf.insert(mid+1, new_m)


if __name__ == '__main__':
    shelf = [('Bleach', 10), ('Naruto', 5), ('One Piece', 24)]
    new = ('Naruto', 18)
    manga_add(shelf, new, True)
    print('--')
    print(shelf)
