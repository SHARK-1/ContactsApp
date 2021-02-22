import tkinter as tk


class App(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.add_menu_bar(root)
        self.add_components(root)

    def add_menu_bar(self, root):
        mainmenu = tk.Menu(root)
        root.config(menu=mainmenu)

        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Exit")

        editmenu = tk.Menu(mainmenu, tearoff=0)
        editmenu.add_command(label="Add Contact")
        editmenu.add_command(label="Edit Contact")
        editmenu.add_command(label="Remove Contact")

        helpmenu = tk.Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="About")

        mainmenu.add_cascade(label="File", menu=filemenu)
        mainmenu.add_cascade(label="Edit", menu=editmenu)
        mainmenu.add_cascade(label="Help", menu=helpmenu)

    def add_components(self, root):

        left_frame = tk.Frame(root)
        left_frame.place(relx=0, rely=0, relwidth=0.328, relheight=0.9)

        right_frame = tk.Frame(root, bg='red')
        right_frame.place(relx=0.328, rely=0, relwidth=0.672, relheight=0.83)

        left_top_frame = tk.Frame(left_frame, width=50)
        left_top_frame.pack(side=tk.TOP, fill=tk.X)
        #
        right_left_frame = tk.Frame(right_frame, width=75)
        right_left_frame.place(relx=0, rely=0, relwidth=0.1374, relheight=1)

        right_right_frame = tk.Frame(right_frame, width=75)
        right_right_frame.place(relx=0.1374, rely=0, relwidth=0.8626, relheight=1)

        self.list_box = tk.Listbox(left_frame, width=39, height=22)
        self.list_box.pack(side=tk.TOP, padx=1, pady=1)

        left_frame_width_buttons=tk.Frame(root)
        left_frame_width_buttons.place(relx=0.01,rely=0.94,width=75,height=25)

        self.add_images = tk.PhotoImage(file="Images/Add_img.png")
        add_button = tk.Button(left_frame_width_buttons, image=self.add_images, bd=0,command=self.print)
        add_button.place(x=0, y=0, width=20, height=20)

        self.edit_images = tk.PhotoImage(file="Images/Edit_img.png")
        add_button = tk.Button(left_frame_width_buttons, image=self.edit_images, bd=0, command=self.print)
        add_button.place(x=25, y=0, width=20, height=20)

        self.del_images = tk.PhotoImage(file="Images/Delet_img.png")
        add_button = tk.Button(left_frame_width_buttons, image=self.del_images, bd=0, command=self.print)
        add_button.place(x=50, y=0, width=20, height=20)


        # Лейблы для описания полей вsdjlf
        self.__info_labels = []
        label_data = ['Surname:', 'Name:', 'Birthday:', 'Phone:', 'E-Mail:', 'vk.com:']
        for i, value in enumerate(label_data):
            frame = tk.Frame(right_left_frame)
            frame.place(x=0, y=i * 25, relwidth=1, height=30)
            label = tk.Label(frame, text=value)
            label.pack(side=tk.RIGHT)

            frame = tk.Frame(right_right_frame)
            frame.place(x=0, y=i * 25, relwidth=1, height=30)
            label = tk.Label(frame, width=63, bg='#ffffff', bd=2, relief=tk.GROOVE)
            label.pack(side=tk.LEFT)
            self.__info_labels.append(label)

        label = tk.Label(left_top_frame, text='  Find: ')
        label.pack(side=tk.LEFT, padx=1, pady=1)

        self.entry = tk.Entry(left_top_frame, width=33, state=tk.NORMAL)
        self.entry.pack(side=tk.LEFT, padx=1, pady=1)

        # self.list_box.bind('<<ListboxSelect>>', self.on_change)

    def on_change(self, event):
        widget = event.widget  # виджет, с которым произошло событие (в данном случае listbox)
        selection = widget.curselection()  # получаем список индексов выделенных элементов
        if selection:  # если что-то выделено
            text = widget.get(selection[0])  # Текст в выбранной строке
            # выводим текст выделенного элемента в консоль
            print(text)

    def print(self):
        print('hello')
