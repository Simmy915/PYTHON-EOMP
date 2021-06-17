#Simphiwe Sithole

from tkinter import *
from tkinter import messagebox
import datetime
from datetime import date
from PIL import Image, ImageTk


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title('Lotto Machine: Simphiwe Sithole')
        self.master.geometry("740x500")
        self.master.configure(bg='yellow')
        self.master.resizable(False, False)

        self.my_image = ImageTk.PhotoImage(Image.open("lotto.png"))
        self.image_label = Label(image=self.my_image, bg='yellow', pady=45, padx=45)
        self.image_label.place(x=280, y=30)

        self.frm = LabelFrame(master)
        self.frm.place(x=50, y=150, width=645, height=300)

        self.lbl1 = Label(self.frm, text="Enter your date of birth", font=("arial", 12))
        self.lbl1.place(x=230, y=40)

        self.year_entry = Entry(self.frm, width=4)
        self.year_entry.place(x=235, y=90)
        self.year_entry.insert(0, 'yyyy')
        self.year_entry.bind("<Button-1>", lambda event: self.clear_entry(event, self.year_entry))

        self.month_entry = Entry(self.frm, width=3)
        self.month_entry.place(x=300, y=90)
        self.month_entry.insert(0, 'mm')
        self.month_entry.bind("<Button-1>", lambda event: self.clear_entry(event, self.month_entry))

        self.day_entry = Entry(self.frm, width=3)
        self.day_entry.place(x=350, y=90)
        self.day_entry.insert(0, 'dd')
        self.day_entry.bind("<Button-1>", lambda event: self.clear_entry(event, self.day_entry))

        self.btn = Button(self.frm, text="Play", font=("arial", 10, "bold"), bg="skyblue", fg="white", padx=50, command=self.login)
        self.btn.place(x=250, y=140)

        # Exit button
        self.exit_btn = Button(self.frm, text="Exit", bg="red", fg="white", font=('arial', 10, 'bold'), padx=40, command=self.exit)
        self.exit_btn.place(x=520, y=250)


    def calc_age(self):
        self.my_date = datetime.date(int(self.year_entry.get()), int(self.month_entry.get()), int(self.day_entry.get()))
        self.today = date.today()
        self.age = self.today.year - self.my_date.year

        print(self.age)
        return self.age


    def clear_entry(self,event, entry):
        entry.delete(0, END)

    def login(self):

        try:
            self.age = self.calc_age()
            self.today = date.today()

            if self.age < 0:
                messagebox.showinfo("Date error", "Your birth date cannot in the future")
            elif self.age <= 5:
                messagebox.showinfo("Too young", "What do you even know about lotto")
            elif 18 <= self.age <= 110 and type(self.age) == int:
                messagebox.showinfo("Successful", "Congatulations you qualify to play")
                file = open('lotto_storage.txt', 'w')
                file.write('File created on: ' + str(self.today) + "\n \n")
                file.close()
                self.master.destroy()
                import lotto
                lotto.Lotto
            elif type(self.age) == str:
                messagebox.showerror("Invalid Input", "Please make sure you enter valid input")
            else:
                messagebox.showwarning("Warning", "Sorry you can't play")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please make sure you enter valid input")

        # Method for the exit Button
    def exit(self):
        self.message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
        if self.message_box == 'yes':
            self.master.destroy()
        else:
            pass


root = Tk()
app = Login(root)
root.mainloop()
