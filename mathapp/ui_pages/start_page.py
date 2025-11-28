import tkinter as tk
from tkinter import ttk
from mathapp.ui_utils import apply_click_effect
from .question_page import QuestionEndlessPage

class MulaiPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        self.title_label = ttk.Label(self, text="Pilih Tipe", background=controller.page_bg, foreground="white", font=("Helvetica", 48, "bold"))
        
        self.title_label.configure(anchor='center', justify='center')
        self.title_label.place(x=170, y=45, width=459, height=77)

        self.line = tk.Canvas(self, width=710, height=1, bg=controller.page_bg, highlightthickness=0)
        self.line.place(x=45, y=138)

        self.line.create_line(0, 0, 710, 0, fill="#FFFFFF", width=1)

        self.basic_button = tk.Button(self, text="Basic", bg="#6EFFA8", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#6EFFA8", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.basic_button.place(x=270, y=171, width=260, height=84)
        apply_click_effect(self.basic_button)

        def _go_to_basic():
            from .type_page import BasicPage
            controller.show_frame(BasicPage)
        self.basic_button.config(command=_go_to_basic)
        
        self.deret_button = tk.Button(self, text="Deret", bg="#FFA14E", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FFA14E", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.deret_button.place(x=270, y=288, width=260, height=84)
        apply_click_effect(self.deret_button)

        def _go_to_deret():
            from .type_page import DeretPage
            controller.show_frame(DeretPage)
        self.deret_button.config(command=_go_to_deret)

        self.kalkulus_button = tk.Button(self, text="Kalkulus", bg="#FF3232", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FF3232", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.kalkulus_button.place(x=270, y=405, width=260, height=84)
        
        def _go_to_kalkulus():
            from .type_page import KalkulusPage
            controller.show_frame(KalkulusPage)
        self.kalkulus_button.config(command=_go_to_kalkulus)

        self.kembali_button = tk.Button(self, text="Kembali", bg="#000000", fg="#FFFFFF", font=("Helvetica", 18, "bold"), activebackground="#000000", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.kembali_button.place(x=21, y=539, width=113, height=45)
        apply_click_effect(self.kembali_button, swap=True)

        def _back_to_main():
            from .main_page import MainMenu
            controller.show_frame(MainMenu)

        self.kembali_button.config(command=_back_to_main)

class EndlessPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        self.title_label = ttk.Label(self, text="Pilih Tipe", background=controller.page_bg, foreground="white", font=("Helvetica", 48, "bold"))
        
        self.title_label.configure(anchor='center', justify='center')
        self.title_label.place(x=170, y=45, width=459, height=77)

        self.line = tk.Canvas(self, width=710, height=1, bg=controller.page_bg, highlightthickness=0)
        self.line.place(x=45, y=138)

        self.line.create_line(0, 0, 710, 0, fill="#FFFFFF", width=1)

        self.basic_button = tk.Button(self, text="Basic", bg="#6EFFA8", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#6EFFA8", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.basic_button.place(x=270, y=171, width=260, height=84)
        apply_click_effect(self.basic_button)
        
        self.deret_button = tk.Button(self, text="Deret", bg="#FFA14E", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FFA14E", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.deret_button.place(x=270, y=267, width=260, height=84)
        apply_click_effect(self.deret_button)

        self.kalkulus_button = tk.Button(self, text="Kalkulus", bg="#FF3232", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FF3232", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.kalkulus_button.place(x=270, y=363, width=260, height=84)
        

        self.semua_button = tk.Button(self, text="Semua", bg="#FF0090", fg="#FFFFFF", font=("Helvetica", 36, "bold"), activebackground="#FF0090", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.semua_button.place(x=270, y=457, width=260, height=84)
        

        self.kembali_button = tk.Button(self, text="Kembali", bg="#000000", fg="#FFFFFF", font=("Helvetica", 18, "bold"), activebackground="#000000", activeforeground="#FFFFFF", borderwidth=0, highlightthickness=0)
        self.kembali_button.place(x=21, y=539, width=113, height=45)
        apply_click_effect(self.kembali_button, swap=True)

        def go_to_basic():
            controller.show_frame(QuestionEndlessPage)
            qs = controller.frames[QuestionEndlessPage]
            qs.start_mode("endless", "basic")
        self.basic_button.config(command=go_to_basic)

        def go_to_deret():
            controller.show_frame(QuestionEndlessPage)
            qs = controller.frames[QuestionEndlessPage]
            qs.start_mode("endless", "series")
        self.deret_button.config(command=go_to_deret)

        def go_to_kalkulus():
            controller.show_frame(QuestionEndlessPage)
            qs = controller.frames[QuestionEndlessPage]
            qs.start_mode("endless", "calculus")
        self.kalkulus_button.config(command=go_to_kalkulus)

        def go_to_semua():
            controller.show_frame(QuestionEndlessPage)
            qs = controller.frames[QuestionEndlessPage]
            qs.start_mode("endless", "all")
        self.semua_button.config(command=go_to_semua)

        def _back_to_main():
            from .main_page import MainMenu
            controller.show_frame(MainMenu)

        self.kembali_button.config(command=_back_to_main)
