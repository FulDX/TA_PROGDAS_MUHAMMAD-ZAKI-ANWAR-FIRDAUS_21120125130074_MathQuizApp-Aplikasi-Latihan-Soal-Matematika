import tkinter as tk
from tkinter import ttk
from mathapp.ui_utils import apply_click_effect
from .question_page import QuestionPage

class BasicPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        # Keep a reference to the controller for callbacks
        self.controller = controller
        self.title_label = tk.Label(self, text="Basic Math", background=controller.page_bg, foreground="white", font=("Helvetica", 48, "bold"))
        self.title_label.configure(anchor='nw', justify='left')
        self.title_label.place(x=45, y=61, width=459, height=77)

        self.line = tk.Canvas(self, width=710, height=1, bg=controller.page_bg, highlightthickness=0)
        self.line.place(x=45, y=138)

        self.line.create_line(0, 0, 710, 0, fill="#FFFFFF", width=1)

        self.aritmetika_button = tk.Button(self, text="Aritmetika", bg="#6EFFA8", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#6EFFA8", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.aritmetika_button.place(x=50, y=171, width=705, height=95)
        apply_click_effect(self.aritmetika_button)

        self.explog_button = tk.Button(self, text="Eksponen & Logaritma", bg="#6EFFA8", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#6EFFA8", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.explog_button.place(x=50, y=291, width=705, height=95)
        apply_click_effect(self.explog_button)

        self.aljabar_button = tk.Button(self, text="Algebra", bg="#6EFFA8", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#6EFFA8", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.aljabar_button.place(x=50, y=411, width=705, height=95)
        apply_click_effect(self.aljabar_button)

        self.kembali_button = tk.Button(self, text="Kembali", bg="#000000", fg="#FFFFFF", font=("Helvetica", 18, "bold"), activebackground="#000000", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.kembali_button.place(x=21, y=539, width=113, height=45)
        apply_click_effect(self.kembali_button, swap=True)

        def _back_to_start():
            from .start_page import MulaiPage
            controller.show_frame(MulaiPage)
        self.kembali_button.config(command=_back_to_start)

        def start_aritmetika():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "arithmetic")
        self.aritmetika_button.config(command=start_aritmetika)

        def start_explog():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "explog")
        self.explog_button.config(command=start_explog)

        def start_aljabar():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "algebra")
        self.aljabar_button.config(command=start_aljabar)
        

class DeretPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        self.title_label = tk.Label(self, text="Deret", background=controller.page_bg, foreground="white", font=("Helvetica", 48, "bold"))
        self.title_label.configure(anchor='nw', justify='left')
        self.title_label.place(x=45, y=61, width=459, height=77)

        self.line = tk.Canvas(self, width=710, height=1, bg=controller.page_bg, highlightthickness=0)
        self.line.place(x=45, y=138)

        self.line.create_line(0, 0, 710, 0, fill="#FFFFFF", width=1)

        self.aritmetika_ser_button = tk.Button(self, text="Deret Aritmetika", bg="#FFA14E", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FFA14E", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.aritmetika_ser_button.place(x=50, y=171, width=705, height=95)
        apply_click_effect(self.aritmetika_ser_button)

        self.geometri_serfin_button = tk.Button(self, text="Deret Geometri Tentu", bg="#FFA14E", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FFA14E", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.geometri_serfin_button.place(x=50, y=291, width=705, height=95)
        apply_click_effect(self.geometri_serfin_button)

        self.geometri_serinf_button = tk.Button(self, text="Deret Geometri Tak Tentu", bg="#FFA14E", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FFA14E", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.geometri_serinf_button.place(x=50, y=411, width=705, height=95)
        apply_click_effect(self.geometri_serinf_button)

        self.kembali_button = tk.Button(self, text="Kembali", bg="#000000", fg="#FFFFFF", font=("Helvetica", 18, "bold"), activebackground="#000000", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.kembali_button.place(x=21, y=539, width=113, height=45)
        apply_click_effect(self.kembali_button, swap=True)

        def _back_to_start():
            from .start_page import MulaiPage
            controller.show_frame(MulaiPage)
        self.kembali_button.config(command=_back_to_start)

        def start_aritmetika_ser():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "arithmetic_ser")
        self.aritmetika_ser_button.config(command=start_aritmetika_ser)

        def start_geometri_serfin():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "geometric_serfin")
        self.geometri_serfin_button.config(command=start_geometri_serfin)

        def start_geometri_serinf():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "geometric_serinf")
        self.geometri_serinf_button.config(command=start_geometri_serinf)

class KalkulusPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        self.title_label = tk.Label(self, text="Kalkulus", background=controller.page_bg, foreground="white", font=("Helvetica", 48, "bold"))
        self.title_label.configure(anchor='nw', justify='left')
        self.title_label.place(x=45, y=61, width=459, height=77)

        self.line = tk.Canvas(self, width=710, height=1, bg=controller.page_bg, highlightthickness=0)
        self.line.place(x=45, y=138)

        self.line.create_line(0, 0, 710, 0, fill="#FFFFFF", width=1)

        self.limit_button = tk.Button(self, text="Limit", bg="#FF3232", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FF3232", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.limit_button.place(x=50, y=171, width=705, height=95)

        self.turunan_button = tk.Button(self, text="Turunan", bg="#FF3232", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FF3232", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.turunan_button.place(x=50, y=291, width=705, height=95)

        self.integral_button = tk.Button(self, text="Integral", bg="#FF3232", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FF3232", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.integral_button.place(x=50, y=411, width=705, height=95)

        self.kembali_button = tk.Button(self, text="Kembali", bg="#000000", fg="#FFFFFF", font=("Helvetica", 18, "bold"), activebackground="#000000", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.kembali_button.place(x=21, y=539, width=113, height=45)
        apply_click_effect(self.kembali_button, swap=True)

        def _back_to_start():
            from .start_page import MulaiPage
            controller.show_frame(MulaiPage)
        self.kembali_button.config(command=_back_to_start)

        def start_limit():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "limit")
        self.limit_button.config(command=start_limit)

        def start_turunan():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "derivative")
        self.turunan_button.config(command=start_turunan)

        def start_integral():
            controller.show_frame(QuestionPage)
            qs = controller.frames[QuestionPage]
            qs.start_mode("standard", "integral")
        self.integral_button.config(command=start_integral)