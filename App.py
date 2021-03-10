import tkinter as tk
from Project import Project
from AboutWindow import AboutWindow
from AddEditWindow import AddEditWindow
from ProjectManager import ProjectManager


class App(tk.Frame):
    def __init__(self, root):
        self.root = root
        super().__init__(root)

        self.add_menu_bar(root)
        self.add_components(root)
        self.__project = Project()
        self.__current_listbox_item = None

    def add_menu_bar(self, root):
        mainmenu = tk.Menu(root)
        root.config(menu=mainmenu)

        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Exit", command=self.destroy_main_window)

        editmenu = tk.Menu(mainmenu, tearoff=0)
        editmenu.add_command(label="Add Contact", command=self.open_add_window)
        editmenu.add_command(label="Edit Contact")
        editmenu.add_command(label="Remove Contact")
        editmenu.add_command(label="Save", command=self.save_contacts)
        editmenu.add_command(label="Load", command=self.load_contacts)

        helpmenu = tk.Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="About", command=self.open_about_window)

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

        right_left_frame = tk.Frame(right_frame, width=75)
        right_left_frame.place(relx=0, rely=0, relwidth=0.1374, relheight=1)

        right_right_frame = tk.Frame(right_frame, width=75)
        right_right_frame.place(relx=0.1374, rely=0, relwidth=0.8626, relheight=1)

        self.list_box = tk.Listbox(left_frame, width=39, height=22)
        self.list_box.pack(side=tk.TOP, padx=1, pady=1)

        left_frame_width_buttons = tk.Frame(root)
        left_frame_width_buttons.place(relx=0.01, rely=0.925, width=75, height=25)

        self.add_images = tk.PhotoImage(file="Images/Add_img.png")
        add_button = tk.Button(left_frame_width_buttons, image=self.add_images, bd=0, command=self.open_add_window)
        add_button.place(x=0, y=0, width=20, height=20)

        self.edit_images = tk.PhotoImage(file="Images/Edit_img.png")
        add_button = tk.Button(left_frame_width_buttons, image=self.edit_images, bd=0, command=self.open_edit_window)
        add_button.place(x=25, y=0, width=20, height=20)

        self.del_images = tk.PhotoImage(file="Images/Delet_img.png")
        add_button = tk.Button(left_frame_width_buttons, image=self.del_images, bd=0, command=self.del_contact)
        add_button.place(x=50, y=0, width=20, height=20)

        # Лейблы для описания полей вsdjlf
        self.__info_labels = []
        self.label_data = ['Name:', 'Surname:', 'Birthday:', 'Phone:', 'E-Mail:', 'vk.com:']
        for i, value in enumerate(self.label_data):
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

        self.list_box.bind('<<ListboxSelect>>', self.list_box_select)

    def list_box_select(self, event):
        widget = event.widget
        self.__selection = widget.curselection()
        if self.__selection:
            self.__current_listbox_item = self.__selection[0]
            contact = self.__project.get_contact(self.__current_listbox_item)
            self.fill_fields(contact)

    def open_about_window(self):
        AboutWindow(self.root)

    def open_add_window(self):
        AddEditWindow(self)

    def open_edit_window(self):
        AddEditWindow(self, mode='edit', contact=self.__project.get_contact(self.__selection[0]))

    def change_contact(self, new_contact):
        self.__project.del_contact_by_index(self.__current_listbox_item)
        self.add_new_contact(new_contact)

    def add_new_contact(self, new_contact):
        self.__project.add_contact(new_contact)
        if self.__current_listbox_item == None:
            self.__current_listbox_item = 0
        self.update_list_box()

    def del_contact(self):
        if self.__current_listbox_item == None:
            return None
        self.__project.del_contact_by_index(self.__current_listbox_item)
        if len(self.__project.get_all_contacts()) == 0:
            self.__current_listbox_item = None
            self.update_list_box()
        else:
            self.__current_listbox_item = 0
            self.update_list_box()

    def update_list_box(self):
        self.list_box.delete(0, tk.END)
        i = 0
        for contact in self.__project.get_all_contacts():
            i += 1
            self.list_box.insert(tk.END, contact.last_name)
        if i == 0:
            self.fill_fields()
        else:
            self.fill_fields(self.__project.get_contact(self.__current_listbox_item))

    def save_contacts(self):
        ProjectManager.save(self.__project)

    def load_contacts(self):
        self.__project = ProjectManager.load()
        if len(self.__project.get_all_contacts()) == 0:
            self.__current_listbox_item = None
        else:
            self.__current_listbox_item = 0
        self.update_list_box()

    def fill_fields(self, contact=None):
        if contact != None:
            self.__info_labels[0].config(
                text=contact.first_name)
            self.__info_labels[1].config(
                text=contact.last_name)
            self.__info_labels[2].config(
                text=contact.date_of_birth)
            self.__info_labels[3].config(
                text=contact.phone)
            self.__info_labels[4].config(
                text=contact.email)
            self.__info_labels[5].config(
                text=contact.social_network)
        else:
            self.__info_labels[0].config(
                text='')
            self.__info_labels[1].config(
                text='')
            self.__info_labels[2].config(
                text='')
            self.__info_labels[3].config(
                text='')
            self.__info_labels[4].config(
                text='')
            self.__info_labels[5].config(
                text='')

    def destroy_main_window(self):
        self.root.destroy()

