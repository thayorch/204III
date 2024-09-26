#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW13_1
# 204111 Sec 001

def product_shopping(p_list: dict[str, tuple[float, float]], allowed_w: float, budget: float) -> dict[str, float]:
    lists = all_pattern(p_list, allowed_w, budget)
    result = []
    _len = 0 
    _weight = allowed_w
    _budget = budget

    for product in lists:
        total_weight = 0.0
        total_cost = 0.0

        for i in product:
            total_weight += p_list.get(i, (0,0))[0]
            total_cost += p_list.get(i, (0,0))[1]

        if len(product) >= _len:
            _len = len(product)

            if(total_weight == allowed_w) and (total_cost < _budget):
                _budget = total_cost
                result = product 
                continue

            if total_weight < _weight:
                _weight = total_weight
                _budget = total_cost
                result = product
                continue
        else:
            continue

    result = sorted(result)
    return dict(map(lambda i: (i, p_list.get(i,(0,0))[0]), result))

def all_pattern(p_list, allowed_w, budget):
    
    result = []
    matrix = [[]]
    shoping_list = list(p_list.keys())

    for i in shoping_list:
        matrix += map(lambda x: x + [i],matrix.copy())
    # print(matrix)
    for shoping_list in matrix:
        total_weight = 0.0
        total_cost = 0.0

        for n in shoping_list:
            total_weight += p_list.get(n)[0]
            total_cost += p_list.get(n)[1]

        if total_weight > allowed_w or total_cost > budget:
            continue

        result.append(shoping_list)
    result = sorted(result, key = lambda x: len(x), reverse = True)
    return result



if __name__ == '__main__':
    # p_list = {"chair": (0.4, 450.0), "pillow": (3.5, 315.0), "stool": (0.3, 300.0), "closet": (2.5, 700.0)}
    # allowed_w = 15.0
    # budget = 1450.00
    # print(product_shopping(p_list, allowed_w, budget))

    assert product_shopping({"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.0)},25.0,2500.00) == {'stool': 0.3,'chair': 0.4,'pillow': 3.5}
    assert product_shopping({"chair": (0.4, 450.0), "pillow": (3.5, 315.0),"stool": (0.3, 300.0), "closet": (2.5, 700.0)}, 15.0,1450.00) == {'stool': 0.3,'chair': 0.4,'closet': 2.5}
    assert product_shopping({"a":(0.1,10)},100.0,100.0) == {'a': 0.1}
    assert product_shopping({"a":(0.1,10)},100.0,1.0) == {}
    assert product_shopping({"shirt": (0.13, 1200.), "trousers": (0.36, 850.),"jeans": (0.3, 1300.), "shoes": (0.5, 1200.),"socks": (0.15, 50.)},5.0,4200.00) == {'jeans': 0.3, 'shirt': 0.13, 'socks': 0.15, 'trousers': 0.36}
    # print(product_shopping({'j': (43, 83), 'b': (68, 95), 'f': (35, 12), 
    #                         'g': (45, 58), 'd': (75, 36), 'c': (18, 55), 'x': (92, 80), 'i': (84, 98), 'm': (55, 76), 'q': (78, 38), 'w': (1, 48), 'v': (34, 47), 'l': (0, 86)},67,96))

    assert product_shopping({'j': (43, 83), 'b': (68, 95), 'f': (35, 12), 
                            'g': (45, 58), 'd': (75, 36), 'c': (18, 55), 'x': (92, 80), 'i': (84, 98), 'm': (55, 76), 'q': (78, 38), 'w': (1, 48), 'v': (34, 47), 'l': (0, 86)},67,96) == {'w': 1, 'v': 34}

    print("All Passed!!!")
