def main():
    print(print_polynomial([(2, -66), (0, -8), (1, 34)], 'x'))
    print(print_polynomial([(2, 0), (0, -1)], 's'))
    test_polynomial()

def print_polynomial(pc_list, v):
    temp = sorted(pc_list, key=lambda x: x[0], reverse=True)
    power_out = list(map(lambda x: str(x[0]), temp))
    coefficients_out = list(map(lambda x: str(x[1]), temp))
    lists = list(map(lambda i: check_lists(power_out, coefficients_out, v, i), range(len(temp))))
    return ''.join(lists).lstrip('+ ').strip().replace(' + -', ' - ')

def check_lists(power, coefficients, variable, index):
    exp = coefficients_ex(coefficients, index)
    if coefficients[index] == '0':
        return ''
    
    if power[index] == '0':
        return f"{exp} {coefficients[index]} "
    elif power[index] == '1':
        if coefficients[index] == '1':
            return f"{exp} {variable}"
        return f"{exp} {coefficients[index]}{variable} "
    else:
        if coefficients[index] == '1':
            return f"{exp} {variable}^{power[index]}"
        return f"{exp} {coefficients[index]}{variable}^{power[index]}"

def coefficients_ex(coefficients, i):
    if float(coefficients[i]) > 0:
        return '+'
    elif float(coefficients[i]) < 0:
        return '-'
    else:
        return ''

def test_polynomial():
    assert print_polynomial([(2, -6), (0, -8), (1, 34)], 'x') == '-6x^2 + 34x - 8'; print("Pass !!")
    assert print_polynomial([(4, -6), (2, -8), (3, 34)], 'x') == '-6x^4 + 34x^3 - 8x^2'; print("Pass !!")
    assert print_polynomial([(2, -6), (0, -8), (1, 34)], 'y') == '-6y^2 + 34y - 8'; print("Pass !!")
    assert print_polynomial([(2, 6), (0, -8), (1, 34)], 'y') == '6y^2 + 34y - 8'; print("Pass !!")
    assert print_polynomial([(2, 6.5), (0, -8)], 'y') == '6.5y^2 - 8'; print("Pass !!")
    assert print_polynomial([(4, -6), (2, -8), (3, 34), (6, 34), (1, 5)], 'x') == '34x^6 - 6x^4 + 34x^3 - 8x^2 + 5x'; print("Pass !!")
    assert print_polynomial([(4, -6), (2, -8), (3, 0)], 'x') == '-6x^4 - 8x^2'; print("Pass !!")
    assert print_polynomial([(0, 0), (1, 1)], 'y') == 'y'; print("Pass !!")
    assert print_polynomial([(0, 0), (1, 0)], 'y') == '0'; print("Pass !!")
    assert print_polynomial([(0, 0), (1, 5)], 'y') == '5y'; print("Pass !!")
    assert print_polynomial([(0, 5), (1, 0)], 'y') == '5'; print("Pass !!")
    assert print_polynomial([(0, 5), (1, 5)], 'x') == '5x + 5'; print("Pass !!")
    assert print_polynomial([(2, -66), (0, -8), (1, 34)], 'x') == '-66x^2 + 34x - 8'
    assert print_polynomial([(2, 6), (0, -8), (1, 34)], 'y') == '6y^2 + 34y - 8'
    assert print_polynomial([(2, -6), (0, -1), (1, 34)], 'x') == '-6x^2 + 34x - 1'
    assert print_polynomial([(2, -6), (0, 1), (1, 34)], 'x') == '-6x^2 + 34x + 1'
    assert print_polynomial([(2, 6), (0, 0), (1, 0)], 'x') == '6x^2'
    assert print_polynomial([(5, 2), (4, -2), (1, 0)], 'x') == '2x^5 - 2x^4'
    assert print_polynomial([(5, 1), (4, -1), (0, 1)], 'x') == 'x^5 - x^4 + 1'
    assert print_polynomial([(0, 1), (1, 1)], 'x') == 'x + 1'
    assert print_polynomial([(2, -100000), (1, -1), (0, -1), (3, -1)], 'x') == '-x^3 - 100000x^2 - x - 1'
    assert print_polynomial([(0, 1), (1, -1)], 'x') == '-x + 1'
    assert print_polynomial([(2, 0), (0, -1), (1, 0)], 'x') == '-1'
    assert print_polynomial([(1, 0), (0, -2)], 'x') == '-2'
    assert print_polynomial([(1, 0.0001), (1, 0)], 'x') == ''

if __name__ == "__main__":
    main()