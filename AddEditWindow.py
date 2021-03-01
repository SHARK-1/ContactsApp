import tkinter as tk
from Contact import Contact


class AddEditWindow(tk.Toplevel):
    def __init__(self, root, fields):
        super().__init__(root)
        self.init_child()
        self.fields = fields
        self.init_components()
        self.__new_contact = Contact()

    def init_child(self):
        self.title('Add/Edit Contact')
        self.geometry('440x210+700+250')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def init_components(self):
        self.__entrys = {}
        self.__string_vars = {}
        for i, value in enumerate(self.fields):
            frame = tk.Frame(self)
            frame.place(x=0, y=i * 25 + 10, width=70, height=30)
            label = tk.Label(frame, text=value)
            label.pack(side=tk.RIGHT)

            frame = tk.Frame(self)
            frame.place(x=75, y=i * 25 + 10, relwidth=1, height=30)
            self.__string_vars[value] = tk.StringVar()
            self.__entrys[value] = tk.Entry(frame, textvariable=self.__string_vars[value], width=57)
            self.__entrys[value].pack(side=tk.LEFT)
            self.__string_vars[value].trace("w", lambda a, b, c, x=value: self.check_correct_value(x))
        self.ok_button = tk.Button(self, text='ОК')
        self.ok_button.place(relx=0.6, rely=0.85, width=80)
        self.cancel_button = tk.Button(self, text='Cansel', command=self.destroy)
        self.cancel_button.place(relx=0.8, rely=0.85, width=80)

    def check_correct_value(self, *args):

        if args[0] == 'Name:':
            try:
                self.__new_contact.first_name = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg='red')
            else:
                self.__entrys[args[0]].config(bg='#ffffff')

        if args[0] == 'Surname:':
            try:
                self.__new_contact.last_name = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg='red')
            else:
                self.__entrys[args[0]].config(bg='#ffffff')

        if args[0] == 'Birthday:':
            try:
                self.__new_contact.date_of_birth = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg='red')
            else:
                self.__entrys[args[0]].config(bg='#ffffff')


        if args[0] == 'Phone:':
            try:
                self.__new_contact.phone = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg='red')
            else:
                self.__entrys[args[0]].config(bg='#ffffff')

        # if args[0] == 'E-Mail:':
        #     try:
        #         self.__e-mail. = self.__entrys[args[0]].get()
        #     except BaseException:
        #         self.__entrys[args[0]].config(bg='red')
        #     else:
        #         self.__entrys[args[0]].config(bg='#ffffff')

        if args[0] == 'vk.com:':
            try:
                self.__new_contact.social_network = self.__entrys[args[0]].get()
            except BaseException:
                self.__entrys[args[0]].config(bg='red')
            else:
                self.__entrys[args[0]].config(bg='#ffffff')


# ['Name:', 'Surname:', 'Birthday:', 'Phone:', 'E-Mail:', 'vk.com:']
