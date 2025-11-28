import tkinter as tk
from tkinter import ttk

import random

from mathapp.ui_utils import apply_click_effect

from generators.basic_math.arithmetic import random_arithmetic_question
from generators.basic_math.algebra import random_algebra_question
from generators.basic_math.explog import random_explog_question
from generators.series.series import arithmetic_series_question, geometric_series_question, geometric_infinite_series_question, random_series_question
from generators.calculus.limit import random_limit_question
from generators.calculus.derivative import random_derivative_question
from generators.calculus.integral import random_integral_question

from mathapp.latex_renderer import latex_to_photoimage
from mathapp.core import Question, checkMathAnswer

class QuestionPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")

        self.controller = controller

        self.title_label = ttk.Label(
            self, text="Question",
            background=controller.page_bg,
            foreground="white",
            font=("Helvetica", 30, "bold"),
            anchor='nw', justify='left'
        )
        self.title_label.place(x=21, y=19, width=222, height=52)
        self.question_number_label = ttk.Label(
            self, text="1/10",
            background=controller.page_bg,
            foreground="white",
            font=("Helvetica", 30, "bold"),
            anchor='nw', justify='left'
        )
        self.question_number_label.place(x=358, y=22, width=105, height=42)

        self.benar_label = ttk.Label(
            self, text="Benar: 0",
            background=controller.page_bg,
            foreground="white",
            font=("Helvetica", 22, "bold"),
            anchor='nw', justify='left'
        )
        self.benar_label.place(x=537, y=29, width=125, height=41)

        self.salah_label = ttk.Label(
            self, text="Salah: 0",
            background=controller.page_bg,
            foreground="white",
            font=("Helvetica", 22, "bold"),
            anchor='nw', justify='left'
        )
        self.salah_label.place(x=660, y=29, width=125, height=41)

        self.question_box = tk.Canvas(
            self,
            width=760,
            height=200,
            bg="white",
            highlightthickness=2,
            highlightbackground="black"
        )
        self.question_box.place(x=20, y=100)

        self.answer_box = tk.Canvas(
            self,
            width=556,
            height=49,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.answer_box.place(x=132, y=337)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(
            self.answer_box,
            textvariable=self.answer_var,
            font=("Helvetica", 26),
            bg="#D9D9D9",
            bd=0,
            justify="center"
        )
        self.answer_entry.place(relx=0.5, rely=0.5, anchor="center", width=556)

        self.submit_button = tk.Button(
            self,
            text="Submit",
            bg="#6EFFA8",
            fg="white",
            font=("Helvetica", 24, "bold"),
            borderwidth=0,
            activebackground="#63e79e"
        )
        self.submit_button.place(x=310, y=405, width=180, height=60)
        apply_click_effect(self.submit_button)
        self.submit_button.config(command=self.submit_answer)

        self.back_button = tk.Button(
            self,
            text="Kembali",
            bg="black",
            fg="white",
            font=("Helvetica", 18, "bold"),
            borderwidth=0
        )
        self.back_button.place(x=20, y=500, width=120, height=40)
        apply_click_effect(self.back_button, swap=True)

        def _back_to_start():
            from .start_page import MulaiPage
            controller.show_frame(MulaiPage)
        self.back_button.config(command=_back_to_start)

    def start_mode(self, mode="standard", kind=None):
        self.mode = mode
        self.kind = kind
        self.benar_value = 0
        self.salah_value = 0
        self.question_index = 0
        
        try:
            self.benar_label.config(text=f"Benar: {self.benar_value}")
            self.salah_label.config(text=f"Salah: {self.salah_value}")
            self.question_number_label.config(text=f"{self.question_index}/10")

            try:
                self.answer_var.set("")
            except Exception:
                pass

            try:
                if isinstance(self.question_box, tk.Canvas):
                    if hasattr(self, '_question_img_id'):
                        self.question_box.delete(self._question_img_id)
                    if hasattr(self, '_question_text_id'):
                        self.question_box.delete(self._question_text_id)
                else:
                    self.question_box.configure(text="")
            except Exception:
                pass
        except Exception:
            pass
        self.next_question()

    def next_question(self):
        self.question_index = getattr(self, 'question_index', 0) + 1
        try:
            self.question_number_label.config(text=f"{self.question_index}/10")
        except Exception:
            pass

        if getattr(self, 'kind', None) == 'arithmetic':
            q = random_arithmetic_question()
            self.type_label = "Aritmetika"
        elif getattr(self, 'kind', None) == 'algebra':
            q = random_algebra_question()
            self.type_label = "Aljabar"
        elif getattr(self, 'kind', None) == 'explog':
            q = random_explog_question()
            self.type_label = "ExpLog"
        elif getattr(self, 'kind', None) == 'arithmetic_ser':
            q = arithmetic_series_question()
            self.type_label = "Der-At"
        elif getattr(self, 'kind', None) == 'geometric_serfin':
            q = geometric_series_question()
            self.type_label = "Der-Gt-Fin"
        elif getattr(self, 'kind', None) == 'geometric_serinf':
            q = geometric_infinite_series_question()
            self.type_label = "Der-Gt-Inf"
        elif getattr(self, 'kind', None) == 'limit':
            q = random_limit_question()
            self.type_label = "Limit"
        elif getattr(self, 'kind', None) == 'derivative':
            q = random_derivative_question()
            self.type_label = "Turunan"
        elif getattr(self, 'kind', None) == 'integral':
            q = random_integral_question()
            self.type_label = "Integral"
        else:
            print("Unknown kind for standard mode")
            return

        self.title_label.config(text=self.type_label)
        self.controller.current_question = q
        self.render_question(q)
    
    def render_question(self, question: Question):
        
        try:
            txt = question.get_text_latex()
        except Exception:
            txt = getattr(question, 'question_text', '')
        img = latex_to_photoimage(txt)

        try:
            if isinstance(self.question_box, tk.Canvas):
                try:
                    if hasattr(self, '_question_text_id'):
                        self.question_box.delete(self._question_text_id)
                except Exception:
                    pass

                try:
                    if hasattr(self, '_question_img_id'):
                        self.question_box.delete(self._question_img_id)
                except Exception:
                    pass

                cx = 760 // 2
                cy = 200 // 2
                self._question_img_id = self.question_box.create_image(cx, cy, image=img)

                self.question_box.image = img
            else:
                self.question_box.configure(image=img, text="")
                self.question_box.image = img
        except Exception:
            try:
                self.question_box.configure(text=txt)
            except Exception:
                pass

        self.answer_var.set("")

    def submit_answer(self):
        user = self.answer_var.get().strip()
        q = self.controller.current_question
        if checkMathAnswer(user, q):
            self.benar_value += 1
            self.benar_label.config(text=f"Benar: {self.benar_value}")
        else:
            self.salah_value += 1
            self.salah_label.config(text=f"Salah: {self.salah_value}")
        
        if getattr(self, 'mode', None) == 'standard' and getattr(self, 'question_index', 0) >= 10:
            
            score = getattr(self, 'benar_value', 0)
            if score >= 9:
                rating = 'A'
            elif score >= 7:
                rating = 'B'
            elif score >= 5:
                rating = 'C'
            elif score >= 3:
                rating = 'D'
            else:
                rating = 'E'
            try:
                from .result_page import ResultPage
                result_page = self.controller.frames[ResultPage]
                tipe = self.type_label
                result_page.update_result(tipe, self.benar_value, self.salah_value, rating)
                self.controller.show_frame(ResultPage)
            except Exception:
                import traceback
                print(traceback.format_exc())
        else:
            self.next_question()
        
        
        if self.mode == "standard":
            try:
                self.question_number_label.config(text=f"{self.question_index}/10")
            except Exception:
                pass

class QuestionEndlessPage(QuestionPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        try:
            try:
                self.question_number_label.place_forget()
            except Exception:
                pass
            self.question_endless_label = ttk.Label(
                self, text="Endless",
                background=controller.page_bg,
                foreground="red",
                font=("Helvetica", 30, "bold"),
                anchor='nw', justify='left'
            )
            self.question_endless_label.place(x=323, y=19, width=156, height=47)
        except Exception:
            pass

        self.submit_button = tk.Button(
            self,
            text="Submit",
            bg="#6EFFA8",
            fg="white",
            font=("Helvetica", 24, "bold"),
            borderwidth=0,
            activebackground="#63e79e"
        )
        self.submit_button.place(x=310, y=405, width=180, height=60)
        apply_click_effect(self.submit_button)
        self.submit_button.config(command=self.submit_answer)

        self.back_button = tk.Button(
            self,
            text="Kembali",
            bg="black",
            fg="white",
            font=("Helvetica", 18, "bold"),
            borderwidth=0
        )
        self.back_button.place(x=20, y=500, width=120, height=40)
        apply_click_effect(self.back_button, swap=True)
        
        def _back_to_start():
            from .start_page import EndlessPage
            controller.show_frame(EndlessPage)
        self.back_button.config(command=_back_to_start)

    def start_mode(self, mode="endless", kind=None):
        super().start_mode(mode=mode, kind=kind)
        

    def next_question(self):

        if getattr(self, 'kind', None) == 'basic':
            q = random.choice([
                random_arithmetic_question,
                random_algebra_question,
                random_explog_question
            ])()
            self.type_label = "Basic"
        elif getattr(self, 'kind', None) == 'series':
            q = random_series_question()
            self.type_label = "Deret"
        elif getattr(self, 'kind', None) == 'calculus':
            q = random.choice([
                random_limit_question,
                random_derivative_question,
                random_integral_question
            ])()
            self.type_label = "Kalkulus"
        elif getattr(self, 'kind', None) == 'all':
            q = random.choice([
                random_arithmetic_question,
                random_algebra_question,
                random_explog_question,
                random_series_question,
                random_limit_question,
                random_derivative_question,
                random_integral_question
            ])()
            self.type_label = "Semua"
        else: 
            print("Unknown kind for endless mode")
            return

        try:
            self.controller.current_question = q
            self.title_label.config(text=self.type_label)
            self.render_question(q)
        except Exception:
            pass

    def render_question(self, question: Question):
        super().render_question(question)
        