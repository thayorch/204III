#!usr/bin/env python3



# (power, coff)

def polynomial_addition(p1: list[tuple[int, float]],p2: list[tuple[int, float]]) -> list[tuple[int, float]]:
    new_p1 = sorted(map(lambda item: item, p1), reverse=True)
    new_p2 = sorted(map(lambda item: item, p2), reverse=True)
    
    result = []
    poly_dict = {}

    # print(new_p1, new_p2)
    
    for power, coeff in p1:
        poly_dict[power] = poly_dict.get(power, 0) + coeff

    for power, coeff in p2:
        poly_dict[power] = poly_dict.get(power, 0) + coeff
    
    result = [(power, coeff) for power, coeff in poly_dict.items() if coeff != 0]
    result.sort(reverse=True, key=lambda x: x[0])
    # print(result)
    return result



if __name__ == "__main__":
    polynomial_addition([(2, 6), (1, 34), (0, -8)], [(2, -6), (0, 2), (1, 1)])

