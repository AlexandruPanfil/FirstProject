from tkinter import *

class Bucati(Toplevel):
    def __init__(self, callback=None):
        super().__init__()
        self.font = ("Colibri", 15, "bold")
        self.geometry("400x200+400+200")
        self.title("Menu Bucati")
        self.callback = callback
        # self.configure(bg="gray")

        self.bucati_info = Label(self, text="Cate bucati adaugati: ", font=self.font)
        self.bucati_info.grid(row=0, column=0, columnspan=3, sticky="nsew", padx= 5, pady= 5)

        self.button_minus = Button(self, text="-", font=self.font, command=self.minus)
        self.button_minus.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.bucati_show = Label(self, text= 1, font=self.font)
        self.bucati_show.grid( row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.button_plus = Button(self, text="+", font=self.font, command=self.plus)
        self.button_plus.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.buttton_done = Button(self, text="Done", font=self.font, command=self.done)
        self.buttton_done.grid(row=2, column=1, sticky = "nsew", padx=5, pady=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)

    def minus(self):
        num = int(self.bucati_show["text"])
        num = max(1, num - 1)
        self.bucati_show["text"] = num
    def plus(self):
        num = int(self.bucati_show["text"])
        num += 1
        self.bucati_show["text"] = num

    def done(self):
        # v1
        # try:
        #     # print(int(self.bucati_show["text"]))
        #     return int(self.bucati_show["text"])
        # finally:
        #     self.destroy()
        num = int(self.bucati_show["text"])
        if self.callback:
            self.callback(num)
        self.destroy()

# if __name__ == "__main__":
#     bucati = Bucati()
#     bucati.mainloop()