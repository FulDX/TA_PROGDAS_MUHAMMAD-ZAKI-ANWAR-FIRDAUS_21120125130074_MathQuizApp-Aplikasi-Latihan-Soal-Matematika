import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor

x = sp.symbols('x')

class Question:
    def __init__(self, text_latex, answer_expression, category, question_expression=None):
        self.__text_latex = text_latex
        self.__answer_expression = answer_expression
        self.__category = category
        self.__question_expression = question_expression

    def get_text_latex(self):
        return self.__text_latex
    
    def get_answer_expression(self):
        return self.__answer_expression
    
    def get_category(self):
        return self.__category
    
    def get_question_expression(self):
        return self.__question_expression
    
    def set_category(self, category):
        self.__category = category

    def set_question_expression(self, expr):
        self.__question_expression = expr

def latexify(expr) -> str:
    
    s = sp.latex(expr)
    
    s = s.replace('\\sin^{-1}', '\\arcsin')
    s = s.replace('sin^{-1}', '\\arcsin')
    s = s.replace('\\cos^{-1}', '\\arccos')
    s = s.replace('cos^{-1}', '\\arccos')
    s = s.replace('\\tan^{-1}', '\\arctan')
    s = s.replace('tan^{-1}', '\\arctan')
    s = s.replace('\\sec^{-1}', '\\arcsec')
    s = s.replace('sec^{-1}', '\\arcsec')
    s = s.replace('\\csc^{-1}', '\\arccsc')
    s = s.replace('csc^{-1}', '\\arccsc')
    s = s.replace('\\cot^{-1}', '\\arccot')
    s = s.replace('cot^{-1}', '\\arccot')
    
    s = s.replace('asin', 'arcsin')
    s = s.replace('acos', 'arccos')
    s = s.replace('atan', 'arctan')
    s = s.replace('asec', 'arcsec')
    s = s.replace('acsc', 'arccsc')
    s = s.replace('acot', 'arccot')
    
    return s

def parseUserInput(userText: str) -> str:
    if not isinstance(userText, str):
        raise ValueError("user_input must be a string")
    s = userText.strip()
    
    s = s.replace('^', '**')
    s = s.replace('−', '-')
    s = s.replace('ln', 'log')

    s = s.replace('∞', 'oo')

    import re as _re
    s = _re.sub(r"\b(inf|infty|infinity)\b", 'oo', s, flags=_re.IGNORECASE)
    
    # biar bisa jawab x = ...

    if '=' in s:
        parts = [p.strip() for p in s.split('=')]
        if len(parts) == 2:
            
            if 'x' in parts[0] and parts[1] != '':
                s = parts[1]
    
    return s

