import tkinter as tk


class AddEditWindow(tk.Toplevel):
    def __init__(self, root, fields):
        super().__init__(root)
        self.init_child()
        self.fields = fields
        self.init_components()

    def init_child(self):
        self.title('Add/Edit Contact')
        self.geometry('440x210+700+250')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def init_components(self):
        self.__entrys = []
        for i, value in enumerate(self.fields):
            frame = tk.Frame(self)
            frame.place(x=0, y=i * 25 + 10, width=70, height=30)
            label = tk.Label(frame, text=value)
            label.pack(side=tk.RIGHT)

            frame = tk.Frame(self)
            frame.place(x=75, y=i * 25 + 10, relwidth=1, height=30)
            entry = tk.Entry(frame, width=57)
            entry.pack(side=tk.LEFT)
            self.__entrys.append(label)

        self.ok_button = tk.Button(self, text='ОК')
        self.ok_button.place(relx=0.6, rely=0.85,width=80)
        self.cancel_button = tk.Button(self, text='Cansel', command=self.destroy)
        self.cancel_button.place(relx=0.8, rely=0.85,width=80)
