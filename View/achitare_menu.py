from tkinter import *

class Achitare(Toplevel):
    def __init__(self, callback = None):
        super().__init__()
        self.font("Colibri", 15, "bold")
        self.geometry("500x250+400+200")
        self.title("Menu Achitare")
        self.callback = callback
        self.iconbitmap("python_ico.ico")
