# import tkinter
from tkinter import *
# from Controler import buttons


def search():
    print("Hello")


def button_0():
    work_interface.add_entry.insert(END, 0)


def button_1():
    work_interface.add_entry.insert(END, 1)


def button_2():
    work_interface.add_entry.insert(END, 2)


def button_3():
    work_interface.add_entry.insert(END, 3)


def button_4():
    work_interface.add_entry.insert(END, 4)


def button_5():
    work_interface.add_entry.insert(END, 5)


def button_6():
    work_interface.add_entry.insert(END, 6)


def button_7():
    work_interface.add_entry.insert(END, 7)


def button_8():
    work_interface.add_entry.insert(END, 8)


def button_9():
    work_interface.add_entry.insert(END, 9)


def clear():
    work_interface.add_entry.delete(0, END)


def dot():
    work_interface.add_entry.insert(END, ".")


def add():
    pass


def delete():
    pass


def anulare():
    pass


def pachet():
    pass


font = ("Colibri", 15)
font_bold = ("Colibri", 15, "bold")


window = Tk()
window.geometry("1550x750")
window.title("Workstation")
window.configure(bg="gray")
window.minsize(1250, 600)
window.maxsize(1920, 1080)


produs_code_message = Message(text="ID: ", font=font_bold, fg="black")
produs_code_message.place(x=10, y=10, width=120, height=40)


produs_code_label = Label(text="", font=font)
produs_code_label.place(x=130, y= 10, width= 1000, height= 40)


produs_name_message = Label(text="Name: ", font=font_bold, fg="black")
produs_name_message.place(x=10, y=55, width= 120, height= 40)


produs_name_label = Label(text="", font=font)
produs_name_label.place(x=130, y=55, width= 1000, height=40)


produs_buc_message = Label(text="Bucata: ",fg= "Black", font=font_bold)
produs_buc_message.place(x=1155, y=10, width=100, height= 40)


produs_buc_label = Label(text="", font=font, justify="left")
produs_buc_label.place(x=1255, y=10, width= 265, height= 40)


produs_pret_message = Label(text="Pret: ", fg="Black", font=font_bold)
produs_pret_message.place(x=1155, y=55, width=100, height= 40)


produs_pret_label = Label(text="", font=font, justify="left")
produs_pret_label.place(x=1255, y=55, width= 265, height=40)


line1 = Label()
line1.place(x=0, y= 105, width=1920, height=1)


lista_produse_label = Label(text="", font=font)
lista_produse_label.place(x=10, y=115, width=850, height=600)


line2 = Label(bg="gray")
line2.place(x=10, y=714, width=850, height=600)


total_message = Message(text="Total: ", font=font_bold)
total_message.place(x=10, y=715, width=100, height=40)


total_label = Label(text="", font=font_bold)
total_label.place(x=110, y=715, width=750, height=40)


white_label = Label()
white_label.place(x=885, y=115, width=635, height=600)


clear_button = Button(text="Clear", font=font_bold, command=clear)
clear_button.place(x=885, y=115, width=100, height=80)


add_entry = Entry(text="", font=font_bold, justify="center")
add_entry.place(x=985, y=115, width=535, height=80)


button_7 = Button(text=7, command=button_7, font=font_bold, bg="light blue")
button_7.place(x=885, y=200, width=100, height=80)


button_8 = Button(text=8, command=button_8, font=font_bold, bg="light blue")
button_8.place(x=995, y=200, width=100, height=80)


button_9 = Button(text=9, command=button_9, font=font_bold, bg="light blue")
button_9.place(x=1105, y=200, width=100, height=80)


button_4 = Button(text=4, command=button_4, font=font_bold, bg="light blue")
button_4.place(x=885, y=290, width=100, height=80)


button_5 = Button(text=5, command=button_5, font=font_bold, bg="light blue")
button_5.place(x=995, y=290, width=100, height=80)


button_6 = Button(text=6, command=button_6, font=font_bold, bg="light blue")
button_6.place(x=1105, y=290, width=100, height=80)


button_1 = Button(text=1, command=button_1, font=font_bold, bg="light blue")
button_1.place(x=885, y=380, width=100, height=80)


button_2 = Button(text=2, command=button_2, font=font_bold, bg="light blue")
button_2.place(x=995, y=380, width=100, height=80)


button_3 = Button(text=3, command=button_3, font=font_bold, bg="light blue")
button_3.place(x=1105, y=380, width=100, height=80)


search_button = Button(text="Search", command=search, font=font_bold, bg="light blue")
search_button.place(x=885, y=470, width=100, height=80)


button_0 = Button(text=0, command=button_0, font=font_bold, bg="light blue")
button_0.place(x=995, y=470, width=100, height=80)


dot_button = Button(text=".", command=dot, font=font_bold, bg="light blue")
dot_button.place(x=1105, y=470, width=100, height=80)


add_button = Button(text="Add", font=font_bold, bg="light green", command=add)
add_button.place(x=1215, y=200, width=300, height=80)


delete_button = Button(text="Delete", font=font_bold, bg="light green", command=delete)
delete_button.place(x=1215, y=290, width=300, height=80)


anulare_button = Button(text="Anulare", font=font_bold, bg="light green", command=anulare)
anulare_button.place(x=1215, y=380, width=300, height=80)


pachet_button = Button(text="Pachet", font=font_bold, bg="light blue", command=pachet)
pachet_button.place(x=1215, y=470, width=300, height=80)


window.mainloop()