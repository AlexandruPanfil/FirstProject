from tkinter import * #Tk, Label, Button, Entry, Message, END, Menu, Frame, LEFT, BOTH
from tkinter import ttk #Treeview
from tkinter.ttk import Treeview
from View.bucati_menu import Bucati
from Controler.Database import products_db

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
        # self.menu_bar = Menu(self)
        # self.config(menu=self.menu_bar)
        # self.menu_option = Menu(self.menu_bar, tearoff=0)
        # self.menu_option.add_command(label="Info", command=print("This is info menu"))
        # self.menu_option.add_command(label="Some new func")
        # self.menu_option.add_separator()
        # self.menu_option.add_command(label="Exit", command=self.destroy)
        # self.menu_bar.add_cascade(label="Options", menu=self.menu_option)

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

        # self.lista_produse_label = Label(self, text="", font=self.font)
        # self.lista_produse_label.place(x=10, y=115, width=850, height=600)

        self.tabel_produse_frame = Frame(self)
        self.tabel_produse_frame.place(x=10, y=115, width=850, height=600)

        self.coloane = ("ID", "Name", "Pret", "Bucate", "Pret Total")
        self.tabel_view = (Treeview(self.tabel_produse_frame, columns=self.coloane, show="headings", height=1000))
        self.tabel_view.grid(row=0, column=0)

        for coloana in self.coloane:
            self.tabel_view.heading(coloana, text=coloana)

        self.tabel_view.column("ID", width=50)
        self.tabel_view.column("Name", width=400)
        self.tabel_view.column("Pret", width=120)
        self.tabel_view.column("Bucate", width=120)
        self.tabel_view.column("Pret Total", width=160)
        self.tabel_view.grid(row=0, column=0)

        self.scroll_bar = Scrollbar(self.tabel_produse_frame, orient=VERTICAL, command=self.tabel_view.yview)
        self.tabel_view.configure(yscroll=self.scroll_bar.set)
        self.scroll_bar.grid(row=0, column=1)

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
    def dot(self):
        self.add_entry.insert(END, ".")

    def clear(self):
        self.add_entry.delete(0, END)


    def add(self):
        bar_code = int(self.add_entry.get())
        self.product = products_db.get_from_db_Products(bar_code)
        # print(product)
        # self.date_tabel = []
        # self.date_tabel.append(product)
        bucati_produs = Bucati(self.callback_bucati)
        # print(bucati_produs)
        # # Utilizează un index pentru a itera prin listă dacă ai nevoie să modifici elementele
        # for index, (id, nume, pret, buc, pret_total) in enumerate(self.date_tabel):
        #     id = index + 1
        #     buc = 1
        #     pret_total = pret * buc
        #
        #     self.date_tabel[index] = (id, nume, pret, buc, pret_total)
        #
        # for date in self.date_tabel:
        #     self.tabel_view.insert("", END, values=date)
        return self.product

    def callback_bucati(self, valoare):
        self.date_tabel = []
        self.date_tabel.append(self.product)
        # print(self.date_tabel)
        self.clear()
        for index, (id, nume, pret, buc, pret_total) in enumerate(self.date_tabel):
            id = id
            buc = valoare
            pret_total = pret * buc
            self.date_tabel[index] = (id, nume, pret, buc, pret_total)

        for date in self.date_tabel:
            self.tabel_view.insert("", END, values=date)
        # for index, (id, nume, pret, buc, pret_total) in enumerate(self.date_tabel):
        #     if index
        #             buc += 1
        #             pret_total = pret * buc
        #             self.date_tabel[index] = (id, nume, pret, buc, pret_total)

        # return valoare

    def delete(self):
        pass

    def anulare(self):
        self.lista_produse_label["text"] = ""
        self.produs_name_label["text"] = ""
        self.produs_pret_label["text"] = ""
        self.produs_code_label["text"] = ""

    def pachet(self):
        pass



# if __name__ == "__main__":
#     root2 = Root_work()
#     root2.mainloop()