import sympy as sp
import random
from mathapp.core import Question, latexify

x = sp.symbols('x')

def simple_integral_question() -> Question:
    # f(x) = a * x^n
    a = random.randint(1, 10)
    n = random.randint(1, 4)

    expression = a * x**n
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_simple_integral", question_expression=expression)

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

def inverseTrigIntegralQuestions() -> Question:
    # f(x) = a / sqrt(b^2 - (cx)^2) atau a / sqrt((cx)^2 - b^2) atau a / sqrt(b^2 + (cx)^2)
    a = random.randint(1, 10)
    b = random.randint(1, 3)
    c = random.randint(1, 3)

    radicands = [sp.sqrt(b**2 - (c * x) ** 2), sp.sqrt((c * x) ** 2 - b**2), sp.sqrt(b**2 + (c * x) ** 2)]
    expression = a / random.choice(radicands)
    integral = sp.integrate(expression, x)
    textLatex = r"\int " + latexify(expression) + r" \, dx"

    return Question(textLatex, integral, "calculus_inverse_trig_integral", question_expression=expression)

def random_integral_question() -> Question:
    question_generators = [
        simple_integral_question,
        trig_integral_question,
        exp_integral_question,
        rational_integral_question,
        power_substitution_integral_question,
        inverseTrigIntegralQuestions
    ]
    generator = random.choice(question_generators)
    return generator()