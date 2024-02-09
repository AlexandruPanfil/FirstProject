from tkinter import *
from Controler.authentification import authentification
from View import work_interface


def connect():
    user = entry_user.get()
    pasw = entry_password.get()
    enter = authentification(user, pasw)
    if enter == True:
        work_interface
        window.destroy()

window = Tk()
window.geometry("400x200+500+200")
window.title("Alexandru Panfil First Project")

label_introducere = Label(text="Salut, aici te logezi in urmatoarea programa", font=("Colibri", 10))
label_introducere.place(x=50, y=20, width =300, height= 25)

label_user = Label(text="Username: ")
label_user.place(x=35, y= 60, width=100, height= 25)

entry_user = Entry(text="", justify="center")
entry_user.place(x=145, y=60, width= 210, height =25)
entry_user.focus()

label_password = Label(text="Password: ")
label_password.place(x=35, y=90, width=100, height =25)

entry_password = Entry(text="", justify="center")
entry_password.place(x=145, y=90, width=210, height=25)

button_connect = Button(text="Connect", command=connect, bg="light green")
button_connect.place(x=100, y=135, width=200, height=30)


window.mainloop()