import random
import sympy as sp

x = sp.Symbol('x')

def random_poly_nonconstant(max_deg=2, a=1, b=5):
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
    
def random_even_function(max_deg=2, a=1, b=5):
    if max_deg % 2 == 1:
        max_deg += 1
    
    terms = []
    for deg in range(0, max_deg + 1, 2):
        coeff = random.randint(a, b)
        if coeff != 0:
            terms.append(coeff * x**deg)
    
    if not terms: 
        return random_even_function(max_deg, a, b)

    return sum(terms)

def random_odd_function(max_deg=2, a=1, b=5):
    if max_deg % 2 == 0:
        max_deg += 1
    
    terms = []
    for deg in range(1, max_deg + 1, 2):
        coeff = random.randint(a, b)
        if coeff != 0:
            terms.append(coeff * x**deg)
    
    if not terms: 
        return random_odd_function(max_deg)

    return sum(terms)

def random_even_trig():
    choices = [
        sp.cos(x),
        sp.cos(2*x),
        sp.cos(3*x),
        sp.sec(x),
        sp.sin(x)**2,
        sp.tan(x)**2,
        sp.sin(2*x)**2,
        sp.tan(2*x)**2
    ]

    n_terms = random.randint(1, 3)
    terms = []

    for _ in range(n_terms):
        coeff = random.randint(-10, 10)
        if coeff != 0:
            terms.append(coeff * random.choice(choices))

    
    if not terms:
        return random_even_trig()

    return sum(terms)

def random_odd_trig():
    choices = [
        sp.sin(x),
        sp.sin(2*x),
        sp.sin(3*x),
        sp.tan(x),
        sp.csc(x),
        sp.cot(x),
        sp.sin(x)*sp.cos(x),
        sp.sin(x)*sp.cos(x)**2,
    ]

    n_terms = random.randint(1, 3)
    terms = []

    for _ in range(n_terms):
        coeff = random.randint(-10, 10)
        if coeff != 0:
            terms.append(coeff * random.choice(choices))

    if not terms:
        return random_odd_trig()

    return sum(terms)

