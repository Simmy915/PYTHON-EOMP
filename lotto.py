
# Imports
from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
import datetime
from PIL import Image, ImageTk
import unittest


class Lotto:
    def __init__(self, master):
        self.master = master
        self.master.title('Lotto Machine: Simphiwe Sithole')
        self.master.geometry("740x520")
        self.master.configure(bg='yellow')
        self.master.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure('My.TSpinbox', arrowsize=15)

        self.my_image = ImageTk.PhotoImage(Image.open("ithuba.png"))
        self.image_label = Label(image=self.my_image, bg="yellow", pady=45, padx=45)
        self.image_label.place(x=280, y=30)

        # Player details
        self.details_frame = LabelFrame(master)
        self.details_frame.place(x=50, y=150, width=645, height=80)

        self.name_lbl = Label(self.details_frame, text="Player name:")
        self.name_lbl.place(x=10, y=30)

        self.name_entry = Entry(self.details_frame)
        self.name_entry.place(x=110, y=30)

        self.number_lbl = Label(self.details_frame, text="Player Number:")
        self.number_lbl.place(x=350, y=30)

        self.number_entry = Entry(self.details_frame)
        self.number_entry.place(x=460, y=30)

        # My number entries
        self.entry_frame = LabelFrame(master)
        self.entry_frame.place(x=50, y=240, width=645, height=85)

        self.choose = Label(self.entry_frame, text="Choose your numbers")
        self.choose.place(x=240, y=2)

        self.en1 = ttk.Spinbox(self.entry_frame, style='My.TSpinbox', from_=1, to=49, width=2, font=("arial", 30, 'bold'),
                               state='readonly')
        self.en1.place(x=10, y=25)
        self.en2 = ttk.Spinbox(self.entry_frame, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 30, 'bold'),
                               state='readonly')
        self.en2.place(x=117, y=25)
        self.en3 = ttk.Spinbox(self.entry_frame, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 30, 'bold'),
                               state='readonly')
        self.en3.place(x=230, y=25)
        self.en4 = ttk.Spinbox(self.entry_frame, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 30, 'bold'),
                               state='readonly')
        self.en4.place(x=334, y=25)
        self.en5 = ttk.Spinbox(self.entry_frame, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 30, 'bold'),
                               state='readonly')
        self.en5.place(x=453, y=25)
        self.en6 = ttk.Spinbox(self.entry_frame, style='My.TSpinbox', from_=1, to=49, width="2", font=("arial", 30, 'bold'),
                               state='readonly')
        self.en6.place(x=555, y=25)

        # Randomise button
        self.r_btn = Button(master, text="Results", fg="white", bg="green", font=("arial", 10, "bold"), padx=40, command=self.click)
        self.r_btn.place(x=320, y=330)

        # Out put of random numbers
        self.random_frame = LabelFrame(master)
        self.random_frame.place(x=50, y=380, width=645, height=80)

        self.r0 = Label(self.random_frame, text="0", font=("arial", 25, "bold"), bg="yellow", width=3, height=1, bd=5, relief=RIDGE)
        self.r0.place(x=10, y=10)
        self.r1 = Label(self.random_frame, text="0", font=("arial", 25, "bold"), bg="green", width=3, height=1, bd=5, relief=RIDGE)
        self.r1.place(x=120, y=10)
        self.r2 = Label(self.random_frame, text="0", font=("arial", 25, "bold"), bg="blue", width=3, height=1, bd=5, relief=RIDGE)
        self.r2.place(x=230, y=10)
        self.r3 = Label(self.random_frame, text="0", font=("arial", 25, "bold"), bg="tan", width=3, height=1, bd=5, relief=RIDGE)
        self.r3.place(x=340, y=10)
        self.r4 = Label(self.random_frame, text="0", font=("arial", 25, "bold"), bg="magenta", width=3, height=1, bd=5, relief=RIDGE)
        self.r4.place(x=450, y=10)
        self.r5 = Label(self.random_frame, text="0", font=("arial", 25, "bold"), bg="red", width=3, height=1, bd=5, relief=RIDGE)
        self.r5.place(x=560, y=10)

        # Clear button
        self.clear_btn = Button(master, text="Clear", bg="blue", fg="white", font=("arial", 10, "bold"), padx=40, command=self.clear)
        self.clear_btn.place(x=50, y=470)

        # Exit button
        self.exit_btn = Button(master, text="Exit", bg="red", fg="white", font=("arial", 10, "bold"), padx=40, command=self.exit)
        self.exit_btn.place(x=584, y=470)

    # Method to get the numbers from user and convert them to a list=====>>..>>
    def get_numbers(self):
        try:
            # Creating a list from the user input
            self.user_list = [int(self.en1.get()), int(self.en2.get()), int(self.en3.get()), int(self.en4.get()), int(self.en5.get()), int(self.en6.get())]
            self.user_list.sort()
            print('user: ', self.user_list)
            return self.user_list
        except ValueError:
            messagebox.showwarning('Fill all inputs', 'Please make sure that you entered 6 numbers')

    # Method to generate numbers and sort them
    def generate_random(self):
        self.r_num = random.sample(range(1, 50), 6)
        self.r_num.sort()
        print('random: ', self.r_num)
        return self.r_num

    # Method to compare the two lists
    def compare_lists(self):
        # calling get_numbers and generate method
        self.get_numbers()
        self.generate_random()

        # check if there no duplicates in the user entry
        if len(self.user_list) != len(set(self.user_list)):
            messagebox.showerror('Input Error', 'Make sure you do not repeat inputs')
        else:
            # Compare the two lists and filter the numbers that match
            self.res = list(set(self.user_list).intersection(self.r_num))
            print("matching are: ", self.res)
            return self.res

    def file_handling(self):
        # self.compare_lists()
        self.prize = {6: "R10, 000 000.00", 5: "R8,584.00", 4: "R2,384.00", 3: "R100.50", 2: "20.00", 1: "R0.00", 0: "R0.00"}

        self.player_name = self.name_entry.get()
        self.player_number = self.number_entry.get()
        self.my_key = len(self.res)
        self.today = datetime.datetime.now()  # get current date

        # printing to the text file
        self.file = open('lotto_storage.txt', 'a')
        self.file.write(f'{self.player_name}: Won {self.prize.get(self.my_key)} \n')
        self.file.write(f'Cell No: {self.player_number} \n')
        self.x = self.today.strftime("%x") + '\n' + 'Time: ' + \
            self.today.strftime("%X %p")
        self.file.write('Date: ' + str(self.x) + "\n \n")
        self.file.close()

    def click(self):
        self.player_name = self.name_entry.get()
        self.player_number = self.number_entry.get()

        if len(self.player_name) > 1 and len(self.player_number) > 1:
            # Calling the compare function
            self.compare_lists()

            self.r0.config(text=self.r_num[0])
            self.r1.config(text=self.r_num[1])
            self.r2.config(text=self.r_num[2])
            self.r3.config(text=self.r_num[3])
            self.r4.config(text=self.r_num[4])
            self.r5.config(text=self.r_num[5])

            if 2 <= len(self.res) <= 6:
                messagebox.showinfo('Winner', f'Congratulations {self.player_name} you have won')
                self.file_handling()
            elif 0 <= len(self.res) <= 1:
                messagebox.showinfo('You lose', 'Try again next time')
        else:
            messagebox.showerror('Input Error', 'Please make sure all the inputs are filled')

    # Method for clearing the inputs and outputs
    def clear(self):
        self.name_entry.delete(0, END)
        self.number_entry.delete(0, END)
        # Enabling the state of the spinbox so it can be cleared
        self.en1.config(state="normal")
        self.en2.config(state="normal")
        self.en3.config(state="normal")
        self.en4.config(state="normal")
        self.en5.config(state="normal")
        self.en6.config(state="normal")
        # clearing the spinbox
        self.en1.delete(0, END)
        self.en2.delete(0, END)
        self.en3.delete(0, END)
        self.en4.delete(0, END)
        self.en5.delete(0, END)
        self.en6.delete(0, END)
        # Disabling the state of the spinbox after it has been cleared
        self.en1.config(state="readonly")
        self.en2.config(state="readonly")
        self.en3.config(state="readonly")
        self.en4.config(state="readonly")
        self.en5.config(state="readonly")
        self.en6.config(state="readonly")
        # clear the random numbers output
        self.r0.config(text='0')
        self.r1.config(text='0')
        self.r2.config(text='0')
        self.r3.config(text='0')
        self.r4.config(text='0')
        self.r5.config(text='0')

    # Method for the exit Button
    def exit(self):
        self.message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
        if self.message_box == 'yes':
            self.master.destroy()
        else:
            pass


root = Tk()
app = Lotto(root)
root.mainloop()
