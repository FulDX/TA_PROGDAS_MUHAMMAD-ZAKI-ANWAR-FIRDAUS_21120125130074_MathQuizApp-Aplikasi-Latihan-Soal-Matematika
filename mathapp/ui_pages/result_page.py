import tkinter as tk
from tkinter import ttk
from .main_page import MainMenu
from mathapp.ui_utils import apply_click_effect

class ResultPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")

        self.controller = controller

        self.title_label = ttk.Label(
            self,
            text="Result",
            background=controller.page_bg,
            foreground="white",
            anchor="center",
            font=("Helvetica", 36, "bold")
        )
        self.title_label.place(x=322, y=21, width=157, height=54)

        self.box = tk.Frame(
            self,
            bg="#D9D9D9",
        )
        self.box.place(x=227, y=103, width=346, height=396)


        self.tipe_label = tk.Label(
            self.box,
            text="Tipe Soal:",
            bg="#D9D9D9",
            fg="black",
            anchor="w",
            font=("Helvetica", 18, "bold")
        )
        self.tipe_label.place(x=20, y=20, width=150, height=30)

        self.tipe_value = tk.Label(
            self.box,
            text="Aritmetika",
            bg="#D9D9D9",
            fg="black",
            anchor="w",
            font=("Helvetica", 18, "bold")
        )
        self.tipe_value.place(x=180, y=20, width=150, height=30)

        self.benar_label = tk.Label(
            self.box,
            text="Benar:",
            bg="#D9D9D9",
            fg="black",
            anchor="w",
            font=("Helvetica", 18, "bold")
        )
        self.benar_label.place(x=20, y=65, width=150, height=30)

        self.benar_value = tk.Label(
            self.box,
            text="7/10",
            bg="#D9D9D9",
            fg="black",
            anchor="w",
            font=("Helvetica", 18, "bold")
        )
        self.benar_value.place(x=180, y=65, width=150, height=30)

        self.salah_label = tk.Label(
            self.box,
            text="Salah:",
            bg="#D9D9D9",
            fg="black",
            anchor="w",
            font=("Helvetica", 18, "bold")
        )
        self.salah_label.place(x=20, y=110, width=150, height=30)

        self.salah_value = tk.Label(
            self.box,
            text="3/10",
            bg="#D9D9D9",
            fg="black",
            anchor="w",
            font=("Helvetica", 18, "bold")
        )
        self.salah_value.place(x=180, y=110, width=150, height=30)

        self.rating_title = tk.Label(
            self.box,
            text="Rating:",
            bg="#D9D9D9",
            fg="black",
            anchor="center",
            font=("Helvetica", 22, "bold")
        )
        self.rating_title.place(x=0, y=170, width=346, height=40)

        self.rating_value = tk.Label(
            self.box,
            text="B",
            bg="#D9D9D9",
            fg="black",
            anchor="center",
            font=("Helvetica", 100, "bold")
        )
        self.rating_value.place(x=0, y=210, width=346, height=150)

        self.back_button = tk.Button(
            self,
            text="Kembali",
            bg="black",
            fg="white",
            font=("Helvetica", 20, "bold"),
            borderwidth=0,
            command=lambda: controller.show_frame(MainMenu)
        )
        self.back_button.place(x=20, y=520, width=140, height=50)
        apply_click_effect(self.back_button, swap=True)

    def rating_score(self, score: int) -> str:
        if score >= 9:
            return 'A'
        elif score >= 7:
            return 'B'
        elif score >= 5:
            return 'C'
        elif score >= 3:
            return 'D'
        else:
            return 'E'

    def update_result(self, tipe, benar, salah):
        self.tipe_value.config(text=tipe)
        self.benar_value.config(text=f"{benar}/10")
        self.salah_value.config(text=f"{salah}/10")
        self.rating_value.config(text=self.rating_score(benar))

class ResultEndlessPage(ResultPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.rating_title.place_forget()
        self.rating_value.place_forget()

        self.total_soal_title = tk.Label(
            self.box,
            text="Total Soal:",
            bg="#D9D9D9",
            fg="black",
            anchor="center",
            font=("Helvetica", 22, "bold")
        )
        self.total_soal_title.place(x=0, y=170, width=346, height=40)

        self.total_soal_value = tk.Label(
            self.box,
            text="B",
            bg="#D9D9D9",
            fg="black",
            anchor="center",
            font=("Helvetica", 100, "bold")
        )
        self.total_soal_value.place(x=0, y=210, width=346, height=150)

    def update_result(self, tipe, benar, salah):
        self.tipe_value.config(text=tipe)
        self.benar_value.config(text=f"{benar}")
        self.salah_value.config(text=f"{salah}")
        self.total_soal_value.config(text=f"{benar + salah}")