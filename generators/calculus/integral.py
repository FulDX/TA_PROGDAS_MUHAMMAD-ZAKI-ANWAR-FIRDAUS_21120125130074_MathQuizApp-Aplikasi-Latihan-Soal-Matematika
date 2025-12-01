import sympy as sp
import random
from mathapp.core import Question, latexify
from generators.utils import *

x = sp.symbols('x')

def simple_integral_question() -> Question:
    # f(x) = a * x^n
    a = random.randint(1, 10)
    n = random.randint(1, 4)

    expression = a * x**n
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_simple_integral", question_expression=expression)

def polynomial_integral_question() -> Question:
    func = random_poly_nonconstant(3, -5, 5)

    expression = func
    
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_polynomial_integral", question_expression=expression)

def trig_integral_question() -> Question:
    # f(x) = a * trig(bx + c)
    trig_functions = [sp.sin, sp.cos, sp.tan, sp.sec, sp.csc, sp.cot]
    function = random.choice(trig_functions)

    a = random.randint(1, 10)
    b = random.randint(1, 5)
    c = random.randint(0, 5)

    expression = a * function(b * x + c)
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_trig_integral", question_expression=expression)

def exp_integral_question() -> Question:
    # f(x) = a * exp(b(x^n))
    a = random.randint(1, 10)
    b = random.randint(1, 5)


    expression = a * sp.exp(b * x)
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_exponential_integral", question_expression=expression)

def rational_integral_question() -> Question:
    # f(x) = a / (bx + c)
    a = random.randint(1, 10)
    b = random.randint(1, 5)
    c = random.randint(0, 5)

    expression = a / (b * x + c)
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_rational_integral", question_expression=expression)

def power_substitution_integral_question() -> Question:
    # f(x) = a * (bx + c)^n
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(0, 10)
    n = random.randint(0, 4)

    expression = a * (b * x + c)**n
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_power_substitution_integral", question_expression=expression)

def inverse_trig_integral_question() -> Question:
    # f(x) = a / sqrt(b^2 - (cx)^2) atau a / sqrt((cx)^2 - b^2) atau a / sqrt(b^2 + (cx)^2)
    a = random.randint(1, 10)
    b = random.randint(1, 3)
    c = random.randint(1, 3)

    radicands = [sp.sqrt(b**2 - (c * x) ** 2), sp.sqrt((c * x) ** 2 - b**2), sp.sqrt(b**2 + (c * x) ** 2)]
    expression = a / random.choice(radicands)
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_inverse_trig_integral", question_expression=expression)

def definite_integral_question() -> Question:
    # f(x) = a * x^n from x = p to x = q
    a = random.randint(1, 10)
    n = random.randint(1, 4)
    p = random.randint(0, 5)
    q = random.randint(p + 1, p + 6)

    expression = a * x**n
    integral = sp.integrate(expression, (x, p, q))
    textLatex = r"\int_{" + latexify(sp.Integer(p)) + r"}^{" + latexify(sp.Integer(q)) + r"} " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_definite_integral", question_expression=expression)

def definite_integral_trig_question() -> Question:
    # f(x) = a * trig(bx) from x = p to x = q
    a = random.randint(1, 10)
    b = random.randint(1, 2)
    p = 0
    q = sp.pi / random.randint(1, 4)

    trigs = [sp.sin, sp.cos]
    function = random.choice(trigs)

    expression = a * function(b * x)
    integral = sp.integrate(expression, (x, p, q))
    textLatex = r"\int_{" + latexify(sp.Integer(p)) + r"}^{" + latexify(q) + r"} " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_definite_integral_trig", question_expression=expression)

def definite_integral_odd_even_question() -> Question:
    # f(x) = even or odd function from x = -a to x = a
    a = random.randint(1, 5)

    kind = random.choice(["even", "odd"])
    if kind == "even":
        expression = random_even_trig()
    else:
        expression = random_odd_trig()

    integral = sp.integrate(expression, (x, -a, a))
    textLatex = r"\int_{" + latexify(-a) + r"}^{" + latexify(a) + r"} " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_definite_integral_odd_even", question_expression=expression)

def definite_integral_odd_even_trig_question() -> Question:
    # f(x) = even or odd trig function from x = -a to x = a
    a = sp.pi / random.randint(1, 4)

    kind = random.choice(["even", "odd"])
    if kind == "even":
        expression = random_even_trig()
    else:
        expression = random_odd_trig()

    integral = sp.integrate(expression, (x, -a, a))
    textLatex = r"\int_{" + latexify(-a) + r"}^{" + latexify(a) + r"} " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_definite_integral_odd_even_trig", question_expression=expression)

def random_integral_question() -> Question:
    question_generators = [
        simple_integral_question,
        polynomial_integral_question,
        trig_integral_question,
        exp_integral_question,
        rational_integral_question,
        power_substitution_integral_question,
        inverse_trig_integral_question,
        definite_integral_question,
        definite_integral_trig_question,
        definite_integral_odd_even_question,
        definite_integral_odd_even_trig_question
    ]
    generator = random.choice(question_generators)
    return generator()