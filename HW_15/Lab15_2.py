#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# Lab15_2
# 204111 Sec 001

def unique_combo(heaps: list[tuple[str]]) -> set[tuple[str]]:
    return {tuple(sorted(set(i))) for i in heaps}

if __name__ == "__main__":
        print(unique_combo([('red', 'green', 'blue', 'blue'), ('blue', 'green', 'red'), ('green', 'blue', 'red'), ('pink', 'purple', 'orange', 'pink'), ('orange', 'purple', 'pink')]))
