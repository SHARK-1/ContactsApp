import tkinter as tk
from Contact import Contact

ERR_BG = 'red'
CURRENT_BG = '#ffffff'


class AddEditWindow(tk.Toplevel):

    def __init__(self, parent, mode='add', contact=None):
        '''
        :param fields: names of fields(first name, last name ...)
        :param mode: 'add' or 'edit'
        :param mode: if mode==edit
        '''
        self.__parrent = parent
        super().__init__(parent)
        self.init_child()
        self.__fields = ['Name:', 'Surname:', 'Birthday:', 'Phone:', 'E-Mail:', 'vk.com:']
        if contact != None:
            self.__contact = contact
        else:
            self.__contact = Contact()

        self.__mode = mode

        if self.__mode == 'add' or self.__mode == 'edit':
            self.init_components(mode)
        else:
            raise ValueError('Param mode must be "add" or "edit"')

    def init_child(self):
        self.title('Add/Edit Contact')
        self.geometry('440x210+700+250')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def init_components(self, mode):
        self.__entrys = {}
        self.__string_vars = {}

        if mode == 'add':
            init_bg = ERR_BG
        else:
            init_bg = CURRENT_BG

        for i, value in enumerate(self.__fields):
            frame = tk.Frame(self)
            frame.place(x=0, y=i * 25 + 10, width=70, height=30)
            label = tk.Label(frame, text=value)
            label.pack(side=tk.RIGHT)

            frame = tk.Frame(self)
            frame.place(x=75, y=i * 25 + 10, relwidth=1, height=30)
            self.__string_vars[value] = tk.StringVar()

            if mode == 'add':
                self.__entrys[value] = tk.Entry(frame, textvariable=self.__string_vars[value], bg=init_bg, width=57)
            else:
                # ['Name:', 'Surname:', 'Birthday:', 'Phone:', 'E-Mail:', 'vk.com:']
                if value == 'Name:':
                    self.__string_vars[value].set(self.__contact.first_name)
                elif value == 'Surname:':
                    self.__string_vars[value].set(self.__contact.last_name)
                elif value == 'Birthday:':
                    self.__string_vars[value].set(self.__contact.date_of_birth)
                elif value == 'Phone:':
                    self.__string_vars[value].set(self.__contact.phone)
                elif value == 'E-Mail:':
                    self.__string_vars[value].set(self.__contact.email)
                elif value == 'vk.com:':
                    self.__string_vars[value].set(self.__contact.social_network)

                self.__entrys[value] = tk.Entry(frame, textvariable=self.__string_vars[value], bg=init_bg, width=57)

            self.__entrys[value].pack(side=tk.LEFT)
            self.__string_vars[value].trace("w", lambda a, b, c, x=value: self.check_correct_value(x))

        self.ok_button = tk.Button(self, text='ОК', command=self.ok_button)
        self.ok_button.place(relx=0.6, rely=0.85, width=80)
        self.cancel_button = tk.Button(self, text='Cansel', command=self.destroy)
        self.cancel_button.place(relx=0.8, rely=0.85, width=80)

    def check_correct_value(self, *args):
        if args[0] == 'Name:':
            try:
                self.__contact.first_name = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg=ERR_BG)
            else:
                self.__entrys[args[0]].config(bg=CURRENT_BG)

        if args[0] == 'Surname:':
            try:
                self.__contact.last_name = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg=ERR_BG)
            else:
                self.__entrys[args[0]].config(bg=CURRENT_BG)

        if args[0] == 'Birthday:':
            try:
                self.__contact.date_of_birth = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg=ERR_BG)
            else:
                self.__entrys[args[0]].config(bg=CURRENT_BG)

        if args[0] == 'Phone:':
            try:
                self.__contact.phone = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg=ERR_BG)
            else:
                self.__entrys[args[0]].config(bg=CURRENT_BG)

        if args[0] == 'E-Mail:':
            try:
                self.__contact.email = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg=ERR_BG)
            else:
                self.__entrys[args[0]].config(bg=CURRENT_BG)

        if args[0] == 'vk.com:':
            try:
                self.__contact.social_network = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg=ERR_BG)
            else:
                self.__entrys[args[0]].config(bg=CURRENT_BG)

    def ok_button(self):
        if self.__mode == 'add':
            self.__parrent.add_new_contact(self.__contact)
        else:
            self.__parrent.change_contact(self.__contact)
        self.destroy()
