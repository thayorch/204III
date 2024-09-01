#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# HW10_3
# 204111 Sec 001
def polynomial_addition(p1: list[tuple[int, float]], p2: list[tuple[int, float]]) -> list[tuple[int, float]]:
    i, j = 0, 0
    result = []
    
    # Traverse both polynomials
    while i < len(p1) and j < len(p2):
        degree1, coef1 = p1[i]
        degree2, coef2 = p2[j]
        
        if degree1 == degree2:
            # If degrees are the same, add coefficients
            if coef1 + coef2 != 0:  # Only add if the result is non-zero
                result.append((degree1, coef1 + coef2))
            i += 1
            j += 1
        elif degree1 > degree2:
            # If degree1 is larger, add the term from p1
            result.append((degree1, coef1))
            i += 1
        else:
            # If degree2 is larger, add the term from p2
            result.append((degree2, coef2))
            j += 1
    
    # Add remaining terms from p1 or p2
    while i < len(p1):
        result.append(p1[i])
        i += 1
    while j < len(p2):
        result.append(p2[j])
        j += 1
    
    return result

if __name__ == '__main__':
    print("Testing...")
    assert polynomial_addition([(2, 6), (1, 34), (0, -8)],[(2, -6), (0, 2), (1, 1)]) == [(1, 35), (0, -6)]
    print("All Pass!!")