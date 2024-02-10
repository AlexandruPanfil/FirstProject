from tkinter import Tk, Label, Button, Entry
from Controler.authentification import authentification
from View.work_interface import Root_work

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.star_width = 200
        self.start_height = 400
        self.geometry(f"{self.start_height}x{self.star_width}+500+200")
        self.title("Alexandru Panfil First Project")

        self.label_introducere = Label(self, text="Salut, aici te logezi in urmatoarea programa", font=("Colibri", 10))
        self.label_introducere.place(x=50, y=20, width =300, height= 25)

        self.label_user = Label(self, text="Username: ")
        self.label_user.place(x=35, y= 60, width=100, height= 25)

        self.entry_user = Entry(self, text="", justify="center")
        self.entry_user.place(x=145, y=60, width= 210, height =25)
        self.entry_user.focus()

        self.label_password = Label(self, text="Password: ")
        self.label_password.place(x=35, y=90, width=100, height =25)

        self.entry_password = Entry(self, text="", justify="center")
        self.entry_password.place(x=145, y=90, width=210, height=25)

        self.button_connect = Button(self, text="Connect", command=self.connect, bg="light green")
        self.button_connect.place(x=100, y=135, width=200, height=30)

    def connect(self):
        user = self.entry_user.get()
        pasw = self.entry_password.get()
        enter = authentification(user, pasw)
        if enter:
            self.destroy()
            root2 = Root_work()
            root2.mainloop()
        else:
            print("Log failed")


if __name__ == "__main__":
    root = Root()
    root.mainloop()
