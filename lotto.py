# Simphiwe Sithole

class Lotto:
    def __init__(self, master):
        self.master = master
        self.master.title('Lotto Machine: Simphiwe Sithole')
        self.master.geometry("780 x620")
        self.master.configure(bg='red')
        self.master.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure('My.TSpinbox', arrowsize=15)

        self.my_image = ImageTk.PhotoImage(Image.open("ithuba.png"))
        self.image_label = Label(image=self.my_image, bg="red", pady=50, padx=50)
        self.image_label.place(x=280, y=30)

        #These are the player details

        self.details_frame = LabelFrame(master)
        self.details_frame.place(x=50, y=150, width=645, height=80)

        self.name_lbl = Label(self.details_frame, text="Player name:")
        self.name_lbl.place(x=10, y=30)

        self.name_entry = Entry(self.details_frame)
        self.name_entry.place(x=110, y=30)

        self.number_lbl = Label(self.details_frame, text="ID Number:")
        self.number_lbl.place(x=350, y=30)

        self.number_entry = Entry(self.details_frame)
        self.number_entry.place(x=460, y=30)

        self.number_lbl = Label(self.details_frame, text="Email address:")
        self.number_lbl.place(x=350, y=20)

        self.number_entry = Entry(self.details_frame)
        self.number_entry.place(x=460, y=30)


