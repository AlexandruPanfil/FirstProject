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
        # self.attributes('-fullscreen')
        self.geometry("1550x750")
        self.state('zoomed')
        self.title("Workstation")
        self.configure(bg="gray")
        self.iconbitmap("pythontutorial.ico")
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
        self.count = []
        self.total = 0.0

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


        self.tabel_view.column("ID", width=50, anchor="center")
        self.tabel_view.column("Name", width=400, anchor="center")
        self.tabel_view.column("Pret", width=120, anchor="center")
        self.tabel_view.column("Bucate", width=120, anchor="center")
        self.tabel_view.column("Pret Total", width=160, anchor="center")
        self.tabel_view.grid(row=0, column=0)

        self.scroll_bar = Scrollbar(self.tabel_produse_frame, orient=VERTICAL, command=self.tabel_view.yview)
        self.tabel_view.configure(yscroll=self.scroll_bar.set)
        self.scroll_bar.grid(row=0, column=1)

        self.line2 = Label(self, bg="gray")
        self.line2.place(x=10, y=715, width=850, height=600)

        self.total_message = Message(self, text="Total: ", font=self.font_bold)
        self.total_message.place(x=10, y=715, width=100, height=40)

        self.total_label = Label(self, text="", font=self.font_bold, justify="right")
        self.total_label.place(x=110, y=715, width=750, height=40)

        self.white_label = Label(self)
        self.white_label.place(x=885, y=110, width=635, height=640)

        self.clear_button = Button(self, text="Clear", font=self.font_bold, command=self.clear)
        self.clear_button.place(x=885, y=120, width=100, height=80)

        self.add_entry = Entry(self, text="", font=self.font_bold, justify="center")
        self.add_entry.place(x=995, y=120, width=515, height=80)

        self.button_7 = Button(self, text=7, command=self.button_7, font=self.font_bold, bg="light blue")
        self.button_7.place(x=885, y=210, width=100, height=80)

        self.button_8 = Button(self, text=8, command=self.button_8, font=self.font_bold, bg="light blue")
        self.button_8.place(x=995, y=210, width=100, height=80)

        self.button_9 = Button(self, text=9, command=self.button_9, font=self.font_bold, bg="light blue")
        self.button_9.place(x=1105, y=210, width=100, height=80)

        self.button_4 = Button(self, text=4, command=self.button_4, font=self.font_bold, bg="light blue")
        self.button_4.place(x=885, y=300, width=100, height=80)

        self.button_5 = Button(self, text=5, command=self.button_5, font=self.font_bold, bg="light blue")
        self.button_5.place(x=995, y=300, width=100, height=80)

        self.button_6 = Button(self, text=6, command=self.button_6, font=self.font_bold, bg="light blue")
        self.button_6.place(x=1105, y=300, width=100, height=80)

        self.button_1 = Button(self, text=1, command=self.button_1, font=self.font_bold, bg="light blue")
        self.button_1.place(x=885, y=390, width=100, height=80)

        self.button_2 = Button(self, text=2, command=self.button_2, font=self.font_bold, bg="light blue")
        self.button_2.place(x=995, y=390, width=100, height=80)

        self.button_3 = Button(self, text=3, command=self.button_3, font=self.font_bold, bg="light blue")
        self.button_3.place(x=1105, y=390, width=100, height=80)

        self.search_button = Button(self,text="Search", command=self.search, font=self.font_bold, bg="light blue")
        self.search_button.place(x=885, y=480, width=100, height=80)

        self.button_0 = Button(self, text=0, command=self.button_0, font=self.font_bold, bg="light blue")
        self.button_0.place(x=995, y=480, width=100, height=80)

        self.dot_button = Button(self,text=".", command=self.dot, font=self.font_bold, bg="light blue")
        self.dot_button.place(x=1105, y=480, width=100, height=80)

        self.add_button = Button(self,text="Add", font=self.font_bold, bg="light green", command=self.add)
        self.add_button.place(x=1215, y=210, width=300, height=80)

        self.delete_button = Button(self,text="Delete", font=self.font_bold, bg="light green", command=self.delete)
        self.delete_button.place(x=1215, y=300, width=300, height=80)

        self.anulare_button = Button(self,text="Anulare", font=self.font_bold, bg="light green", command=self.anulare)
        self.anulare_button.place(x=1215, y=390, width=300, height=80)

        self.pachet_button = Button(self,text="Pachet", font=self.font_bold, bg="light blue", command=self.pachet)
        self.pachet_button.place(x=1215, y=480, width=300, height=80)

        self.achitat_label = Label(self, text="Achitat", font=self.font_bold,)
        self.achitat_label.place(x=885, y=570, width=100, height=80)

        self.achitat_entry = Entry(self, text=0.0, font=self.font_bold, justify="center")
        self.achitat_entry.place(x=995, y=570, width=515, height=80)

        self.discount = Button(self, text="Discount", font=self.font_bold, justify="center", command=self.discount, bg="light pink")
        self.discount.place(x=885, y=660, width=200, height=80)

        self.achitat_card = Button(self, text="Card", font=self.font_bold, justify="center", command=self.card, bg="light pink")
        self.achitat_card.place(x=1098, y=660, width=200, height=80)

        self.achitat_cash = Button(self, text="Cash", font=self.font_bold, justify="center", command=self.cash, bg="light pink")
        self.achitat_cash.place(x=1311, y=660, width=200, height=80)

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
        bucati_produs = Bucati(self.callback_bucati)
        self.produs_name_label["text"] = self.product[1]
        self.produs_pret_label["text"] = self.product[2]
        self.produs_code_label["text"] = self.product[4]
        return self.product


    def callback_bucati(self, valoare):
        self.date_tabel = []
        self.date_tabel.append(self.product)
        self.clear()
        self.produs_buc_label["text"] = valoare
        for index, (id, nume, pret, buc, pret_total) in enumerate(self.date_tabel):
            self.count.append(id)
            id = len(self.count)
            buc = valoare
            pret_total = pret * buc
            self.date_tabel[index] = (id, nume, pret, buc, pret_total)


        for date in self.date_tabel:
            # print(date[4])
            self.total += date[4]
            self.total_label["text"] = f"{self.total:.2f}"
            self.tabel_view.insert("", END, values=date)

        # self.total = 0.0
        # for row in self.tabel_view.get_children():
        #     print(row)
        #     for coloana in self.tabel_view.item(row)["values"]:
        #         pass
        #     self.total += float(coloana)
        #     self.total_label["text"] = f"{self.total:.2f}"

        # for parent in self.tabel_view.get_children():
        #     # print(self.tabel_view(parent))
        #     for child in self.tabel_view.get_children(parent):
        #         data = self.tabel_view.item()["values"]
        #         print( data, self.tabel_view.item())
    ...
        # TODO This part of code, if the intem is duplicating to add more quantity
        # for index, (id, nume, pret, buc, pret_total) in enumerate(self.date_tabel):
        #     if index
        #             buc += 1
        #             pret_total = pret * buc
        #             self.date_tabel[index] = (id, nume, pret, buc, pret_total)

        # return valoare

    def delete(self):
        # TODO to clear all elements from tree view
        for item in self.tabel_view.get_children():
            self.tabel_view.delete(item)
        self.count = []
        self.produs_code_label["text"] = ""
        self.produs_name_label["text"] = ""
        self.produs_buc_label["text"] = ""
        self.produs_pret_label["text"] = ""


    def anulare(self):
        # TODO to clear last element from the tree view
        self.produs_code_label["text"] = ""
        self.produs_name_label["text"] = ""
        self.produs_buc_label["text"] = ""
        self.produs_pret_label["text"] = ""

    def pachet(self):
        self.add_entry.delete(0, END)
        self.add_entry.insert(0, "987987")
        self.add()

        # product = products_db.get_from_db_Products(987987)
        # self.date_tabel = []
        # self.date_tabel.append(product)
        # self.produs_name_label["text"] = product[1]
        # self.produs_pret_label["text"] = product[2]
        # self.produs_code_label["text"] = product[4]
        # self.produs_buc_label["text"] = 1

        # for index, (id, nume, pret, buc, pret_total) in enumerate(self.date_tabel):
        #     self.count.append(id)
        #     id = len(self.count)
        #     buc = 1
        #     pret_total = pret * 1
        #     self.date_tabel[index] = (id, nume, pret, buc, pret_total)
        #
        # for date in self.date_tabel:
        #     self.tabel_view.insert("", END, values=date)

    def discount(self):
        print("Discount 5%")
    def card(self):
        print("Achitat cu card, summa xxx")
    def cash(self):
        print("Achitat cu cash, summa xxx")



if __name__ == "__main__":
    root2 = Root_work()
    root2.mainloop()