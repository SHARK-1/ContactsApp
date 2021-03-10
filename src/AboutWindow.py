import tkinter as tk


class AboutWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.init_child()
        self.init_components()

    def init_child(self):
        self.title('About')
        self.geometry('382x265+700+250')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def init_components(self):
        refx_value = 0.05
        tk.Label(self, text='ContactsApp', font=("Times New Roman", 16, "bold")).place(relx=refx_value, rely=0.055)
        tk.Label(self, text='v. ?.?.?').place(relx=refx_value, rely=0.159)
        tk.Label(self, text='Author: Matinin Alexandr').place(relx=refx_value, rely=0.3)
        tk.Label(self, text='e-mail for feedback: sashasss95@gmail.com').place(relx=refx_value, rely=0.4526)
        tk.Label(self, text='GitHub: SHARK-1/ContactsApp').place(relx=refx_value, rely=0.5199)
        tk.Label(self, text='2021 Matinin Alexandr', font=("Times New Roman", 8)).place(relx=refx_value, rely=0.9174)
