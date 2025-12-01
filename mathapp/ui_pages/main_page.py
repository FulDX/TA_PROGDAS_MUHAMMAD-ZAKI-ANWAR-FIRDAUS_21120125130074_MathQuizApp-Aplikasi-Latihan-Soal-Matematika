import tkinter as tk
from tkinter import ttk
from mathapp.ui_utils import apply_click_effect

class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")

        self.title_label = ttk.Label(
            self, 
            text="Math Quiz App", 
            background=controller.page_bg, 
            foreground="white", 
            font=("Helvetica", 48, "bold")
        )
        self.title_label.configure(anchor='center', justify='center')
        self.title_label.place(x=170, y=45, width=459, height=77)

        self.line = tk.Canvas(
            self, 
            width=710, 
            height=1, 
            bg=controller.page_bg, 
            highlightthickness=0
        )
        self.line.place(x=45, y=138)
        self.line.create_line(0, 0, 710, 0, fill="#FFFFFF", width=1)

        self.mulai_button = tk.Button(
            self, 
            text="Mulai", 
            bg="#6EFFA8", 
            fg="#FFFFFF", 
            font=("Helvetica", 36, "bold"), 
            activebackground="#6EFFA8", 
            activeforeground="#FFFFFF", 
            borderwidth=0, 
            highlightthickness=0
        )
        self.mulai_button.place(x=270, y=171, width=260, height=84)
        apply_click_effect(self.mulai_button)

        self.endless_button = tk.Button(self, 
            text="Endless", 
            bg="#FF4E51", 
            fg="#FFFFFF", 
            font=("Helvetica", 36, "bold"), 
            activebackground="#FF4E51", 
            activeforeground="#FFFFFF", 
            borderwidth=0, 
            highlightthickness=0
        )
        self.endless_button.place(x=270, y=288, width=260, height=84)

        self.keluar_button = tk.Button(self, 
            text="Keluar", 
            bg="#000000", 
            fg="#FFFFFF", 
            font=("Helvetica", 36, "bold"), 
            activebackground="#000000", 
            activeforeground="#FFFFFF", 
            borderwidth=0, 
            highlightthickness=0
        )
        self.keluar_button.place(x=270, y=405, width=260, height=84)
        apply_click_effect(self.keluar_button, swap=True)

        def _open_mulai():
            from .start_page import MulaiPage
            controller.show_frame(MulaiPage)
        self.mulai_button.config(command=_open_mulai)

        def _open_endless():
            from .start_page import EndlessPage
            controller.show_frame(EndlessPage)
        self.endless_button.config(command=_open_endless)

        def _exit():
            controller.destroy()
        self.keluar_button.config(command=_exit)
