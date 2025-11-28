import sympy as sp
import random
from mathapp.core import Question, latexify

x = sp.symbols('x')

def limit_polynomial_question() -> Question:
    # lim x->p f(x) = ax^3 + bx^2 + cx + d
    a = random.randint(1, 5)
    b = random.randint(0, 5)
    c = random.randint(0, 5)
    d = random.randint(0, 5)

    p = random.randint(1, 5)
    expression = a * x**3 + b * x**2 + c * x + d
    limit_expr = sp.limit(expression, x, p)
    textLatex = r"\lim_{ " + latexify(x) + r"\to " + latexify(sp.Integer(p)) + r"} " + latexify(expression)

    return Question(textLatex, limit_expr, "calculus_limit_polynomial", question_expression=expression)

def limit_rational_question() -> Question:
    # lim x->a f(x) = (x-a)(px + q)/(x-a)(rx + s)
    a = random.randint(1, 5)
    p = random.randint(1, 5)
    q = random.randint(1, 5)
    r = random.randint(1, 5)
    s = random.randint(1, 5)
    
    numerator = sp.simplify(p * x**2 + (q - a * p) * x - a * q)
    denominator = sp.simplify(r * x**2 + (s - a * r) * x - a * s)

    expression = numerator / denominator
    limit_expr = sp.limit(expression, x, a)
    textLatex = r"\lim_{ " + latexify(x) + r"\to " + latexify(sp.Integer(a)) + r"} " + latexify(expression)

    return Question(textLatex, limit_expr, "calculus_limit_rational", question_expression=expression)

def limit_infinity_rational() -> Question:
    # lim x->infinity of f(x) = (ax^2 + bx + c)/(dx^2 + ex + f)
    a = random.randint(1, 5)
    b = random.randint(0, 5)
    c = random.randint(0, 5)
    d = random.randint(1, 5)
    e = random.randint(0, 5)
    f = random.randint(0, 5)

    numerator = a * x**2 + b * x + c
    denominator = d * x**2 + e * x + f

    expression = numerator / denominator
    limit_expr = sp.limit(expression, x, sp.oo)
    textLatex = r"\lim_{ " + latexify(x) + r"\to \infty} " + latexify(expression)

    return Question(textLatex, limit_expr, "calculus_limit_infinity", question_expression=expression)

def limit_infinity_irrational() -> Question:
    # lim x->infinity of f(x) = sqrt(ax^2 + bx + c) - sqrt(ax^2 + qx + r)
    a = random.randint(1, 5)
    b = random.randint(0, 5)
    c = random.randint(0, 5)
    q = random.randint(0, 5)
    r = random.randint(0, 5)

    expression = sp.sqrt(a * x**2 + b * x + c) - sp.sqrt(a * x**2 + q * x + r)
    limit_expr = sp.limit(expression, x, sp.oo)
    textLatex = r"\lim_{ " + latexify(x) + r"\to \infty} " + latexify(expression)

    return Question(textLatex, limit_expr, "calculus_limit_infinity_irrational", question_expression=expression)

def random_limit_question() -> Question:
    question_generators = [
        limit_polynomial_question,
        limit_rational_question,
        limit_infinity_rational,
        limit_infinity_irrational
    ]
    generator = random.choice(question_generators)
    return generator()