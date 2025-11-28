import sympy as sp
import random
from mathapp.core import Question, latexify

x = sp.symbols('x')

def linear_question() -> Question:

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(0, 10)
    y = a * x + b

    equation = sp.Eq(y, c)
    solution_list = sp.solve(equation, x)
    solution = solution_list[0] if isinstance(solution_list, (list, tuple)) else solution_list
    textLatex = latexify(equation)

    return Question(textLatex, solution, "algebra_simple_linear", question_expression=y)

def quadratic_question() -> Question:
    # f(x) = ax^2 + bx + c from (x - x1)(x - x2)
    x1 = random.randint(1, 5)
    x2 = random.randint(1, 5)

    equation = sp.Eq(x**2 - (x1 + x2) * x + x1 * x2, 0)
    solution = sp.solve(equation, x)
    textLatex = latexify(equation)

    return Question(textLatex, solution, "algebra_quadratic", question_expression=x**2 - (x1 + x2) * x + x1 * x2)

def exponential_question() -> Question:
    # a^x = b
    a = random.randint(2, 5)
    x_value = random.randint(1, 4)
    b = a ** x_value

    equation = sp.Eq(a**x, b)
    solution = sp.solve(equation, x)
    textLatex = latexify(equation)

    return Question(textLatex, solution, "algebra_exponential", question_expression=a**x)

def random_algebra_question() -> Question:
    question_generators = [
        linear_question, 
        quadratic_question, 
        exponential_question
        ]
    generator = random.choice(question_generators)
    return generator()

