from tkinter import Tk, Label, Button, Entry, Message, END

class Root_work(Tk):
    def __init__(self):
        super().__init__()
        self.font = ("Colibri", 15)
        self.font_bold = ("Colibri", 15, "bold")
        self.geometry("1550x750")
        self.title("Workstation")
        self.configure(bg="gray")
        self.minsize(1250, 600)
        self.maxsize(1920, 1080)

        self.produs_code_message = Message(self, text="ID: ", font=self.font_bold, fg="black")
        self.produs_code_message.place(x=10, y=10, width=120, height=40)

        self.produs_code_label = Label(self, text="", font=self.font)
        self.produs_code_label.place(x=130, y=10, width=1000, height=40)

        self.produs_name_message = Label(self, text="Name: ", font=self.font_bold, fg="black")
        self.produs_name_message.place(x=10, y=55, width=120, height=40)

        self.produs_name_label = Label(self, text="", font=self.font)
        self.produs_name_label.place(x=130, y=55, width=1000, height=40)

        self.produs_buc_message = Label(self, text="Bucata: ", fg="Black", font=self.font_bold)
        self.produs_buc_message.place(x=1155, y=10, width=100, height=40)

        self.produs_buc_label = Label(self, text="", font=self.font, justify="left")
        self.produs_buc_label.place(x=1255, y=10, width=265, height=40)

        self.produs_pret_message = Label(self, text="Pret: ", fg="Black", font=self.font_bold)
        self.produs_pret_message.place(x=1155, y=55, width=100, height=40)

        self.produs_pret_label = Label(self, text="", font=self.font, justify="left")
        self.produs_pret_label.place(x=1255, y=55, width=265, height=40)

        self.line1 = Label(self)
        self.line1.place(x=0, y=105, width=1920, height=1)

        self.lista_produse_label = Label(self, text="", font=self.font)
        self.lista_produse_label.place(x=10, y=115, width=850, height=600)

        self.line2 = Label(self, bg="gray")
        self.line2.place(x=10, y=714, width=850, height=600)

        self.total_message = Message(self, text="Total: ", font=self.font_bold)
        self.total_message.place(x=10, y=715, width=100, height=40)

        self.total_label = Label(self, text="", font=self.font_bold)
        self.total_label.place(x=110, y=715, width=750, height=40)

        self.white_label = Label(self)
        self.white_label.place(x=885, y=115, width=635, height=600)

        self.clear_button = Button(self, text="Clear", font=self.font_bold, command=self.clear)
        self.clear_button.place(x=885, y=115, width=100, height=80)

        self.add_entry = Entry(self, text="", font=self.font_bold, justify="center")
        self.add_entry.place(x=985, y=115, width=535, height=80)

        self.button_7 = Button(self, text=7, command=self.button_7, font=self.font_bold, bg="light blue")
        self.button_7.place(x=885, y=200, width=100, height=80)

        self.button_8 = Button(self, text=8, command=self.button_8, font=self.font_bold, bg="light blue")
        self.button_8.place(x=995, y=200, width=100, height=80)

        self.button_9 = Button(self, text=9, command=self.button_9, font=self.font_bold, bg="light blue")
        self.button_9.place(x=1105, y=200, width=100, height=80)

        self.button_4 = Button(self, text=4, command=self.button_4, font=self.font_bold, bg="light blue")
        self.button_4.place(x=885, y=290, width=100, height=80)

        self.button_5 = Button(self, text=5, command=self.button_5, font=self.font_bold, bg="light blue")
        self.button_5.place(x=995, y=290, width=100, height=80)

        self.button_6 = Button(self, text=6, command=self.button_6, font=self.font_bold, bg="light blue")
        self.button_6.place(x=1105, y=290, width=100, height=80)

        self.button_1 = Button(self, text=1, command=self.button_1, font=self.font_bold, bg="light blue")
        self.button_1.place(x=885, y=380, width=100, height=80)

        self.button_2 = Button(self, text=2, command=self.button_2, font=self.font_bold, bg="light blue")
        self.button_2.place(x=995, y=380, width=100, height=80)

        self.button_3 = Button(self, text=3, command=self.button_3, font=self.font_bold, bg="light blue")
        self.button_3.place(x=1105, y=380, width=100, height=80)

        self.search_button = Button(self,text="Search", command=self.search, font=self.font_bold, bg="light blue")
        self.search_button.place(x=885, y=470, width=100, height=80)

        self.button_0 = Button(self, text=0, command=self.button_0, font=self.font_bold, bg="light blue")
        self.button_0.place(x=995, y=470, width=100, height=80)

        self.dot_button = Button(self,text=".", command=self.dot, font=self.font_bold, bg="light blue")
        self.dot_button.place(x=1105, y=470, width=100, height=80)

        self.add_button = Button(self,text="Add", font=self.font_bold, bg="light green", command=self.add)
        self.add_button.place(x=1215, y=200, width=300, height=80)

        self.delete_button = Button(self,text="Delete", font=self.font_bold, bg="light green", command=self.delete)
        self.delete_button.place(x=1215, y=290, width=300, height=80)

        self.anulare_button = Button(self,text="Anulare", font=self.font_bold, bg="light green", command=self.anulare)
        self.anulare_button.place(x=1215, y=380, width=300, height=80)

        self.pachet_button = Button(self,text="Pachet", font=self.font_bold, bg="light blue", command=self.pachet)
        self.pachet_button.place(x=1215, y=470, width=300, height=80)

    def search(self):
        print("Hello")

    def button_0(self):
        self.add_entry.insert(END, 0)

    def button_1(self):
        self.add_entry.insert(END, 1)

    def button_2(self):
        self.add_entry.insert(END, 2)

    def button_3(self):
        self.add_entry.insert(END, 3)

    def button_4(self):
        self.add_entry.insert(END, 4)

    def button_5(self):
        self.add_entry.insert(END, 5)

    def button_6(self):
        self.add_entry.insert(END, 6)

    def button_7(self):
        self.add_entry.insert(END, 7)

    def button_8(self):
        self.add_entry.insert(END, 8)

    def button_9(self):
        self.add_entry.insert(END, 9)

    def clear(self):
        self.add_entry.delete(0, END)

    def dot(self):
        self.add_entry.insert(END, ".")

    def add(self):
        pass

    def delete(self):
        pass

    def anulare(self):
        pass

    def pachet(self):
        pass



if __name__ == "__main__":
    root2 = Root_work()
    root2.mainloop()