import random
import sympy as sp

x = sp.Symbol('x')

def random_poly_nonconstant(max_deg, a, b):
    while True:
        leading = random.randint(a, b)
        if leading == 0:
            continue

        coeffs = [random.randint(a, b) for _ in range(max_deg)]
        coeffs.append(leading)

        if max_deg >= 1 and all(coeffs[i] == 0 for i in range(1, max_deg + 1)):
            continue

        poly = sum(coeffs[i] * x**i for i in range(max_deg + 1))
        return poly