def checkMathAnswer(userInput: str, question: Question) -> bool:
    try:
        s = userInput

        # jawaban kosong salah
        if not isinstance(s, str) or s.strip() == "":
            return False

        # a,b == a, b == x = a; x = b = True

        import re
        tokens = [t.strip() for t in re.split(r"[,;]", s) if t.strip() != '']
        if not tokens:
            return False
        
        # dict untuk parsing
        local_dict = {
            'x': x,
            'e': sp.E,
            'pi': sp.pi,
            # trigs
            'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
            'sec': sp.sec, 'csc': sp.csc, 'cot': sp.cot,
            'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan,
            'asec': sp.asec, 'acsc': sp.acsc, 'acot': sp.acot,
            'arcsin': sp.asin, 'arccos': sp.acos, 'arctan': sp.atan,
            'arcsec': sp.asec, 'arccsc': sp.acsc, 'arccot': sp.acot,
            
            # Function lain
            'log': sp.log, 'ln': sp.log, 'sqrt': sp.sqrt, 'exp': sp.exp
        }
        local_dict.update({
            'oo': sp.oo, 'inf': sp.oo, 'infty': sp.oo, 'Infinity': sp.oo, '∞': sp.oo
        })
        # kalo ada simbol bebas di jawaban, tambahin ke local_dict
        try:
            free_syms = getattr(question.get_answer_expression(), 'free_symbols', set())
            for sym in free_syms:
                local_dict[str(sym)] = sym
        except Exception:
            pass
        # cegah biar nggak error kalo user masukin simbol lain, anggap aja simbol baru
        import re
        # dapatkan semua nama simbol yang dikenali
        known_names = set(local_dict.keys())

        def _split_unknown_alpha_token(match):
            token = match.group(0)
            if token in known_names:
                return token
            # pisahkan jadi karakter tunggal dengan '*' (misal: 'abc' -> 'a*b*c')
            return '*'.join(list(token))

        # tambahkan '*' untuk perkalian implisit (angka diikuti variabel/fungsi atau '(')
        s = re.sub(r"(\d|\))\s*(?=[A-Za-z(])", r"\1*", s)
        # pisahkan urutan huruf yang bukan nama yang dikenal menjadi huruf tunggal yang dipisahkan oleh '*'
        s = re.sub(r"[A-Za-z]+", _split_unknown_alpha_token, s)
        transformations = standard_transformations + (implicit_multiplication_application, convert_xor)
        
        userExpressions = []
        userExpressions_struct = []
        for t in tokens:
            t_parsed = parseUserInput(t)
            
            if '=' in t_parsed:
                
                parts = [p.strip() for p in t_parsed.split('=')]
                if len(parts) >= 2 and parts[-1] != '':
                    t_parsed = parts[-1]
            # tambahkan '*' untuk perkalian implisit
            t_parsed = re.sub(r"(\d|\))\s*(?=[A-Za-z(])", r"\1*", t_parsed)
            t_parsed = re.sub(r"[A-Za-z]+", lambda m: _split_unknown_alpha_token(m), t_parsed)
            
            try:
                ue_eval = parse_expr(t_parsed, local_dict=local_dict, transformations=transformations, evaluate=True)
            except Exception:
                ue_eval = parse_expr(t_parsed, local_dict=local_dict, transformations=transformations, evaluate=False)
            
            try:
                ue_struct = parse_expr(t_parsed, local_dict=local_dict, transformations=transformations, evaluate=False)
            except Exception:
                ue_struct = ue_eval
            userExpressions.append(ue_eval)
            userExpressions_struct.append(ue_struct)
        
        userExpression = userExpressions[0] if userExpressions else None

        
        # ------------------------------
        # Define helper matchers
        #    - _sympy_equal: symbolically compare two expressions
        #    - _numeric_close: numeric tolerance check
        #    - _match_single_candidate: compare user expr with one candidate
        #    - _match_user_expressions_to_candidates: match multiple answers to candidates
        # ------------------------------
        def _sympy_equal(a, b, tol=1e-9):
            try:
                a_sym = sp.sympify(a)
                b_sym = sp.sympify(b)
            except Exception:
                try:
                    a_sym = sp.sympify(str(a))
                    b_sym = sp.sympify(str(b))
                except Exception:
                    return False
            try:
                if (a_sym == sp.oo and b_sym == sp.oo) or (a_sym == -sp.oo and b_sym == -sp.oo):
                    return True
            except Exception:
                pass
            try:
                if sp.simplify(a_sym - b_sym) == 0:
                    return True
            except Exception:
                pass
            try:
                ratio = a_sym / b_sym
                if sp.simplify(ratio - 1) == 0:
                    return True
            except Exception:
                pass
            try:
                if sp.simplify(sp.powsimp(a_sym) - sp.powsimp(b_sym)) == 0:
                    return True
            except Exception:
                pass
            try:
                if sp.simplify(sp.together(a_sym - b_sym)) == 0:
                    return True
            except Exception:
                pass
            try:
                if sp.simplify(sp.factor(a_sym - b_sym)) == 0:
                    return True
            except Exception:
                pass
            try:
                diff = sp.N(a_sym - b_sym, 50)
                if abs(diff) < tol:
                    return True
            except Exception:
                pass
            return False

        
        def _numeric_close(a, b, tol=1e-9):
            try:
                da = float(sp.N(a))
                db = float(sp.N(b))
                return abs(da - db) < tol
            except Exception:
                return False

        def _match_single_candidate(ue, candidate):
            try:
                if _sympy_equal(ue, candidate):
                    return True
                diff = sp.N(ue - candidate)
                if abs(diff) < 1e-9:
                    return True
            except Exception:
                if _numeric_close(ue, candidate):
                    return True
            return False

        def _match_user_expressions_to_candidates(user_exprs, candidates):
            # match each user expression to a unique candidate (order unimportant)
            if len(user_exprs) != len(candidates):
                return False
            used = [False] * len(candidates)
            for ue in user_exprs:
                matched = False
                for i, cand in enumerate(candidates):
                    if used[i]:
                        continue
                    if _match_single_candidate(ue, cand):
                        used[i] = True
                        matched = True
                        break
                if not matched:
                    return False
            return True

        try:
            question_expr = question.get_question_expression()
        except Exception:
            question_expr = None
        if question_expr is not None:
            import re
            op_re = re.compile(r"[\+\*\/\^×÷]")
            def _normalize_token_str(s):
                s = s.strip()
                # ganti common latex operators ke textual equivalents
                s = s.replace('\\times', '*').replace('\\cdot', '*')
                
                s = s.replace('\t', '*').replace('\times', '*')
                s = s.replace('\\div', '/').replace('\\frac', '/')
                # samakan ^ jadi **
                s = s.replace('^', '**')
                s = re.sub(r"\s+", "", s)
                return s

            for t, ue, ue_struct in zip(tokens, userExpressions, userExpressions_struct):
                
                try:
                    
                    qtxt = question.get_text_latex()
                    
                    qtxt = re.sub(r"\s*=\s*\?\s*$", "", qtxt)
                    
                    qtxt = qtxt.replace('\\times', '*').replace('\\cdot', '*')
                    qtxt = qtxt.replace('\\div', '/').replace('\\frac', '/')
                    tn = _normalize_token_str(t)
                    qn = _normalize_token_str(qtxt)
                    if tn == qn:
                        return False
                    # Cegah biar user nggak cuma nyalin soal
                    try:
                        # treat only infix operators (not a leading sign) as copying the question
                        has_infix_op = any(op in t[1:] for op in ['+', '-', '*', '/', '^', '×', '÷'])
                        if has_infix_op and sp.srepr(ue_struct) == sp.srepr(question_expr):
                            return False
                    except Exception:
                        pass
                except Exception:
                    pass
                
                try:
                    qtxt = question.get_text_latex()
                    tn = re.sub(r"\s+", "", t)
                    qn = re.sub(r"\s+", "", qtxt)
                    if tn == qn:
                        return False
                except Exception:
                    pass


        # Cek integral
        if isinstance(question.get_category(), str) and 'integral' in question.get_category():
            
            userExpression = userExpressions[0] if userExpressions else None
            if userExpression is None:
                return False
            try:
                category = question.get_category()
            except Exception:
                category = None
            if isinstance(category, str) and 'definite' in category:
                # Untuk integral tentu, cek langsung nilai numeriknya
                correct_val = question.get_answer_expression()
                try:
                    diff = sp.N(userExpression - correct_val)
                    if abs(diff) < 1e-9:
                        return True
                except Exception:
                    try:
                        if abs(float(sp.N(userExpression)) - float(sp.N(correct_val))) < 1e-9:
                            return True
                    except Exception:
                        return False
                return False
            else:
                # Untuk integral tak tentu, cek dengan turunan pertama dari userAnswer - answerExpression == 0
                try:
                    check = sp.simplify(sp.diff(userExpression - question.get_answer_expression(), x))
                    return check == 0
                except Exception:
                    # kalo gagal, coba cek di beberapa titik
                    try:
                        pts = [0, 1, 2]
                        for p in pts:
                            d_user = float(sp.N(sp.diff(userExpression, x).subs(x, p)))
                            d_correct = float(sp.N(sp.diff(question.get_answer_expression(), x).subs(x, p)))
                            if abs(d_user - d_correct) > 1e-6:
                                return False
                        return True
                    except Exception:
                        return False
        # ------------------------------
        # Multi-answer and single-answer handling
        #    - if `correct` is a collection, we need to compare either:
        #      a) user provides same number of answers -> one-to-one matching
        #      b) correct is collection size 1 -> alternative answers (accept single)
        #      c) otherwise -> reject (user must provide all solutions)
        # ------------------------------
        else:
            correct = question.get_answer_expression()
            if isinstance(correct, (list, tuple, set)):
                correct_list = list(correct)
            else:
                correct_list = None
            if correct_list is not None and len(userExpressions) > 1:
                
                if len(userExpressions) != len(correct_list):
                    return False
                
                used = [False] * len(correct_list)
                for ue in userExpressions:
                    matched = False
                    for i, cand in enumerate(correct_list):
                        if used[i]:
                            continue
                        try:
                            if _sympy_equal(ue, cand):
                                used[i] = True
                                matched = True
                                break
                            diff = sp.N(ue - cand)
                            if abs(diff) < 1e-9:
                                used[i] = True
                                matched = True
                                break
                        except Exception:
                            try:
                                diff = float(sp.N(ue) - sp.N(cand))
                                if abs(diff) < 1e-9:
                                    used[i] = True
                                    matched = True
                                    break
                            except Exception:
                                continue
                    if not matched:
                        return False
                return True
            
            if isinstance(correct, (list, tuple, set)):
                # Jika user memberikan jumlah jawaban yang sama dengan kandidat, cocokkan 1-ke-1
                if len(userExpressions) == len(list(correct)):
                    return _match_user_expressions_to_candidates(userExpressions, list(correct))
                # Jika hanya ada 1 kandidat, cocokkan langsung
                if len(list(correct)) == 1 and len(userExpressions) == 1:
                    return _match_single_candidate(userExpressions[0], list(correct)[0])
                # Jika tidak, anggap salah
                return False
            
            if isinstance(correct, (list, tuple, set)):
                # Jika user memberikan satu ekspresi, periksa apakah cocok dengan salah satu kandidat
                if len(userExpressions) == 1:
                    ue = userExpressions[0]
                    for candidate in correct:
                        if _match_single_candidate(ue, candidate):
                            return True
                    return False
                # Jika user memberikan beberapa ekspresi, cocokkan semua dengan kandidat
                return _match_user_expressions_to_candidates(userExpressions, list(correct))
            else:
                return _sympy_equal(userExpression, correct)
    except Exception as e:
        print(f"Error parsing user input: {e}")
        return False