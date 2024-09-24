#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW13_1
# 204111 Sec 001

def product_shopping(p_list: dict[str, tuple[float, float]], allowed_w: float, budget: float) -> dict[str, float]:
    shopping_list = {}
    total_weight = 0.0
    total_cost = 0.0
    
    for item, (weight, cost) in p_list.items():
        if total_weight + weight <= allowed_w and total_cost + cost <= budget:
            shopping_list[item] = weight
            total_weight += weight
            total_cost += cost
        
        # print(shopping_list)
        
    return shopping_list

if __name__ == '__main__':
    # p_list = {"chair": (0.4, 450.0), "pillow": (3.5, 315.0), "stool": (0.3, 300.0), "closet": (2.5, 700.0)}
    # allowed_w = 15.0
    # budget = 1450.00
    # print(product_shopping(p_list, allowed_w, budget))

    # assert product_shopping({"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.0)},25.0,2500.00) == {'stool': 0.3,'chair': 0.4,'pillow': 3.5}
    # assert product_shopping({"chair": (0.4, 450.0), "pillow": (3.5, 315.0),"stool": (0.3, 300.0), "closet": (2.5, 700.0)}, 15.0,1450.00) == {'stool': 0.3,'chair': 0.4,'closet': 2.5}
    # assert product_shopping({"a":(0.1,10)},100.0,100.0) == {'a': 0.1}
    # assert product_shopping({"a":(0.1,10)},100.0,1.0) == {}
    # assert product_shopping({"shirt": (0.13, 1200.), "trousers": (0.36, 850.),"jeans": (0.3, 1300.), "shoes": (0.5, 1200.),"socks": (0.15, 50.)},5.0,4200.00) == {'jeans': 0.3, 'shirt': 0.13, 'socks': 0.15, 'trousers': 0.36}
    print(product_shopping({'j': (43, 83), 'b': (68, 95), 'f': (35, 12), 
                            'g': (45, 58), 'd': (75, 36), 'c': (18, 55), 'x': (92, 80), 'i': (84, 98), 'm': (55, 76), 'q': (78, 38), 'w': (1, 48), 'v': (34, 47), 'l': (0, 86)},67,96))
    
    assert product_shopping({'j': (43, 83), 'b': (68, 95), 'f': (35, 12), 
                            'g': (45, 58), 'd': (75, 36), 'c': (18, 55), 'x': (92, 80), 'i': (84, 98), 'm': (55, 76), 'q': (78, 38), 'w': (1, 48), 'v': (34, 47), 'l': (0, 86)},67,96) == {'w': 1, 'v': 34}
