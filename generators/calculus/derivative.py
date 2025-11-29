import sympy as sp
import random
from mathapp.core import Question, latexify
from generators.utils import random_poly_nonconstant

x = sp.symbols('x')

def simple_derivative_question() -> Question:
    # f(x) = ax^n
    a = random.randint(1, 5)
    n = random.randint(2, 5)

    expression = a * x**n
    derivative = sp.diff(expression, x)
    text_latex = r"\frac{d}{dx} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_simple")

def polynomial_derivative_question() -> Question:
    # f(x) = polinomial max derajat 3
    func = random_poly_nonconstant(3, -5, 5)

    expression = func
    
    derivative = sp.diff(expression, x)
    text_latex = r"\frac{d}{dx} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_polynomial")

def trig_derivative_question() -> Question:
    # f(x) = a * trig(bx + c)
    trig_functions = [sp.sin, sp.cos, sp.tan, sp.sec, sp.csc, sp.cot]
    function = random.choice(trig_functions)

    a = random.randint(1, 10)
    b = random.randint(1, 5)
    c = random.randint(0, 5)

    expression = a * function(b * x + c)
    derivative = sp.diff(expression, x)
    text_latex = r"\frac{d}{dx} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_trig")

def exp_derivative_question() -> Question:
    # f(x) = a * exp(b(x^n))
    a = random.randint(1, 10)
    b = random.randint(1, 5)
    n = random.randint(1, 3)

    expression = a * sp.exp(b * x**n)
    derivative = sp.diff(expression, x)
    text_latex = r"\frac{d}{dx} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_exponential")

def rational_derivative_question() -> Question:
    # f(x) = (ax^m + b)/(cx^n + d)
    a = random.randint(1, 5)
    b = random.randint(0, 5)
    c = random.randint(1, 5)
    d = random.randint(0, 5)
    m = random.randint(1, 3)
    n = random.randint(1, 3)

    numerator = a * x**m + b
    denominator = c * x**n + d
    expression = numerator / denominator
    derivative = sp.diff(expression, x)
    text_latex = r"\frac{d}{dx} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_rational")

def irrational_derivative_question() -> Question:
    # f(x) = sqrt(ax^n + b)
    a = random.randint(1, 5)
    b = random.randint(0, 5)
    n = random.randint(1, 4)

    expression = sp.sqrt(a * x**n + b)
    derivative = sp.diff(expression, x)
    text_latex = r"\frac{d}{dx} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_irrational")

def chain_rule_derivative_question() -> Question:
    # f(x) = (ax^n + b)^m
    a = random.randint(1, 5)
    b = random.randint(0, 5)
    n = random.randint(1, 3)
    m = random.randint(2, 4)

    inner = a * x**n + b
    expression = inner**m
    derivative = sp.diff(expression, x)
    text_latex = r"\frac{d}{dx} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_chain_rule")

def inverse_trig_derivative_question() -> Question:
    # f(x) = a * arcsin(bx + c)
    trig_functions = [sp.asin, sp.acos, sp.atan]
    function = random.choice(trig_functions)

    a = random.randint(1, 10)
    b = random.randint(1, 5)
    c = random.randint(0, 5)

    expression = a * function(b * x + c)
    derivative = sp.diff(expression, x)
    text_latex = r"\frac{d}{dx} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_inverse_trig")

def high_order_derivative_question() -> Question:
    # f(x) = P(x), cari turunan ke-k
    p = random_poly_nonconstant(3, -5, 5)
    k = random.randint(2, 4)

    expression = p
    derivative = sp.diff(expression, x, k)
    text_latex = r"\frac{d^{" + str(k) + r"}}{dx^{" + str(k) + r"}} \left( " + latexify(expression) + r" \right)"

    return Question(text_latex, derivative, "calculus_derivative_high_order")

def random_derivative_question() -> Question:
    question_generators = [
        simple_derivative_question,
        polynomial_derivative_question,
        trig_derivative_question,
        exp_derivative_question,
        rational_derivative_question,
        irrational_derivative_question,
        chain_rule_derivative_question,
        inverse_trig_derivative_question,
        high_order_derivative_question
    ]
    
    generator = random.choice(question_generators)
    return generator()