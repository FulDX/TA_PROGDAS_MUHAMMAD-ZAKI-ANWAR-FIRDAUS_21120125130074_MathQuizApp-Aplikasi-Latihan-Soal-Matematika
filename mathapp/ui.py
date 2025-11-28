import tkinter as tk
from tkinter import ttk

from mathapp.ui_pages.main_page import MainMenu
from mathapp.ui_pages.start_page import MulaiPage, EndlessPage
from mathapp.ui_pages.type_page import BasicPage, DeretPage, KalkulusPage
from mathapp.ui_pages.question_page import QuestionPage, QuestionEndlessPage
from mathapp.ui_pages.result_page import ResultPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math Quiz App")
        self.geometry("800x600")
        self.resizable(False, False)
        
        self.center_window(800, 600)

        self.page_bg = "#1e1e1e"
        style = ttk.Style()
        style.configure("TFrame", background=self.page_bg)

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, MulaiPage, BasicPage, DeretPage, KalkulusPage,
                  QuestionPage, QuestionEndlessPage, EndlessPage, ResultPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

        self.current_question = None

    
    def center_window(self, w, h):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw // 2) - (w // 2)
        y = (sh // 2) - (h // 2)

        self.geometry(f"{w}x{h}+{x}+{y}")

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
