#Simphiwe Sithole

import datetime
from tkinter import *
from tkinter import messagebox
from validate_email import validate_email
import rsaidnumber
from dateutil import relativedelta
root = Tk()
img = PhotoImage(file='ithuba.png')
img = img.subsample(16)
lbl_image = Label(root, image=img, bg="yellow")
lbl_image.place(x=240, y=260)


class EmailError(Exception):
    pass
class IdLengthError(Exception):
    pass

class LottoGUI:
    def __init__(self, master):
#THIS IS THE WINDOW SET UP ..

        self.master = master
        self.master.title("")
        self.master.geometry("600x400")
        self.master.config(bg="blue")

#THIS IS THE LOGIN PAGE..

        self.frame = Frame(self.master, width=450, height=200, bg="green")
        self.frame.place(x=25, y=95)
        self.lbl_head = Label(self.master, text="FEELING LUCKY\nTODAY?\n", width=12, font="monospace 12 bold", bg="yellow", fg="red")
        self.lbl_head.place(x=160, y=20)
        self.lbl_subhead = Label(self.frame, text="Wanna play? Please enter your details", font="Garuda 12 bold", bg="yellow", fg="red")
        self.lbl_subhead.place(x=80, y=20)


        self.lbl_name = Label(self.frame, text="Name", font="Garuda 12", bg="green", fg="white")
        self.lbl_email = Label(self.frame, text="Email", font="Garuda 12", bg="green", fg="white")
        self.lbl_id = Label(self.frame, text="South African ID number", font="Garuda 12", bg="green", fg="white")
        self.lbl_name.place(x=60, y=60)
        self.lbl_email.place(x=60, y=100)
        self.lbl_id.place(x=60, y=140)

        #THIS ARE THE FUNCTION AND DETAILS OF THE LOGIN PAGE

        self.entry_email = Entry(self.frame, borderwidth="0")
        self.entry_name = Entry(self.frame, borderwidth="0")
        self.entry_id = Entry(self.frame, borderwidth="0")
        self.entry_name.place(x=245, y=67)
        self.entry_email.place(x=245, y=107)
        self.entry_id.place(x=245, y=147)

        #CREATING BUTTONS THAT WILL VALIDATE
        self.btn_validate = Button(self.master, text="Validate", bg="green", fg="green", borderwidth="0",
                                   highlightbackground="red", activebackground="red",
                                   activeforeground="yellow", command=self.validate)
        self.btn_validate.place(x=30, y=340)

        #CREATING BUTTONS THAT WILL CLEAR WHEN ACTIVATED...

        self.btn_clear = Button(self.master, text="Clear", bg="green", fg="green", borderwidth="0",
                                highlightbackground="red", activebackground="red", activeforeground="blue",
                                command=self.clear)
        self.btn_clear.place(x=350, y=340)

        #THIS BUTTON WILL EXIT THE APPLICATION WHEN ACTIVATED ...
        self.btn_exit = Button(self.master, text="Exit", bg="green", fg="green", borderwidth="0",
                               highlightbackground="yellow", activebackground="yellow",
                               activeforeground="red", command=exit)
        self.btn_exit.place(x=430, y=340)

        self.master.mainloop()

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_id.delete(0, 'end')

    def validate(self):
        try:
            if not validate_email(self.entry_email.get()):
                raise EmailError

            int(self.entry_id.get())
            id = (self.entry_id.get())
            date_of_birth = rsaidnumber.parse(id).date_of_birth
            if len(id) < 13 or len(id) > 13:
                raise IdLengthError
            elif relativedelta.relativedelta(datetime.datetime.today(), date_of_birth).years < 18:
                messagebox.showerror("Error", "You are too young to play. Try again next time.")

            else:
                messagebox.showinfo("You are through!", "Let's play!")
                root.withdraw()
                import play

        except EmailError:
            messagebox.showerror("Error", "THe format of your e-mail address is invalid")

        except ValueError:
            messagebox.showerror("Error", "Your RSA ID number is invalid")

        except IdLengthError:
            messagebox.showerror("Error", "Your RSA ID number should only contain 13 digits")

LottoGUI(root)

