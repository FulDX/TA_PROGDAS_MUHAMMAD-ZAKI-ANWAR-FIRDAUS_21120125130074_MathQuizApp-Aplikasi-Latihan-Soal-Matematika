import sympy as sp
import random
from mathapp.core import Question, latexify

x = sp.symbols('x')

def exponent_question() -> Question:
    # f(x) = a^b
    a = random.randint(2, 5)
    b = random.randint(2, 4)
    display_expr_latex = latexify(sp.Integer(a)) + "^{" + latexify(sp.Integer(b)) + "}"
    answer = sp.Integer(a ** b)
    textLatex = display_expr_latex
    question_expr = sp.Pow(sp.Integer(a), sp.Integer(b), evaluate=False)
    return Question(textLatex + " = ?", answer, "basic_math_exponent", question_expression=question_expr)

def exponent_mult_question() -> Question:
    # a^m * a^n 
    a = random.randint(2, 10)
    m = random.randint(1, 10)
    n = random.randint(1, 10)
    
    expression = sp.Pow(sp.Integer(a), m, evaluate=False) * sp.Pow(sp.Integer(a), n, evaluate=False)
    question_expr = sp.Mul(sp.Pow(sp.Integer(a), m, evaluate=False), sp.Pow(sp.Integer(a), n, evaluate=False), evaluate=False)
    simplified = sp.simplify(sp.Pow(sp.Integer(a), m) * sp.Pow(sp.Integer(a), n))
    textLatex = latexify(sp.Integer(a)) + "^{" + str(m) + "} \\times " + latexify(sp.Integer(a)) + "^{" + str(n) + "}"

    return Question(textLatex + " = ?", simplified, "basic_math_exponent_multiplication", question_expression=question_expr)

def exponent_div_question() -> Question:
    # a^m / a^n 
    a = random.randint(2, 10)
    m = random.randint(2, 10)
    n = random.randint(1, m) 
    
    expression = sp.Pow(sp.Integer(a), m, evaluate=False) / sp.Pow(sp.Integer(a), n, evaluate=False)
    question_expr = sp.Mul(sp.Pow(sp.Integer(a), m, evaluate=False), sp.Pow(sp.Integer(a), n, evaluate=False), evaluate=False)
    simplified = sp.simplify(sp.Pow(sp.Integer(a), m) / sp.Pow(sp.Integer(a), n))
    textLatex = latexify(sp.Integer(a)) + "^{" + str(m) + "} / " + latexify(sp.Integer(a)) + "^{" + str(n) + "}"

    return Question(textLatex + " = ?", simplified, "basic_math_exponent_division", question_expression=question_expr)

def exponent_mult_rule() -> Question:
    # a^n * b^n
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    n = random.randint(2, 10)

    expression = sp.Pow(sp.Integer(a), n, evaluate=False) * sp.Pow(sp.Integer(b), n, evaluate=False)
    question_expr = sp.Mul(sp.Pow(sp.Integer(a), n, evaluate=False), sp.Pow(sp.Integer(b), n, evaluate=False), evaluate=False)
    simplified = sp.simplify(sp.Pow(sp.Integer(a), n) * sp.Pow(sp.Integer(b), n))
    textLatex = latexify(sp.Integer(a)) + "^{" + str(n) + "} \\times " + latexify(sp.Integer(b)) + "^{" + str(n) + "}"

    return Question(textLatex + " = ?", simplified, "basic_math_exponent_multiplication_rule", question_expression=question_expr) 

def exponent_div_rule() -> Question:
    # a^n / b^n
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    n = random.randint(2, 10)

    expression = sp.Pow(sp.Integer(a), n, evaluate=False) / sp.Pow(sp.Integer(b), n, evaluate=False)
    question_expr = sp.Mul(sp.Pow(sp.Integer(a), n, evaluate=False), sp.Pow(sp.Integer(b), -n, evaluate=False), evaluate=False)
    simplified = sp.simplify(sp.Pow(sp.Integer(a), n) / sp.Pow(sp.Integer(b), n))
    textLatex = latexify(sp.Integer(a)) + "^{" + str(n) + "} / " + latexify(sp.Integer(b)) + "^{" + str(n) + "}"

    return Question(textLatex + " = ?", simplified, "basic_math_exponent_division_rule", question_expression=question_expr)

def log_question() -> Question:
    # log_b(a)
    b = random.randint(2, 5)
    a = b ** random.randint(1, 4) 

    expression = sp.log(a, b)
    textLatex = r"\log_{" + latexify(b) + "}{" + latexify(a) + "}"

    return Question(textLatex + " = ?", expression, "basic_math_logarithm", question_expression=expression)

def random_explog_question() -> Question:
    question_generators = [
        exponent_question, 
        exponent_mult_question, 
        exponent_div_question, 
        exponent_mult_rule,
        exponent_div_rule,
        log_question
        ]
    generator = random.choice(question_generators)
    return generator()