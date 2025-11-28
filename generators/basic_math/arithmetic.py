import sympy as sp
import random
from mathapp.core import Question, latexify

def addition_question() -> Question:
    a = random.randint(50, 500)
    b = random.randint(50, 500)
    expr_display = f"{latexify(sp.Integer(a))} + {latexify(sp.Integer(b))}"
    textLatex = expr_display + r" = ?"
    answer = sp.Integer(a + b)
    question_expr = sp.Integer(a) + sp.Integer(b)
    return Question(textLatex, answer, "arithmetic_addition", question_expression=question_expr)

def subtraction_question() -> Question:
    a = random.randint(50, 500)
    b = random.randint(50, 500)
    expr_display = f"{latexify(sp.Integer(a))} - {latexify(sp.Integer(b))}"
    textLatex = expr_display + r" = ?"
    answer = sp.Integer(a - b)
    question_expr = sp.Integer(a) - sp.Integer(b)
    return Question(textLatex, answer, "arithmetic_subtraction", question_expression=question_expr)

def multiplication_question() -> Question:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    expr_display = f"{latexify(sp.Integer(a))} \\times {latexify(sp.Integer(b))}"
    textLatex = expr_display + r" = ?"
    answer = sp.Integer(a * b)
    question_expr = sp.Integer(a) * sp.Integer(b)
    return Question(textLatex, answer, "arithmetic_multiplication", question_expression=question_expr)

def division_question() -> Question:
    a = random.randint(1, 20)
    b = a * random.randint(1, 20)
    expr_display = f"{latexify(sp.Integer(b))} / {latexify(sp.Integer(a))}"
    textLatex = expr_display + r" = ?"
    answer = sp.Rational(b, a)
    question_expr = sp.Rational(b, a) if (b % a == 0) else (sp.Integer(b) / sp.Integer(a))
    question_expr = sp.Rational(b, a) if isinstance(answer, sp.Rational) else sp.Integer(b) / sp.Integer(a)
    return Question(textLatex, answer, "arithmetic_division", question_expression=question_expr)

def random_arithmetic_question() -> Question:
    question_generators = [
        addition_question, 
        subtraction_question, 
        multiplication_question, 
        division_question
        ]
    generator = random.choice(question_generators)
    return generator()  