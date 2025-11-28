import sympy as sp
import random
from mathapp.core import Question, latexify

x = sp.symbols('x')

def arithmetic_series_question() -> Question:
    # S_n = sum_{k=1}^{n} (a1 + (k-1) d)
    k = sp.symbols('k', integer=True, positive=True)
    a1 = random.randint(1, 10)
    d = random.randint(1, 6)
    n = random.randint(3, 8)

    sum_symbol = sp.Sum(a1 + (k - 1) * d, (k, 1, n))
    answer = sp.summation(a1 + (k - 1) * d, (k, 1, n))
    textLatex = latexify(sum_symbol) + r" = ?"
    return Question(textLatex, answer, "arithmetic_series", question_expression=answer)

def geometric_series_question() -> Question:
    # finite geometric series: sum_{k=0}^{n-1} a r^k
    k = sp.symbols('k', integer=True, nonnegative=True)
    a = random.randint(1, 8)
    r = random.randint(2, 5)
    n = random.randint(2, 6)

    sum_symbol = sp.Sum(a * r**k, (k, 0, n - 1))
    answer = sp.summation(a * r**k, (k, 0, n - 1))
    textLatex = latexify(sum_symbol) + r" = ?"
    return Question(textLatex, answer, "geometric_series_finite", question_expression=answer)

def geometric_infinite_series_question() -> Question:
    # convergent infinite geometric series: sum_{k=0}^{infty} a r^k, for |r| < 1
    k = sp.symbols('k', integer=True, nonnegative=True)
    a = random.randint(1, 8)

    possible_rs = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 4), sp.Rational(-1, 2), sp.Rational(-1, 3)]
    r = random.choice(possible_rs)
        
    sum_symbol = sp.Sum(a * r**k, (k, 0, sp.oo))

    answer = sp.summation(a * r**k, (k, 0, sp.oo))
    textLatex = latexify(sum_symbol) + r" = ?"
    return Question(textLatex, answer, "geometric_series_infinite", question_expression=answer)


def random_series_question() -> Question:
    question_generators = [
        arithmetic_series_question,
        geometric_series_question,
        geometric_infinite_series_question,
    ]
    generator = random.choice(question_generators)
    return generator()